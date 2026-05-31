# Başlık önerisi

Public-safe internship portfolio content for industrial service operations analysis

## Özet

Bu PR, Siemens Energy stajı sırasında yapılan iki akademik makale analizini ham staj defteri formatından çıkarıp kamuya açık, portföy odaklı ve teknik olarak temkinli bir repo yapısına dönüştürür.

Ana odak, hizmet operasyonları literatürü ile saha servis işgücü tasarımı arasındaki bağlantıyı göstermektir. İçerik; analiz metinleri, yayın notları, bibliyografik kaynaklar, küçük bir öğretici simülasyon ve kamuya güvenli yeniden çizilmiş görsellerden oluşur.

## Eklenen dosyalar

- `README.md`: Türkçe ana repo açıklaması, içerik haritası ve okuma sırası.
- `internship_summary.md`: Staj bağlamı ve çalışmanın portföy projesine dönüştürülme gerekçesi.
- `article1_analysis.md`: Hizmet operasyonları tarihçesi makalesi için kamuya açık kavramsal analiz.
- `article2_analysis.md`: Saha servis çapraz eğitim politikaları için teknik analiz.
- `publication_notes.md`: Kamuya açık paylaşım sınırları, gizlilik ve telif notları.
- `references/bibliography.md`: İncelenen iki akademik çalışmanın bibliyografik künyeleri.
- `references/citations.bib`: BibTeX atıf kayıtları.
- `CITATION.cff`: Repo için atıf metadata dosyası.
- `.github/PULL_REQUEST_TEMPLATE.md`: Gelecek değişiklikler için kontrol odaklı PR şablonu.
- `figures/internship/*.webp` ve `figures/article2/*.webp`: Telifli figürlerden kopyalanmayan, repo için özgün üretilmiş açıklayıcı görseller.

## Telif/gizlilik notu

Bu PR ham DOCX staj belgesini, orijinal PDF makaleleri, üçüncü taraf görselleri veya kurum içi detay izlenimi verebilecek içeriği repoya eklemez.

Görseller kamuya açık kullanım için yeniden çizilmiş veya sentetik olarak üretilmiştir; makale figürlerinin birebir yeniden dağıtımı değildir. Makalelerden uzun doğrudan alıntı yapılmamış, içerik ağırlıklı olarak kişisel analiz ve paraphrase olarak yazılmıştır.

## Neden bu repo yapısı seçildi

Repo yapısı, çalışmayı “staj defteri yükleme” çizgisinden çıkarıp okunabilir bir portföy projesine dönüştürmek için seçildi:

- Kök dosyalar hızlı değerlendirme için kısa ve taranabilir tutuldu.
- Makale analizleri ayrı dosyalara bölünerek teknik ayrıntı README’den ayrıldı.
- `publication_notes.md` ve `references/` klasörü, kamuya açık paylaşım sınırlarını görünür kıldı.
- `work/` ve ham kaynaklar `.gitignore` altında tutuldu; işlenmiş özel çalışma çıktıları repo dışı bırakıldı.
- Görseller, telif riskini azaltmak için özgün/sentetik açıklayıcı çıktılar olarak üretildi.

## Gözden geçirme kontrol listesi

- [ ] Markdown linkleri ve görsel referansları çalışıyor.
- [ ] Ham DOCX/PDF kaynaklar stage alanında yok.
- [ ] `.gitignore`, `work/`, ham kaynaklar ve private referans klasörlerini dışarıda bırakıyor.
- [ ] Kurum içi veri, kişi bilgisi veya ham staj defteri dili kamuya taşınmadı.
- [ ] Görsellerin açıklayıcı/sentetik olduğu ve makale sonuçlarını yeniden üretmediği net.
- [ ] Bibliyografik künyeler ve DOI bilgileri kontrol edildi.
- [ ] README, makale dosyaları ve yayın notları arasında gereksiz tekrar yok.
