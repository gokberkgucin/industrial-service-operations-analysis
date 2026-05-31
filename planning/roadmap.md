# Roadmap

Bu yol haritası, mevcut portföy odaklı repoyu staj defterinin sayfa sadakati yüksek GitHub Pages yayınına dönüştürmek için kullanılacaktır. Ana doğruluk kaynağı `EK-10_Siemens_Staj_Makale_Analizleri.docx` dosyası ve onun sayfa sırasıdır.

## README yayın stratejisi

README, içeriğin kendisi değil yayın portalı olacak: staj defterinin hangi kaynak dosyadan üretildiğini, GitHub Pages sayfa görüntüleyicisine nasıl gidileceğini, transcript ve kaynakça sayfalarının ikincil erişim katmanı olduğunu, ayrıca telif/gizlilik sınırlarının nasıl ele alındığını kısa ve net biçimde anlatacak. README kökte kalacak; asıl okuma deneyimi `docs/staj-defteri.html` üzerinden ilerleyecek.

## Fazlar

### 1. audit

- Repo ağacı, mevcut içerik ve kaynak dosyalar denetlenir.
- Mevcut portföy dosyaları ile hedef staj-defteri yayını arasındaki fark belgelenir.
- Çıktı: `planning/migration_audit.md`.

### 2. asset extraction

- DOCX metni, medya öğeleri ve metadata yerelde çıkarılır.
- DOCX'ten PDF üretim yöntemi netleştirilir.
- PDF sayfa sayısı, DOCX metadata sayfa sayısıyla karşılaştırılır.
- Çıktı: `_work/` veya `work/` altında ham/ara çıkarımlar.

### 3. site skeleton

- `docs/` altında GitHub Pages iskeleti oluşturulur.
- `index.html`, `staj-defteri.html`, `transcript.html`, `kaynakca.html`, CSS/JS ve data klasörleri hazırlanır.
- Çıktı: boş olmayan ama henüz final içerikle dolmamış statik site omurgası.

### 4. content population

- Staj defteri sayfaları `docs/assets/staj/pages/` altında sabit isimlerle yayıma hazırlanır.
- Sayfa manifesti oluşturulur.
- Görsel kalite, dosya boyutu ve sayfa sırası kontrol edilir.
- Çıktı: `page-001.png` veya seçilen nihai formatta sayfa dosyaları.

### 5. transcript/search

- DOCX metninden transcript çıkarılır.
- Transcript sayfa görüntülerine ikincil erişim katmanı olarak bağlanır.
- Arama indeksi üretilir.
- Çıktı: `docs/transcript.html`, `docs/data/search_index.json`.

### 6. legal publication boundary

- Telif belirsiz PDF'ler, üçüncü taraf görseller ve kişisel/kurumsal bilgiler değerlendirilir.
- Public tracked dosya yapılacak ve yapılmayacak içerikler netleştirilir.
- Çıktı: yayın notu, kaynakça ve risk notları.

### 7. QA

- Relative linkler, görsel yolları, manifest eşleşmeleri, UTF-8 karakterler ve GitHub Pages çalışabilirliği doğrulanır.
- Ham DOCX/PDF dosyalarının yanlışlıkla stage edilmediği kontrol edilir.
- Çıktı: kısa QA raporu ve düzeltme listesi.

### 8. commit/publish

- Temiz commit planı uygulanır.
- Public repo sınırları son kez kontrol edilir.
- Branch push edilir ve gerekiyorsa PR açılır.
- Çıktı: yayıma hazır GitHub Pages yapısı.

## Faz Sonu Kontrolü

Her fazın sonunda şu üç çıktı zorunludur:

- verification sonucu
- değişen/oluşan dosya listesi
- kısa özet ve açık riskler
