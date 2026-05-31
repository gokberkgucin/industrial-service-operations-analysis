# Public Safe Inventory

## Kapsam ve yöntem

Bu analiz yalnızca şu üç yerel dosyaya dayanır:

- `EK-10_Siemens_Staj_Makale_Analizleri.docx`
- `Cross-training policies in field services.pdf`
- `Chase - A history of research in service operations  What s the big idea.pdf`

İnternete çıkılmadı. Dosyalardaki metinlere dayanmayan iddialar eklenmedi. PDF makaleler telifli akademik yayın niteliğinde değerlendirildiği için kamuya açık sürümde PDF dosyalarının kendisi, uzun özetleri, tablo/grafik kopyaları veya uzun alıntıları kullanılmamalıdır.

## Bu staj çalışmasında gerçekten ne yaptın?

Kanıta göre staj çalışmasının ana işi, iki akademik makaleyi okuyup anlamak, bunlardan anladıklarını eleştiri ve yorumlarla yazıya dökmekti. DOCX dosyasında bu görevin Endüstriyel Uygulamalar Bölümü / saha servisi bağlamında verildiği, her makale için ayrı değerlendirme/mülakat beklendiği ve iki makalenin adının belirtildiği görülüyor.

Çalışma basit bir makale özeti veya çeviri olarak konumlandırılmamış. DOCX içinde açıkça ödevlerin orijinal makalelerin özeti ya da çevirisi olmadığı, makalelerden anlaşılanların kişisel yorumlar, eleştiriler, ek araştırma ve hatırlanan örneklerle genişletildiği yazıyor. Bu, GitHub anlatısı için önemli: katkı, "iki makalenin kopyalanması" değil, iki akademik metni operasyon yönetimi bakışıyla yorumlayıp bir öğrenme ve analiz dosyasına dönüştürmek.

Birinci makale için yapılan çalışma, Chase ve Apte'nin hizmet operasyonları tarihçesi makalesi etrafında bir deneme üretmek. DOCX'te hizmet sektörünün yükselişi, bilimsel yönetimin hizmetlere uygulanması, McDonald's ve Disney gibi örnekler, hizmet deneyimi, süreç adaleti, ifade özgürlüğü ve kişisel operasyon yönetimi deneyimi gibi başlıklar işlenmiş. Bu bölümde akademik makale ile kişisel gözlem ve genel yorumlar iç içe geçmiş.

İkinci makale için yapılan çalışma, Colen ve Lambrecht'in saha servisinde çapraz eğitim politikaları makalesini teknik düzeyde anlamlandırmak. DOCX'te PM/acil bakım ayrımı, E-FSE ve N-FSE işgücü rolleri, maliyet oranı, sabit bütçe mantığı, cevap süresi, kullanılabilirlik, ceza puanı, bakım periyodu, makine güvenilirliği, sözleşme kapsamı, doğrudan/dolaylı etki ve "emergency trap" kavramları açıklanmış. Ayrıca modelin ihmal ettiği insani/organizasyonel etkiler hakkında yorumlar eklenmiş.

## GitHub için anlatılmaya değer olanlar

- Akademik makale okuma ve teknik kavramları öğrenme süreci: DOCX, ilk makalenin endüstri mühendisliği kavramlarını öğrenmeyi gerektirdiğini ve ikinci makalenin matematik içerdiğini gösteriyor.
- Hizmet operasyonları tarihçesini portföy diline dönüştürme: kamuya açık sürümde "service operations literature review notes" olarak anlatılabilir.
- Saha servis kapasite kararları: PM/acil bakım, çapraz eğitimli ve uzman teknisyen ayrımı, cevap süresi ve hizmet kalitesi gibi kavramlar portföy için güçlüdür.
- Simülasyon mantığını sadeleştirme: ikinci makaledeki model kamuya açık repoda telifli tabloyu kopyalamadan, oyuncak bir simülasyon ve açıklayıcı diyagramlarla yeniden kurulabilir.
- Eleştirel okuma: model varsayımlarını sorgulama, insani etkileri ve sözleşme türlerini tartışma GitHub'da "analysis notes" olarak değerlendirilebilir.
- Kamuya açık öğrenme çıktısı: "Bir staj görevi kapsamında iki akademik makaleyi operasyon yönetimi perspektifiyle analiz ettim" anlatısı güçlü ve güvenlidir.

