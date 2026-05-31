# Migration Audit

Denetim tarihi: 2026-06-01

Bu dosya, `D:\TOPLANDIK\IK\industrial-service-operations-analysis` klasöründeki mevcut repoyu staj defterine çok yakın bir GitHub yayınına dönüştürmek için hazırlanmış audit ve migration planıdır. Bu aşamada silme, taşıma, yeniden yazma, commit veya push yapılmadı.

## mevcut repo özeti

Repo şu anda staj defterinin birebir yayınlanmasına değil, daha önce hazırlanmış portföy odaklı bir anlatıya göre şekillenmiş durumda.

Mevcut takip edilen ana içerikler:

- `README.md`, `README.en.md`, `internship_summary.md`, `article1_analysis.md`, `article2_analysis.md`
- `docs/tr/` ve `docs/en/` altında proje özeti, makale notları, öğrenimler ve portföy metinleri
- `figures/` altında seçilmiş görseller
- `notebooks/field_service_toy_simulation.ipynb` ve `src/field_service_toy_simulation.py`
- `references/`, `REFERENCES.md`, `publication_notes.md`, `FINAL_REVIEW.md`, `PR_DRAFT.md`

Bu yapı, "staj defterini olduğu gibi göstermek" yerine "staj çalışmasından portföy projesi üretmek" hedefini taşıyor. Yeni hedef bunun tersine, DOCX dosyasının metin ve sayfa düzenini merkeze alan bir yayın olmalı.

Kaynak dosya denetimi:

- `EK-10_Siemens_Staj_Makale_Analizleri.docx` repo kökünde mevcut.
- `Chase - A history of research in service operations  What s the big idea.pdf` repo kökünde mevcut.
- `Cross-training policies in field services.pdf` repo kökünde mevcut.
- DOCX metadata bilgisi yaklaşık olarak 28 sayfa, 5409 kelime, 35 tablo ve 80 medya öğesi gösteriyor.
- DOCX içinde `.emf`, `.jpeg`, `.jpg`, `.png` ve `.svg` uzantılı medya öğeleri var.

Mevcut GitHub Pages benzeri hedef site dosyaları henüz yok:

- `docs/.nojekyll` yok.
- `docs/index.html` yok.
- `docs/staj-defteri.html` yok.
- `docs/transcript.html` yok.
- `docs/kaynakca.html` yok.
- `docs/data/page_manifest.json` yok.
- `docs/data/search_index.json` yok.
- `docs/assets/staj/pages/` yok.

Mevcut `.gitignore`, önceki güvenli-portföy yaklaşımına uygun olarak `*.docx`, `*.pdf`, `planning/`, `scripts/` ve `work/` gibi dosya ve klasörleri dışarıda bırakıyor. Bu yeni hedef için özellikle `scripts/`, `planning/` ve olası `docs/assets/staj/originals/` kararları yeniden ele alınmalı.

Yerelde kullanılabilir araçlar:

- LibreOffice `soffice` mevcut.
- `pandoc` mevcut.
- ImageMagick `magick` mevcut.
- Python ortamında `fitz` / PyMuPDF, `python-docx`, Pillow, BeautifulSoup ve lxml mevcut.

Bu nedenle internet gerektirmeyen, yerelde yeniden üretilebilir bir dönüşüm hattı teknik olarak mümkün görünüyor.

## korunacak dosyalar

Aşağıdaki dosyalar ve çıktılar korunmalı; bu aşamada silinmemeli veya üstüne yazılmamalı:

- `EK-10_Siemens_Staj_Makale_Analizleri.docx`: ana doğruluk kaynağı.
- İki PDF makale: yardımcı referans kaynağı olarak korunmalı, ancak kamuya açık dağıtım kararı ayrıca verilmeli.
- `work/extracted/` altındaki önceki çıkarım çıktıları: metin, görsel ve metadata incelemesi için değerli ara kanıt.
- `work/manifests/` altındaki manifestler: önceki görsel ve yayınlanabilirlik kararları için referans.
- `scripts/extract_docx_assets.py`, `scripts/extract_pdf_assets.py`, `scripts/optimize_images.py`, `scripts/build_markdown.py`: mevcut halleri yeni hedefe tam uymasa da extraction mantığı yeniden kullanılabilir.
- `planning/public_safe_inventory.md`, `planning/evidence_map.md`, `planning/repo_strategy.md`: yeni hedefle tam uyumlu değil, fakat risk geçmişini ve önceki karar mantığını belgelediği için korunmalı.
- Mevcut Markdown analizleri: nihai yayının ana omurgası olmayacak, fakat transcript sonrası açıklayıcı/ek kaynak olarak değerlendirilebilir.

