# Commit Plan

Bu planın amacı repoyu tek büyük commit yerine, gerçek ilerlemeyi anlatan okunabilir bir geçmişle hazırlamaktır. Ham çalışma alanı olan `_work/`, `__pycache__/` ve benzeri geçici çıktılar commit kapsamına alınmamalıdır.

## Mevcut durum notu

- `_work/` ignored kalmalı; ham DOCX/PDF çıktıları ve yedekler commitlenmemeli.
- `scripts/__pycache__/` ignored kalmalı.
- `article1_analysis.md`, `article2_analysis.md`, `internship_summary.md`, `publication_notes.md`, `references/bibliography.md` gibi eski kök/ara dosyalar daha önceki yapıdan kalmış görünüyor. Nihai minimal repo için gerekli değillerse ayrı bir temizlik kararına bırakılmalı; bu plandaki ana commit akışına otomatik eklenmemeliler.
- Önerilen ana stil: **Conventional Commits**. Türkçe ve akademik/portföy odaklı alternatifler aşağıda verildi.

## Commit mesajı stilleri

| Stil | Örnek kısa mesaj | Ne zaman iyi çalışır? |
|---|---|---|
| Conventional Commits | `docs: add field service cross-training analysis` | GitHub, PR ve otomatik changelog akışlarında temiz görünür. |
| Sade Türkçe | `Saha servisi analiz yazısını ekle` | Yerel/kişisel repo geçmişinde hızlı okunur. |
| Akademik/portföy odaklı | `Portfolio: document cross-training analysis for field service operations` | Projeyi portföy çıktısı gibi konumlandırmak istediğinde iyi çalışır. |

## Önerilen commit sırası

### 1. Repo iskeleti

**Kısa mesaj seçenekleri**

- Conventional: `chore: scaffold publishable internship repository`
- Sade Türkçe: `Yayınlanabilir repo iskeletini hazırla`
- Akademik/portföy: `Portfolio: establish curated internship analysis structure`

**Uzun açıklama**

Repo yapısının kamuya açık portföy sürümü olarak kurulmasını sağlar. `.gitignore` ile ham çalışma alanları, kaynak PDF/DOCX dosyaları ve geçici çıktılar dışarıda bırakılır. `metadata/repo-audit.md`, ilk denetim ve yapılandırma kararını belgelediği için iskelet commitine uygundur.

**Örnek PowerShell komutu**

```powershell
git -c safe.directory=D:/TOPLANDIK/GitHub/industrial-service-operations-analysis -C 'D:\TOPLANDIK\GitHub\industrial-service-operations-analysis' add .gitignore metadata/repo-audit.md
git -c safe.directory=D:/TOPLANDIK/GitHub/industrial-service-operations-analysis -C 'D:\TOPLANDIK\GitHub\industrial-service-operations-analysis' commit -m "chore: scaffold publishable internship repository" -m "Set up the public repository boundary for the internship analysis work. Keep raw sources and temporary extraction outputs out of version control while documenting the initial repository audit."
```

### 2. Extraction scripts

**Kısa mesaj seçenekleri**

- Conventional: `build: add local extraction workflow`
- Sade Türkçe: `Yerel çıkarım scriptini ekle`
- Akademik/portföy: `Portfolio: document reproducible extraction workflow`

**Uzun açıklama**

DOCX ve PDF kaynaklarından yerel metin/görsel çıkarımı için kullanılan scripti ve çıkarım özetini ekler. Ham çıkarım çıktıları `_work/` altında kaldığı için commitlenmez; yalnızca yöntemi ve özet raporu tutulur.

**Örnek PowerShell komutu**

```powershell
git -c safe.directory=D:/TOPLANDIK/GitHub/industrial-service-operations-analysis -C 'D:\TOPLANDIK\GitHub\industrial-service-operations-analysis' add scripts/extract_assets.py metadata/extraction-summary.md
git -c safe.directory=D:/TOPLANDIK/GitHub/industrial-service-operations-analysis -C 'D:\TOPLANDIK\GitHub\industrial-service-operations-analysis' commit -m "build: add local extraction workflow" -m "Add the extraction script used to derive local working text and image assets from the internship report and article PDFs. Keep raw extracted material ignored, and commit only the reproducible workflow plus extraction summary."
```

### 3. Section map

**Kısa mesaj seçenekleri**

- Conventional: `docs: map internship report into publishable sections`
- Sade Türkçe: `Staj defteri bölüm haritasını ekle`
- Akademik/portföy: `Portfolio: define editorial map for internship analysis`

**Uzun açıklama**

Ham staj defterinin hangi parçalarının public repo içinde kullanılacağını, hangi parçaların dışarıda kalacağını ve iki ana Markdown dosyasının sınırlarını açıklar. Bu commit, sonraki içerik commitlerinin editoryal gerekçesini görünür yapar.

**Örnek PowerShell komutu**

