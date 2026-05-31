# Copyright Notes

Bu dosya hukuki görüş değildir; public repo sınırını ve hangi dosyaların neden paylaşılmadığını belgelemek için hazırlanmıştır.

## Public Olarak Tutulan Dosyalar

- `docs/assets/staj/pages/page-001.png` ... `page-028.png`
  - Staj defteri DOCX dosyasından üretilmiş sayfa görselleridir.
  - Bu repo için birincil yayın yüzeyidir.
- `docs/assets/staj/originals/EK-10_Siemens_Staj_Makale_Analizleri.pdf`
  - Staj defteri DOCX dosyasından üretilmiş PDF kopyasıdır.
- `docs/assets/staj/originals/EK-10_Siemens_Staj_Makale_Analizleri.docx`
  - Staj defterinin public yayın hedefi kapsamında eklenen DOCX kopyasıdır.
- `docs/transcript/**` ve `docs/data/search_index.json`
  - DOCX metin katmanından çıkarılmış ikincil transcript ve arama katmanıdır.
- `docs/kaynakca.html`
  - Bibliyografik kayıt ve yayın sınırı sayfasıdır.

## Local-Only Tutulacak Dosyalar

- `Chase - A history of research in service operations  What s the big idea.pdf`
- `Cross-training policies in field services.pdf`
  - Bu iki dosya akademik makale PDF'leridir.
  - Yerel analiz ve doğrulama için kullanılabilir; telif hakkı/yeniden dağıtım durumu doğrulanmadan public tracked file yapılmaz.
- `work/`, `_work/`
  - Extraction çıktıları, ham medya, render denemeleri, loglar ve local ara dosyalar içerir.
  - Public site çıktısı değildir.
- `raw/`, `raw_sources/`, `source_materials/`, `private_reference/`, `local_sources/`, `_local_sources/`
  - Yardımcı kaynakları yerelde tutmak için ayrılmış private klasörlerdir.
- Makale PDF'lerinden çıkarılmış figürler, tablolar, tam sayfa renderlar veya uzun doğrudan alıntılar
  - Public repo'ya eklenmemelidir.

## Akademik Makale Sınırı

Bu repo, iki akademik makaleyi şu şekilde kullanır:

- bibliyografik kayıt,
- DOI/yayıncı bağlantısı,
- staj defterinde zaten yer alan kısa kaynakça bilgisi,
- yerel doğrulama metadata'sı.

Bu repo, aşağıdakileri yapmaz:

- yayımlanmış makale PDF'lerini yeniden dağıtmak,
- makale figürlerini veya tablolarını kopya asset olarak sunmak,
- makalelerin yerine geçecek uzun özet veya yeniden yayın üretmek.

## Metadata Kaynakları

Yerel PDF metadata çıkarımında şu DOI bilgileri kullanılmıştır:

- Chase, R. B., & Apte, U. M. (2007): `10.1016/j.jom.2006.11.002`
- Colen, P. J., & Lambrecht, M. R. (2012): `10.1016/j.ijpe.2012.03.003`

Her iki PDF için extraction notlarında Elsevier telif notu adayları görülmüştür. Bu nedenle varsayılan public davranış, PDF dosyalarını repoya dahil etmemek ve yalnızca bibliyografik bağlantı vermektir.

## Son Kontrol Notu

Final push öncesinde `git status --short --ignored` ile kök dizindeki akademik makale PDF'lerinin ignored kaldığı doğrulanmalıdır.