## GitHub'a ham haliyle konmaması gerekenler

- Kişi adları ve tanımlayıcı bilgiler: DOCX'te öğrenci/staj defteri alanları, iş yeri yetkilisi alanları, "Yüksel Bey" ve "Gökberk" gibi kişisel adlar geçiyor. Bunlar anonimleştirilmeli.
- Kurum içi veya kurumla ilişki ima eden ayrıntılar: Siemens Enerji adı, bölüm adı, saha servisi müdürü, iş yeri imza/kaşe alanları ve "S.E.'de bu oranlar nedir?" gibi ifadeler ham haliyle paylaşılmamalı.
- Telifli akademik makaleler: iki PDF dosyası, Elsevier/Wiley kaynaklı akademik yayın metni gibi görünüyor. PDF'ler repoya konmamalı; sadece bibliyografik referans ve kısa, özgün anlatım kullanılmalı.
- Uzun alıntılar ve makale tabloları: DOCX'te bazı doğrudan alıntılar ve makale denklemlerine/tablesel sonuçlarına dayalı açıklamalar var. Bunlar yeniden yazılmalı, telifli tablo/grafikler kopyalanmamalı.
- Aşırı kişisel/polemik bölümler: Çin, ülke üretkenliği, ifade özgürlüğü, Nusret, devlet başkanı/ünlü örnekleri gibi bölümler portföyde odağı dağıtabilir ve gereksiz risk yaratabilir.
- Önceki iş deneyimi ayrıntıları: prefabrik yapı fabrikası, çalışan tepkileri, fire azalması, üretim hızının artması gibi iddialar doğrulanabilir kanıt ve anonimleştirme olmadan ham halde yayımlanmamalı.
- Resmi staj defteri formatı: üniversite/staj komisyonu/iş yeri yetkilisi imza alanları ve iş yaprağı tabloları GitHub içeriği değil; bunlar çıkarılmalı.

## Makale 1: Hizmet operasyonları tarihçesi

### Ana tema

Makale 1, hizmet operasyonları araştırmasının tarihsel gelişimini ve "büyük fikirler" üzerinden alanın nasıl şekillendiğini ele alıyor. PDF'de hizmet sektörünün ekonomideki ağırlığı, bilimsel yönetimin hizmetlere uyarlanması, Disney, McDonald's, hizmet kalitesi, deneyim ekonomisi, bilgi yoğun hizmetler ve gelecek araştırma alanları gibi temalar yer alıyor.

### Benim katkım

DOCX'e göre katkı, makaleyi birebir özetlemek değil; makaledeki tarihsel çerçeveyi kişisel yorumlar, ek örnekler ve operasyon yönetimi üzerine düşüncelerle genişletmek. Özellikle insan-makine karşılaştırması, süreç adaleti, ifade özgürlüğünün operasyonel öğrenmeye etkisi, deneyim ekonomisi ve kişisel operasyon yönetimi gözlemleri bu katkının parçası.

### Portföy değeri

Bu bölüm, teknik olmayan ama mühendislik yönetimiyle ilişkili bir okuma yetkinliği gösterir. Bir akademik makaledeki kavramları alıp hizmet tasarımı, süreç yönetimi, çalışan davranışı ve müşteri deneyimi gibi daha geniş bir çerçeveye bağlama becerisi portföy açısından değerlidir.

### Riskler

Ham metin çok kişisel ve yer yer polemik. Bazı ülke, şirket, kişi ve siyasi figür örnekleri kamuya açık profesyonel portföyde gereksiz risk yaratır. Ayrıca kişisel önceki iş deneyimi, şirket ve çalışan davranışları hakkında keskin yargılar içeriyor. Bu bölümde akademik kaynak dışı HBR ve diğer örnekler geçiyor; bu üç dosya dışında doğrulanmadığı için kamu sürümünde ya çıkarılmalı ya da sonra ayrıca kaynaklandırılmalı.

### Kamuya açık sürüme nasıl dönüştürülebilir?

