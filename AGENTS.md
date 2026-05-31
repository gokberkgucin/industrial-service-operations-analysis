# AGENTS.md

Bu repo bir belge çoğaltma ve yayınlama reposudur; yeniden yorumlama, bloglaştırma veya akademik özet üretme reposu değildir.

## Kaynak Hiyerarşisi

- Canonical source: `EK-10_Siemens_Staj_Makale_Analizleri.docx`.
- Sayfa sırası, görsel yerleşimi ve metin akışı DOCX'e göre korunur.
- Yardımcı PDF'ler yalnızca referans ve doğrulama için kullanılır; telif durumu netleşmeden public tracked file yapılmaz.

## Birincil Çıktı

- Primary output: GitHub Pages üzerinde çalışan sayfa görüntüleyicisi.
- Sayfa görselleri birincildir; transcript ve arama indeksi ikincil erişim katmanıdır.
- Transcript, sayfa görüntülerinin yerine geçmez ve anlamı yeniden yazmaz.

## Metin ve Yol Kuralları

- Türkçe karakterler, özel adlar, başlıklar ve metin sırası kaynak belgedeki biçime sadık kalacak şekilde korunur.
- Metin düzeltmesi yalnızca teknik encoding, kırık satır veya açık OCR/çıkarım hatası için yapılır.
- Repo içindeki bağlantılar relative path ile yazılır.
- Public site çıktıları `docs/` altında tutulur.
- Geçici işler ve ara çıktılar `_work/` veya `work/` altında tutulur ve public içerik gibi ele alınmaz.

## Güvenlik ve Telif

- Yıkıcı değişiklikten önce branch, worktree ve `git status` kontrol edilir.
- Dosya silme, taşıma veya toplu overwrite işlemleri ayrı onay gerektirir.
- Makale PDF'leri, üçüncü taraf figürleri ve telif belirsiz görseller varsayılan olarak public repo'ya eklenmez.
- Kişisel bilgiler, imza alanları, resmi form alanları ve kurumsal detaylar yayın sınırı açısından ayrıca işaretlenir.

## Faz Sonu Zorunlulukları

Her faz sonunda:

- `git status --short` kontrol edilir.
- Üretilen dosyalar listelenir.
- Link, görsel ve manifest doğrulaması ilgili fazın kapsamına göre yapılır.
- Kısa bir summary yazılır.
- Kritik risk veya belirsizlik varsa ilerlemeden önce raporlanır.

## Yapılmayacaklar

- DOCX metni serbestçe yeniden yazılmaz.
- Staj defteri makale özetine veya portföy anlatısına indirgenmez.
- İnternete bağımlı bir üretim akışı varsayılmaz.
- Telif durumu belirsiz kaynaklar public tracked dosya yapılmaz.