## uyarlanacak dosyalar

Yeni hedef için aşağıdaki dosyalar doğrudan kullanılmak yerine uyarlanmalı:

- `README.md`: Portföy projesi girişinden, staj defteri yayınına açılan portal sayfasına dönüştürülmeli.
- `docs/tr/*` ve `docs/en/*`: Mevcut analiz dili korunabilir, fakat ana yayın akışı yerine ikincil/legacy içerik olarak konumlandırılmalı.
- `article1_analysis.md`, `article2_analysis.md`, `internship_summary.md`: DOCX tabanlı staj defteri yayınında asıl metin yerine açıklama, not veya arka plan içeriği olabilir.
- `publication_notes.md` ve `REFERENCES.md`: GitHub Pages tarafında `docs/kaynakca.html` ve ayrı bir yayın notu bölümüne dönüştürülebilir.
- `.gitignore`: `docs/` altında üretilecek statik site dosyalarını engellememeli; fakat `_work/`, geçici renderlar ve özel kaynakları korumalı.
- `scripts/`: Eski mutlak yollar yerine repo kökünü esas alan, yeniden üretilebilir bir pipeline haline getirilmeli.

Önerilen script dönüşümü:

- kaynak dosya doğrulama ve hash manifesti üretme
- DOCX'i yerelde PDF'e dönüştürme
- PDF sayfalarını PNG/WebP olarak render etme
- DOCX metninden transcript çıkarma
- sayfa manifesti üretme
- arama indexi üretme
- HTML site üretme
- link, görsel, manifest ve hassas dosya kontrolü yapma

## kaldırılacak / yerini yenisinin alacağı dosyalar

Bu başlık silme talimatı değildir. Aşağıdaki öğeler mevcut görev için nihai ana omurga olmaktan çıkacak; migration sırasında arşivlenmeleri, legacy olarak bırakılmaları veya yeni yapı tarafından gölgelenmeleri önerilir.

- Kök seviyedeki `article1_analysis.md`, `article2_analysis.md`, `internship_summary.md`: Staj defterinin birebir yayın akışının yerine geçmemeli.
- `docs/tr/` ve `docs/en/` altındaki makale notları: yeni `docs/staj-defteri.html` ve `docs/transcript.html` yapısının ana içeriği olmamalı.
- `figures/` altındaki seçilmiş portföy görselleri: sayfa renderlarından bağımsız yardımcı görsel olarak kalabilir; yeni defter sayfaları `docs/assets/staj/pages/` altında üretilmeli.
- `notebooks/` ve `src/` altındaki toy simulation: önceki portföy stratejisine ait; yeni hedefte zorunlu değil.
- `PR_DRAFT.md`, `FINAL_REVIEW.md`, mevcut `publication_notes.md`: yeni migration tamamlanınca güncel yayın notu ve QA raporlarıyla yer değiştirmeli.
- Eski extraction scriptleri: kök-local kaynaklarla çalışan yeni pipeline scriptleriyle değiştirilmelidir.

## önerilen hedef klasör yapısı

Hedef yapı, README merkezli özet repo değil; GitHub Pages üzerinden okunabilir bir staj defteri yayını olmalı.

```text
industrial-service-operations-analysis/
├─ AGENTS.md
├─ README.md
├─ .gitignore
├─ .codex/
├─ planning/
│  ├─ migration_audit.md
│  └─ ...
├─ scripts/
│  ├─ 00_check_sources.py
│  ├─ 10_convert_docx_to_pdf.ps1
│  ├─ 20_render_pages.py
│  ├─ 30_extract_transcript.py
│  ├─ 40_build_site.py
│  └─ 50_verify_site.py
├─ docs/
│  ├─ .nojekyll
│  ├─ index.html
│  ├─ staj-defteri.html
│  ├─ transcript.html
│  ├─ kaynakca.html
│  ├─ assets/
│  │  ├─ css/
│  │  │  └─ site.css
│  │  ├─ js/
│  │  │  └─ site.js
│  │  ├─ staj/
│  │  │  ├─ pages/
│  │  │  │  ├─ page-001.png
│  │  │  │  ├─ page-002.png
│  │  │  │  └─ ...
│  │  │  └─ originals/
│  │  │     └─ optional-onay-gerektirir
│  │  └─ refs/
│  └─ data/
│     ├─ page_manifest.json
│     └─ search_index.json
└─ _work/
   ├─ extracted/
   ├─ drafts/
   └─ logs/
```