Bu bölüm, "Service Operations Research: Reading Notes and Reflections" başlığıyla yeniden yazılabilir. İçerik, Chase ve Apte makalesinin ana kavramlarını kısa ve özgün şekilde anlatmalı; kişisel/polemik örnekler çıkarılmalı; McDonald's, Disney ve deneyim ekonomisi gibi başlıklar yalnızca kavramsal örnek olarak ele alınmalı. Kişisel operasyon deneyimi kullanılacaksa şirket, kişi, ürün ve ölçü iddiaları anonimleştirilmeli ve "kişisel gözlem" olarak sınırlanmalı.

## Makale 2: Saha servisinde çapraz eğitim politikaları

### Ana tema

Makale 2, saha servisinde tamamen çapraz eğitimli teknisyenler ile PM odaklı uzman/dedicated teknisyenler arasında nasıl bir işgücü karması seçileceğini inceliyor. PDF, bakım talebinin sözleşme kapsamı ve bakım politikasıyla etkileştiğini; simülasyonla iş yükü, makine güvenilirliği, bakım sıklığı ve sözleşme kapsamının optimal çapraz eğitim politikasına etkisini değerlendirdiğini gösteriyor.

### Benim katkım

DOCX'te makalenin teknik modeli Türkçe ve açıklayıcı hale getirilmiş: PM/acil bakım ayrımı, E-FSE/N-FSE görev sınırları, maliyet oranı, sabit bütçe, kullanılabilirlik ve ceza puanı gibi bileşenler parçalara ayrılmış. Ayrıca sonuçlar yorumlanmış: N-FSE eklemenin PM gecikmelerini azaltarak acil işe dönüşümü önleyebileceği, fakat fazla N-FSE'nin acil müdahale kapasitesini zayıflatabileceği anlatılmış. Bunun yanında yazarların ihmal ettiği insan motivasyonu, ücret, eğitim bağlılığı ve müşteri algısı gibi etkiler eklenmiş.

### Portföy değeri

Bu bölüm portföy için en güçlü teknik malzeme. Saha servis planlama, kapasite, bakım politikası, simülasyon, hizmet seviyesi ve işgücü tasarımı gibi kavramlar doğrudan endüstriyel mühendislik/operasyon analizi becerisi gösterir. Bu içerik GitHub'da oyuncak simülasyon, Mermaid diyagramı ve sade dokümantasyonla desteklenirse profesyonel görünür.

### Riskler

PDF telifli olduğu için model denklemleri, tablo/grafik sonuçları ve makale metni kopyalanmamalı. DOCX'te özel şirket/staj bağlamı ve "S.E." ile ilgili oran tahmini gibi kurum içi çağrışım yapabilecek ifadeler var. Makaledeki OEM verileri de aynen çoğaltılmamalı; kamu sürümünde gerçek şirket verisi gibi sunulmamalı.

### Kamuya açık sürüme nasıl dönüştürülebilir?

Bu bölüm, "Field Service Cross-Training: A Toy Simulation" olarak yeniden kurulabilir. Gerçek makale modelinin birebir kopyası yerine, aynı problemi anlatan basitleştirilmiş ve özgün bir simülasyon kullanılmalı. E-FSE/N-FSE yerine "flexible technician" ve "PM-focused technician" gibi genel terimler seçilebilir. Çıktılar; backlog, cevap süresi vekili, PM gecikmesi ve kullanım oranı gibi sade metriklerle gösterilebilir. Makale sadece referans olarak verilmeli; PDF repoya eklenmemeli.

## En güçlü halka

En güçlü halka, ikinci makaledeki saha servis çapraz eğitim analizidir. Çünkü konu açık, operasyonel problem net, simülasyona dönüşebilir ve GitHub'da kod/dokümantasyon/diyagram üçlüsüyle gösterilebilir.

## Zayıf halka

Zayıf halka, birinci makale analizindeki dağınık ve polemik kişisel bölümlerdir. Bunlar öğrenme sürecini gösterse de kamuya açık portföyde profesyonel odağı zayıflatabilir. Bu bölüm korunacaksa ciddi biçimde sadeleştirilmeli, anonimleştirilmeli ve kaynaklandırılmalıdır.
