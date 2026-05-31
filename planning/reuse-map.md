# Reuse Map

Bu dosya, mevcut portföy odaklı repodan staj defteri odaklı GitHub Pages yayınına geçerken hangi içeriklerin korunduğunu, uyarlandığını veya public yüzeyden kaldırıldığını belgeler.

## Sınıflandırma Özeti

| Dosya / klasör | Karar | Gerekçe |
|---|---|---|
| `EK-10_Siemens_Staj_Makale_Analizleri.docx` | Korundu, public source olarak değil | Canonical source. Orijinal DOCX'e dokunulmadı; public surface'e doğrudan link verilmedi. |
| `docs/assets/staj/pages/page-*.png` | Korundu | GitHub Pages görüntüleyicisinin birincil sayfa katmanı. |
| `docs/assets/staj/originals/EK-10_Siemens_Staj_Makale_Analizleri.pdf` | Korundu, kontrollü public artifact | DOCX'ten üretilmiş staj defteri PDF'i. Makale PDF'i değildir; yine de yayın sınırı QA'da kontrol edilmeli. |
| `docs/data/page_manifest.json` | Korundu | Sayfa görüntüleyicisi için zorunlu manifest. |
| `scripts/export_docx_to_pdf.ps1` | Korundu | Yeni reproducible build hattının PDF export adımı. |
| `scripts/export_pdf_pages.py` | Korundu | Yeni reproducible build hattının sayfa render adımı. |
| `scripts/extract_docx_media.py` | Korundu | DOCX medya ve transcript ham girdisi çıkarımı için kullanılıyor. |
| `scripts/build_manifest.py` | Korundu | `page_manifest.json` üretimi için kullanılıyor. |
| `README.md` | Uyarlandı | Eski portföy README'si yeni yayın hedefiyle çelişiyordu; artık Pages portalı ve kaynak ilkesi olarak çalışıyor. |
| `CITATION.cff` | Uyarlandı | Eski dosya projeyi software/portfolio olarak tanımlıyordu; belge yayını/pipeline bağlamına çekildi. |
| `.gitignore` | Uyarlandı | `planning/` ve yeni `scripts/` public hale getirildi; `_work/`, kök DOCX ve üçüncü taraf PDF'ler private kaldı. |
| `REFERENCES.md`, `publication_notes.md` | Public kökten kaldırıldı, legacy olarak saklandı | İçerik yeni `docs/kaynakca.html` içinde sadeleştirilerek kullanıldı. |
| `references/bibliography.md`, `references/citations.bib` | Legacy olarak saklandı | Bibliyografik bilgi yeni HTML kaynakça sayfasına taşındı. |
| `article1_analysis.md`, `article2_analysis.md`, `internship_summary.md` | Public kökten kaldırıldı, legacy olarak saklandı | Bunlar önceki portföy stratejisine aitti; yeni ana çıktı staj defteri görüntüleyicisi. |
| `docs/tr/*`, `docs/en/*`, `docs/figures/*.mmd` | Public Pages yolundan kaldırıldı, legacy olarak saklandı | Eski analiz dokümantasyonu yeni birebir yayın hedefini karıştırıyordu. |
| `figures/*` | Public Pages yolundan kaldırıldı, legacy olarak saklandı | Eski açıklayıcı portföy görselleri; yeni ana görsel katman sayfa renderlarıdır. |
| `notebooks/`, `src/` toy simulation | Legacy olarak saklandı | Önceki portföy stratejisinin demo modeli; yeni yayın hedefinde zorunlu değil. |
| Eski extraction scriptleri | `_work/legacy/scripts/` altına taşındı | Eski mutlak yol ve portföy akışı içeriyordu; yeni public script setiyle karışmaması için public script klasöründen çıkarıldı. |

## Korunan Eski İçerik

Eski analiz metinleri, simülasyon ve görseller tamamen silinmedi. Geriye dönük izlenebilirlik için `planning/legacy/` altında tutuldu. Bu alan, GitHub Pages sitesinin ana okuma yolu değildir.

## Uygulanan Yeni Public Yapı

```text
docs/
  .nojekyll
  index.html
  staj-defteri.html
  transcript.html
  kaynakca.html
  assets/
    css/site.css
    js/site.js
    refs/README.md
    staj/pages/page-001.png ...
    staj/originals/EK-10_Siemens_Staj_Makale_Analizleri.pdf
  data/page_manifest.json
scripts/
  export_docx_to_pdf.ps1
  export_pdf_pages.py
  extract_docx_media.py
  build_manifest.py
planning/
  migration_audit.md
  roadmap.md
  reuse-map.md
  legacy/
```

## Kaldırma Notu

Bu fazda içerik körlemesine silinmedi. "Kaldırıldı" ifadesi, dosyanın public okuma yüzeyinden çıkarıldığı ve legacy/planning alanına taşındığı anlamına gelir.
