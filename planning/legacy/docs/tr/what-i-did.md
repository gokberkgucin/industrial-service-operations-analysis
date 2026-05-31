# Ne Yaptım?

Bu dosya, çalışmanın kamuya açık portföy sürümünde benim katkımı netleştirir. Buradaki anlatı ham belge paylaşmaz; akademik okuma ve analiz işini yeniden düzenlenmiş bir proje çıktısına dönüştürür.

## Görevin Tanımı

Çalışmanın başlangıç noktası, hizmet operasyonları ve saha servis çapraz eğitim politikaları üzerine iki akademik makaleyi okuyup anlamak, ardından bu makalelerden çıkarılan fikirleri yorum ve eleştirilerle yazıya dökmekti.

Kamuya açık proje sürümünde bu görev şu biçime dönüştürüldü: iki akademik metinden hareketle, saha servis operasyonlarında işgücü esnekliği ve önleyici bakım kararlarını anlatan anonim, kaynaklı ve teknik bir portföy projesi oluşturmak.

## Çalışma Şeklim

Önce makalelerdeki ana kavramları ayırdım: hizmet operasyonları tarihçesi, önleyici bakım, acil bakım, çapraz eğitimli teknisyen, PM odaklı teknisyen, yanıt süresi, kullanılabilirlik ve ceza puanı.

Sonra bu kavramları ham çalışma notu dilinden çıkarıp profesyonel bir dokümantasyon yapısına taşıdım. Özellikle kurum adı, kişi adı, resmi belge formatı, telifli PDF içeriği ve polemik örnekleri kamuya açık sürümden ayırdım.

Son aşamada, ikinci makaledeki saha servis karar problemini küçük bir simülasyon fikrine bağladım. Bu simülasyon gerçek organizasyon verisini temsil etmez; karar mantığını görünür kılmak için tasarlanmış öğretici bir modeldir.

## Kullandığım Düşünme Biçimi

Çalışmada yalnızca "makale ne diyor?" sorusunu değil, "bu fikir bir saha servis yöneticisinin kararına nasıl dönüşür?" sorusunu takip ettim.

Bu yüzden kavramları üç düzeyde ele aldım:

- Kavramsal düzey: Hizmet operasyonları neden ayrı bir yönetim alanıdır?
- Model düzeyi: İşgücü karması, bakım türleri ve performans ölçütleri nasıl ilişkilidir?
- Uygulama düzeyi: Bu model gerçek bir organizasyonda hangi varsayımlar kontrol edilmeden kullanılamaz?

Bu yaklaşım, makaleyi sadece özetlemeyi değil; analitik bir karar çerçevesine dönüştürmeyi hedefledi.

## Ürettiğim Çıktıların Niteliği

Bu repo için üretilen çıktıların ortak özelliği, kamuya açık ve yeniden kullanılabilir olmalarıdır.

- README, projeyi ham belge paylaşımı değil portföy projesi olarak konumlandırır.
- Makale 1 notu, hizmet operasyonları tarihçesini kısa ve profesyonel bir teknik not haline getirir.
- Makale 2 notu, saha servis çapraz eğitim kararını problem, varsayım, metrik, sonuç ve eleştirel katkı başlıklarıyla açıklar.
- Python kodu, gerçek veri kullanmadan saha servis kapasite mantığını deneysel olarak gösterecek bir demo simülasyon sağlar.
- Kaynakça, iki akademik makaleyi bibliyografik olarak gösterir; telifli PDF'leri repoya dahil etmez.

## Neyi Özellikle Yapmadım

Ham çalışma belgelerini GitHub'a koymadım. Çünkü bu format kişi bilgileri, resmi alanlar ve kurum bağlamı içerebilir.

Akademik PDF dosyalarını veya makale tablolarını repoya eklemedim. Bunun yerine kaynakları `REFERENCES.md` içinde bibliyografik olarak belirttim.

Makalelerdeki sonuçları belirli bir organizasyon için doğrudan geçerliymiş gibi sunmadım. Modelin bağlama duyarlı olduğunu ve yerel veriyle yeniden değerlendirilmesi gerektiğini özellikle korudum.

Kişisel veya polemik örnekleri profesyonel portföy anlatısına taşımadım. Bunların yerine, arkasındaki yönetimsel fikirleri daha ölçülü kavramlara dönüştürdüm.

## Bu İş Neden Teknik ve Analitik Değer Taşıyor?

Bu çalışma teknik değer taşır çünkü bir akademik okuma görevini ölçülebilir kavramlara ve karar değişkenlerine ayırır: iş yükü, bakım periyodu, teknisyen yetkinliği, yanıt süresi, kullanılabilirlik ve backlog.

Analitik değer taşır çünkü "çapraz eğitim iyi midir?" gibi genel bir soruyu, "hangi koşulda, hangi iş yükünde, hangi bakım yapısında, hangi metrik açısından daha iyi?" sorusuna dönüştürür.

Portföy değeri ise burada ortaya çıkar: çalışma yalnızca okuduğumu göstermekle kalmaz; okuduğum şeyi güvenli, anlaşılır, modellenebilir ve tekrar çalıştırılabilir bir teknik proje yapısına çevirdiğimi gösterir.
