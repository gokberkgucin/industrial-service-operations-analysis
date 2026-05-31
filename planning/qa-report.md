# QA Report

Tarih: 2026-06-01T02:29:25

Sonuç: PASS

## Kontroller

- **PASS** `manifest sequence`: 28 manifest kaydı sıralı.
- **PASS** `asset sequence`: 28 PNG sayfa asset'i manifestle eşleşiyor.
- **PASS** `manifest required fields`: Tüm manifest kayıtlarında zorunlu alanlar var.
- **PASS** `manifest images`: Manifestteki tüm görsel yolları mevcut.
- **PASS** `relative html links`: 32 HTML dosyasında kırık relative link yok.
- **PASS** `project-site subpath`: Root-absolute link/src bulunmadı.
- **PASS** `local absolute paths`: HTML içinde yerel absolute path yok.
- **PASS** `old css/js refs`: HTML dosyaları main.css ve viewer.js yapısıyla uyumlu.
- **PASS** `download artifacts`: PDF (1625128 bytes) ve DOCX (2384396 bytes) mevcut.
- **PASS** `public pdf boundary`: Public assets içinde yalnızca staj defteri PDF'i var.
- **PASS** `transcript count`: 28 transcript sayfası manifestle eşleşiyor.
- **PASS** `manifest transcript paths`: Manifestteki tüm transcript path'leri mevcut.
- **PASS** `transcript backlinks`: Transcript sayfaları ilgili görsel sayfaya geri bağlı.
- **PASS** `search index`: 28 search kaydı gerekli alanlarla mevcut.
- **PASS** `utf-8 replacement chars`: Docs içeriğinde U+FFFD bulunmadı.
- **PASS** `external cdn`: Dış CDN bağımlılığı bulunmadı.
- **PASS** `gitignored private sources`: Kök kaynaklar ve local-only klasörler ignored durumda.

## Kalan Bilinen Kusurlar

- Kritik doğrulama hatası yok.