Önerilen migration akışı:

1. Kaynak dosyaların varlığını, boyutunu ve hash değerlerini kaydet.
2. DOCX'i yerel LibreOffice veya Microsoft Word eşdeğeriyle PDF'e çevir; sayfa düzeni için PDF'i geçici doğruluk ara çıktısı kabul et.
3. PDF sayfalarını sabit DPI ile `docs/assets/staj/pages/page-001.png` biçiminde render et.
4. DOCX metninden temiz transcript çıkar; sayfa kırılımları kesin yakalanamıyorsa bunu manifestte not et.
5. `page_manifest.json` içinde sayfa numarası, görsel yolu, piksel boyutu, transcript anchor'ı ve kaynak hash bilgisini tut.
6. `search_index.json` içinde sayfa bazlı veya bölüm bazlı aranabilir metin üret.
7. `docs/index.html`, `docs/staj-defteri.html`, `docs/transcript.html`, `docs/kaynakca.html` dosyalarını statik ve bağımsız çalışacak şekilde üret.
8. QA scriptiyle tüm linkleri, görsel yollarını, manifest eşleşmelerini, dosya boyutlarını ve yanlışlıkla commit edilecek özel dosyaları kontrol et.

## riskler

- Staj defteri sayfalarında kişisel bilgiler, resmi formlar, imza alanları, kurum/üniversite bilgileri ve danışman/yönetici isimleri bulunabilir. Birebir yayın hedefi bu riski artırır.
- DOCX içindeki 80 medya öğesinin bir kısmı üçüncü taraf görsel, logo, ekran görüntüsü, makale figürü veya şablon öğesi olabilir. Kamuya açık kullanım hakkı tek tek değerlendirilmeli.
- Yardımcı PDF'ler telifli akademik makaleler olabilir. PDF'lerin kendisini repoya koymak ile sadece bibliyografik atıf yapmak farklı risk seviyeleridir.
- `.gitignore` şu anda tüm `*.pdf` ve `*.docx` dosyalarını engelliyor. Orijinallerin `docs/assets/staj/originals/` altında yayınlanması istenirse bu bilinçli bir istisna gerektirir.
- DOCX'ten doğrudan sayfa görüntüsü üretimi, kullanılan render aracına göre değişebilir. Word, LibreOffice ve Pandoc aynı sayfa düzenini birebir vermeyebilir.
- DOCX metadata 28 sayfa gösteriyor; üretilen PDF'in sayfa sayısı farklı çıkarsa layout doğruluğu ayrıca kontrol edilmeli.
- Console çıktılarında bazı Türkçe karakterler bozuk görünebiliyor. Bu muhtemelen PowerShell codepage görüntüleme sorunu olabilir, fakat site üretiminde UTF-8 doğrulaması yapılmalı.
- GitHub Pages'de yüksek çözünürlüklü PNG sayfaları repo boyutunu büyütebilir. Birebirlik ile dosya boyutu arasında karar gerekebilir.
- Mevcut repo geçmişi portföy projesi olarak ilerlediği için, yeni yayın yapısı eski dosyalarla yan yana kalırsa okuyucu açısından kafa karışıklığı doğabilir.

## açık sorular

1. Orijinal DOCX ve/veya bundan üretilen PDF, `docs/assets/staj/originals/` altında kamuya açık yayımlansın mı; yoksa sadece sayfa görüntüleri ve transcript mi yayımlansın?
2. Resmi form, imza alanı, öğrenci/kurum/yönetici bilgisi içeren sayfalar birebir mi kalmalı, kırpılmalı mı, bulanıklaştırılmalı mı, yoksa yayından çıkarılmalı mı?
3. Hedefte en önemli kriter hangisi: sayfa düzenine birebir sadakat mi, repo boyutunun küçük kalması mı, yoksa tarayıcıda hızlı okuma deneyimi mi?
4. Mevcut portföy odaklı Markdown dosyaları yeni yapıda `legacy`/`notes` olarak korunmalı mı, yoksa sonraki aşamada ana yayından tamamen ayrılmalı mı?
5. Siemens Energy ve üniversite adları kamuya açık yayında açık biçimde kalacak mı, yoksa daha nötr bir staj bağlamı dili mi kullanılacak?
