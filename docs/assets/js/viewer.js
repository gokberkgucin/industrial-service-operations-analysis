(function () {
  const manifestPath = "data/page_manifest.json";
  let manifest = [];
  let currentIndex = 0;
  let observer = null;

  function byAttr(name) {
    return document.querySelector(`[${name}]`);
  }

  async function loadManifest() {
    const response = await fetch(manifestPath);
    if (!response.ok) {
      throw new Error(`${manifestPath} yüklenemedi`);
    }
    return response.json();
  }

  function imageSrc(page) {
    return page.image_path.replace(/^docs\//, "");
  }

  function pageText(page) {
    return `${page.page_label} - ${page.section}`;
  }

  function renderIndexSummary() {
    const target = byAttr("data-summary");
    if (!target) return;

    const sections = Array.from(new Set(manifest.map((page) => page.section))).filter(Boolean);
    target.innerHTML = [
      "<h2>Yayın Özeti</h2>",
      `<p>${manifest.length} sayfa manifest içinde kayıtlı.</p>`,
      `<p>Bölümler: ${sections.join(", ")}</p>`,
    ].join("");
  }

  function normalizeSearchText(value) {
    return String(value || "").toLocaleLowerCase("tr");
  }

  function renderSearchResults(items, query) {
    const results = byAttr("data-search-results");
    const count = byAttr("data-search-count");
    if (!results || !count) return;

    const normalized = normalizeSearchText(query);
    const filtered = normalized
      ? items.filter((item) => normalizeSearchText(item.search_text).includes(normalized))
      : items;

    count.textContent = normalized
      ? `${filtered.length} sonuç bulundu.`
      : `${items.length} sayfa aranabilir.`;

    results.innerHTML = "";
    filtered.slice(0, 50).forEach((item) => {
      const article = document.createElement("article");
      article.className = "search-result";

      const title = document.createElement("a");
      title.href = item.full_text_path;
      title.textContent = `${item.page_label}: ${item.title}`;

      const meta = document.createElement("p");
      meta.className = "search-meta";
      meta.textContent = item.section;

      const excerpt = document.createElement("p");
      excerpt.textContent = item.text_excerpt;

      const scan = document.createElement("a");
      scan.href = item.scan_path;
      scan.textContent = "Sayfa görüntüsüne git";

      article.append(title, meta, excerpt, scan);
      results.appendChild(article);
    });

    if (filtered.length > 50) {
      const note = document.createElement("p");
      note.className = "search-meta";
      note.textContent = "İlk 50 sonuç gösteriliyor.";
      results.appendChild(note);
    }
  }

  async function initSearch() {
    const root = byAttr("data-search-root");
    if (!root) return;
    const input = byAttr("data-search-input");
    const response = await fetch("data/search_index.json");
    if (!response.ok) {
      throw new Error("search_index.json yüklenemedi");
    }
    const items = await response.json();
    renderSearchResults(items, "");
    if (input) {
      input.addEventListener("input", () => renderSearchResults(items, input.value));
    }
  }

  function populateControls() {
    const select = byAttr("data-page-select");
    const list = byAttr("data-page-list");
    if (!select || !list) return;

    select.innerHTML = "";
    list.innerHTML = "";

    manifest.forEach((page, index) => {
      const option = document.createElement("option");
      option.value = String(index);
      option.textContent = pageText(page);
      select.appendChild(option);

      const link = document.createElement("a");
      link.href = `#page-${String(page.page_index).padStart(3, "0")}`;
      link.textContent = `${page.page_label} · ${page.short_title}`;
      link.dataset.pageIndex = String(index);
      link.addEventListener("click", (event) => {
        event.preventDefault();
        showPage(index, true);
      });
      list.appendChild(link);
    });

    select.addEventListener("change", () => {
      showPage(Number(select.value), true);
    });

    const prev = byAttr("data-prev-page");
    const next = byAttr("data-next-page");
    if (prev) prev.addEventListener("click", () => showPage(currentIndex - 1, true));
    if (next) next.addEventListener("click", () => showPage(currentIndex + 1, true));
  }

  function renderPageStream() {
    const stream = byAttr("data-page-stream");
    if (!stream) return;

    stream.innerHTML = "";
    manifest.forEach((page, index) => {
      const article = document.createElement("article");
      article.className = "scan-frame";
      article.id = `page-${String(page.page_index).padStart(3, "0")}`;
      article.dataset.pageIndex = String(index);

      const header = document.createElement("header");
      header.className = "scan-header";

      const label = document.createElement("p");
      label.className = "scan-label";
      label.textContent = `Belge etiketi: ${page.page_label} · Manifest sırası: ${page.page_index}/${manifest.length}`;

      const title = document.createElement("h2");
      title.textContent = page.short_title || pageText(page);

      const section = document.createElement("p");
      section.className = "scan-section";
      section.textContent = page.section;

      const links = document.createElement("p");
      links.className = "scan-links";
      const transcript = document.createElement("a");
      transcript.href = page.transcript_path || `transcript/page-${String(page.page_index).padStart(3, "0")}.html`;
      transcript.textContent = "Transcript";
      links.appendChild(transcript);

      const image = document.createElement("img");
      image.className = "scan-image";
      image.src = imageSrc(page);
      image.alt = page.alt_text || `${page.page_label}: ${page.short_title || page.section}`;
      image.loading = index === 0 ? "eager" : "lazy";
      image.decoding = "async";
      if (page.image_width) image.width = page.image_width;
      if (page.image_height) image.height = page.image_height;

      header.append(label, title, section, links);
      article.append(header, image);
      stream.appendChild(article);
    });
  }

  function scrollToCurrent() {
    const target = document.querySelector(`[data-page-index="${currentIndex}"].scan-frame`);
    if (target) {
      target.scrollIntoView({ behavior: "smooth", block: "start" });
    }
  }

  function startObserver() {
    const frames = document.querySelectorAll(".scan-frame[data-page-index]");
    if (!frames.length || !("IntersectionObserver" in window)) return;

    observer = new IntersectionObserver(
      (entries) => {
        const visible = entries
          .filter((entry) => entry.isIntersecting)
          .sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];
        if (!visible) return;
        const nextIndex = Number(visible.target.dataset.pageIndex);
        if (!Number.isNaN(nextIndex) && nextIndex !== currentIndex) {
          showPageInternal(nextIndex, false, false);
        }
      },
      { root: null, threshold: [0.35, 0.65] }
    );

    frames.forEach((frame) => observer.observe(frame));
  }

  function showPage(index, updateHash) {
    return showPageInternal(index, updateHash, true);
  }

  function showPageInternal(index, updateHash, shouldScroll) {
    if (!manifest.length) return;
    currentIndex = Math.max(0, Math.min(index, manifest.length - 1));
    const page = manifest[currentIndex];

    const status = byAttr("data-page-status");
    const select = byAttr("data-page-select");
    const prev = byAttr("data-prev-page");
    const next = byAttr("data-next-page");

    if (status) status.textContent = pageText(page);
    if (select) select.value = String(currentIndex);
    if (prev) prev.disabled = currentIndex === 0;
    if (next) next.disabled = currentIndex === manifest.length - 1;

    document.querySelectorAll("[data-page-index]").forEach((link) => {
      const isCurrent = Number(link.dataset.pageIndex) === currentIndex;
      if (isCurrent && link.tagName === "A") {
        link.setAttribute("aria-current", "page");
      } else if (link.tagName === "A") {
        link.removeAttribute("aria-current");
      }
    });

    if (updateHash) {
      history.replaceState(null, "", `#page-${String(page.page_index).padStart(3, "0")}`);
    }
    if (shouldScroll) {
      scrollToCurrent();
    }
  }

  function initialIndexFromHash() {
    const match = window.location.hash.match(/page-(\d+)/);
    if (!match) return 0;
    const pageNumber = Number(match[1]);
    const found = manifest.findIndex((page) => Number(page.page_index) === pageNumber);
    return found >= 0 ? found : 0;
  }

  document.addEventListener("DOMContentLoaded", async () => {
    try {
      manifest = await loadManifest();
      renderIndexSummary();
      if (byAttr("data-viewer")) {
        populateControls();
        renderPageStream();
        showPageInternal(initialIndexFromHash(), false, true);
        startObserver();
      }
      await initSearch();
    } catch (error) {
      const target = byAttr("data-summary") || byAttr("data-page-status");
      if (target) {
        target.textContent = `Manifest hatası: ${error.message}`;
      }
    }
  });
})();