```powershell
git -c safe.directory=D:/TOPLANDIK/GitHub/industrial-service-operations-analysis -C 'D:\TOPLANDIK\GitHub\industrial-service-operations-analysis' add metadata/section-map.md metadata/section-map.yml
git -c safe.directory=D:/TOPLANDIK/GitHub/industrial-service-operations-analysis -C 'D:\TOPLANDIK\GitHub\industrial-service-operations-analysis' commit -m "docs: map internship report into publishable sections" -m "Document the editorial split between the two main internship analysis files and mark private, form-like, or copyright-sensitive material as out of scope for the public repository."
```

### 4. Main Markdown part 1

**Kısa mesaj seçenekleri**

- Conventional: `docs: add service operations analysis essay`
- Sade Türkçe: `Hizmet operasyonları yazısını ekle`
- Akademik/portföy: `Portfolio: add conceptual service operations analysis`

**Uzun açıklama**

Makale Ödevi 1 içeriğini kamuya açık, düzenlenmiş ve okunabilir bir Markdown yazısı olarak ekler. Bu commit kavramsal arka planı, hizmet operasyonları literatürüyle bağlantıyı ve staj defterindeki kişisel yorum katmanını taşır.

**Örnek PowerShell komutu**

```powershell
git -c safe.directory=D:/TOPLANDIK/GitHub/industrial-service-operations-analysis -C 'D:\TOPLANDIK\GitHub\industrial-service-operations-analysis' add docs/internship-part-1.md
git -c safe.directory=D:/TOPLANDIK/GitHub/industrial-service-operations-analysis -C 'D:\TOPLANDIK\GitHub\industrial-service-operations-analysis' commit -m "docs: add service operations analysis essay" -m "Add the first main public Markdown article, covering service operations, standardization, experience design, process thinking, and the cleaned editorial version of the first internship assignment."
```

### 5. Main Markdown part 2

**Kısa mesaj seçenekleri**

- Conventional: `docs: add field service cross-training analysis`
- Sade Türkçe: `Saha servisi çapraz eğitim analizini ekle`
- Akademik/portföy: `Portfolio: add technical field service operations analysis`

**Uzun açıklama**

Makale Ödevi 2 içeriğini repodaki teknik merkez olarak ekler. PM/emergency ayrımı, E-FSE/N-FSE yapısı, bütçe mantığı, availability, penalty score, direct/indirect effect ve emergency trap gibi karar mekanizmalarını açıklar.

**Örnek PowerShell komutu**

```powershell
git -c safe.directory=D:/TOPLANDIK/GitHub/industrial-service-operations-analysis -C 'D:\TOPLANDIK\GitHub\industrial-service-operations-analysis' add docs/internship-part-2.md
git -c safe.directory=D:/TOPLANDIK/GitHub/industrial-service-operations-analysis -C 'D:\TOPLANDIK\GitHub\industrial-service-operations-analysis' commit -m "docs: add field service cross-training analysis" -m "Add the second main Markdown article as the technical center of the repository, explaining cross-training, preventive maintenance, emergency work, performance metrics, and field service management implications."
```

### 6. Images

**Kısa mesaj seçenekleri**

- Conventional: `docs: add curated visual assets and image manifest`
- Sade Türkçe: `Seçilmiş görselleri ve manifesti ekle`
- Akademik/portföy: `Portfolio: add curated visuals for service operations case study`

**Uzun açıklama**

Public repo için seçilmiş veya yeniden çizilmiş görselleri ekler. `metadata/image-manifest.csv`, hangi ham görselin nasıl ele alındığını ve hangi Markdown dosyasında kullanıldığını açıklar. Küçük ikonlar, form şablonları ve telif riski taşıyan ham figürler commitlenmez.

**Örnek PowerShell komutu**

```powershell
git -c safe.directory=D:/TOPLANDIK/GitHub/industrial-service-operations-analysis -C 'D:\TOPLANDIK\GitHub\industrial-service-operations-analysis' add assets/images metadata/image-manifest.csv scripts/optimize_images.ps1
git -c safe.directory=D:/TOPLANDIK/GitHub/industrial-service-operations-analysis -C 'D:\TOPLANDIK\GitHub\industrial-service-operations-analysis' commit -m "docs: add curated visual assets and image manifest" -m "Add selected public visual assets for both main articles, include the image manifest, and keep raw or ambiguous extracted visuals out of the committed repository."
```

### 7. README

**Kısa mesaj seçenekleri**

- Conventional: `docs: add repository portal README`
- Sade Türkçe: `Repo giriş README dosyasını ekle`
- Akademik/portföy: `Portfolio: add public-facing repository overview`

**Uzun açıklama**

README dosyasını iki ana yazının önüne geçmeyen bir portal olarak ekler. Repo konusu, okuma sırası, içerik haritası, Mermaid yapı diyagramı ve yayın sınırları kısa biçimde sunulur. README varyant karşılaştırması da karar gerekçesi olarak metadata altında tutulur.

**Örnek PowerShell komutu**

