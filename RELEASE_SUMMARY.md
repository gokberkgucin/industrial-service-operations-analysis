# Release Summary

Bu özet, push öncesi son kontrol için hazırlanmıştır.

## Eklenenler

- Staj defterini GitHub Pages üzerinde sayfa sadakatiyle gösterecek statik site kabuğu eklendi.
- 28 sayfalık sayfa görseli, sayfa manifesti ve arama/transcript katmanı üretildi.
- Staj defterinin public yayın yüzeyinde kullanılacak PDF ve DOCX çıktıları `docs/assets/staj/originals/` altında konumlandırıldı.
- Kaynakça sayfası, telif sınırı notları, build scriptleri ve repo çalışma kuralları eklendi.
- Eski portföy odaklı içerikler silinmek yerine `planning/legacy/` altında arşivlendi.

## Kalan Riskler

- Staj defteri görselleri ve indirilebilir DOCX/PDF, belgenin neredeyse birebir yayını olduğu için push öncesi son insan kontrolü gerektirir.
- Sayfa görselleri içinde üçüncü taraf görsel, logo veya makale içeriği bulunma ihtimali tamamen ortadan kaldırılmış değildir.
- Akademik makale PDF'leri public tracked dosya yapılmadı; kökteki yerel kopyalar `.gitignore` ile dışarıda tutuluyor.
- Transcript katmanı yardımcıdır; doğrulukta öncelik sayfa görsellerindedir.

## Public Telif Sınırı

Public tutulması hedeflenenler:

- `docs/` altındaki GitHub Pages site dosyaları
- staj defteri sayfa görselleri
- staj defteri PDF/DOCX yayın kopyası
- transcript, arama indeksi, kaynakça ve telif notları

Local-only tutulması gerekenler:

- üçüncü taraf akademik makale PDF'leri
- `_work/`, `work/`, `_local_sources/` ve benzeri üretim/ara çıktı klasörleri
- telif doğrulaması yapılmamış ham yardımcı kaynaklar

## Push Öncesi Kontrol

- `scripts/verify_repo.py` son çalıştırmada PASS verdi.
- Kırık relative link, eksik manifest sayfası veya eksik transcript sayfası raporlanmadı.
- Push yapılmadan önce GitHub Pages URL yer tutucusu gerçek yayın adresiyle kontrol edilmelidir.