```powershell
git -c safe.directory=D:/TOPLANDIK/GitHub/industrial-service-operations-analysis -C 'D:\TOPLANDIK\GitHub\industrial-service-operations-analysis' add README.md metadata/readme-comparison.md
git -c safe.directory=D:/TOPLANDIK/GitHub/industrial-service-operations-analysis -C 'D:\TOPLANDIK\GitHub\industrial-service-operations-analysis' commit -m "docs: add repository portal README" -m "Add a concise README that routes readers to the two main analysis files, explains the repository structure with Mermaid, and states the public sharing boundary without replacing the main articles."
```

### 8. QA scripts

**Kısa mesaj seçenekleri**

- Conventional: `test: add repository quality checks`
- Sade Türkçe: `Repo kalite kontrol scriptini ekle`
- Akademik/portföy: `Portfolio: add quality gate for public Markdown repository`

**Uzun açıklama**

`scripts/verify_repo.py` ile dosya varlığı, frontmatter, görsel linkleri, relative linkler ve boş TODO blokları kontrol edilir. `metadata/qa-report.md`, son çalıştırma sonucunu belgelediği için bu commite dahildir.

**Örnek PowerShell komutu**

```powershell
git -c safe.directory=D:/TOPLANDIK/GitHub/industrial-service-operations-analysis -C 'D:\TOPLANDIK\GitHub\industrial-service-operations-analysis' add scripts/verify_repo.py metadata/qa-report.md
git -c safe.directory=D:/TOPLANDIK/GitHub/industrial-service-operations-analysis -C 'D:\TOPLANDIK\GitHub\industrial-service-operations-analysis' commit -m "test: add repository quality checks" -m "Add a runnable QA script for the Markdown repository and commit the generated QA report so broken links, missing frontmatter, missing required files, and empty TODO placeholders are visible before publication."
```

### 9. Publication note / license

**Kısa mesaj seçenekleri**

- Conventional: `docs: add publication boundaries and license notice`
- Sade Türkçe: `Yayın notu ve lisans uyarısını ekle`
- Akademik/portföy: `Portfolio: document publication limits and rights notice`

**Uzun açıklama**

Kamuya açık paylaşım sınırlarını, kaynakların nasıl kullanıldığını ve şimdilik açık lisans seçilmediğini belgeleyen destek dosyalarını ekler. `docs/references.md` temiz bibliyografik künyeleri; `docs/publication-note.md` yayın yaklaşımını; `LICENSE.md` ise geçici hak saklıdır notunu taşır.

**Örnek PowerShell komutu**

```powershell
git -c safe.directory=D:/TOPLANDIK/GitHub/industrial-service-operations-analysis -C 'D:\TOPLANDIK\GitHub\industrial-service-operations-analysis' add docs/references.md docs/publication-note.md LICENSE.md
git -c safe.directory=D:/TOPLANDIK/GitHub/industrial-service-operations-analysis -C 'D:\TOPLANDIK\GitHub\industrial-service-operations-analysis' commit -m "docs: add publication boundaries and license notice" -m "Add reference, publication, and rights notices that clarify this repository is an editorial public version of an internship output, not a redistribution of raw internship files or copyrighted article PDFs."
```

## Commit öncesi önerilen kontrol

Her committen önce kısa bir diff kontrolü yapılmalı:

```powershell
git -c safe.directory=D:/TOPLANDIK/GitHub/industrial-service-operations-analysis -C 'D:\TOPLANDIK\GitHub\industrial-service-operations-analysis' status --short --ignored
git -c safe.directory=D:/TOPLANDIK/GitHub/industrial-service-operations-analysis -C 'D:\TOPLANDIK\GitHub\industrial-service-operations-analysis' diff --cached --stat
python D:\TOPLANDIK\GitHub\industrial-service-operations-analysis\scripts\verify_repo.py
```

## Not: eski kök dosyalar

Şu dosyalar eski repo denemelerinden veya alternatif yapıdan kalmış görünüyor:

- `article1_analysis.md`
- `article2_analysis.md`
- `internship_summary.md`
- `publication_notes.md`
- `references/bibliography.md`
- `figures/article2/*.webp`
- `figures/internship/*.webp`

Nihai minimal repo hedefi `README.md`, `docs/`, `assets/`, `metadata/`, `scripts/`, `.gitignore` ve `LICENSE.md` etrafında toparlanacaksa bu eski dosyalar ayrı bir temizlik commitinde ele alınmalı. Önerilen mesaj:

```powershell
git -c safe.directory=D:/TOPLANDIK/GitHub/industrial-service-operations-analysis -C 'D:\TOPLANDIK\GitHub\industrial-service-operations-analysis' rm article1_analysis.md article2_analysis.md internship_summary.md publication_notes.md references/bibliography.md
git -c safe.directory=D:/TOPLANDIK/GitHub/industrial-service-operations-analysis -C 'D:\TOPLANDIK\GitHub\industrial-service-operations-analysis' commit -m "chore: remove superseded root-level drafts" -m "Remove earlier root-level draft files after the repository was consolidated around README, docs, assets, metadata, and scripts."
```

Bu temizlik commitini ancak dosyaların artık gerekli olmadığı kesinleşirse yapmak doğru olur.
