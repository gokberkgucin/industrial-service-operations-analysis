# Repo Strategy

## Temel karar

Bu çalışma GitHub'da "staj defteri yüklemesi" olarak değil, staj sırasında yapılan akademik okuma ve analizden türetilmiş bir portföy projesi olarak konumlandırılmalıdır. Varsayılan güvenli strateji, Siemens adını ve staj defteri formatını kullanmadan; saha servis operasyonları, çapraz eğitim ve basitleştirilmiş simülasyon üzerine anonim bir teknik proje sunmaktır.

## Konumlandırma seçenekleri

### 1. Anonim saha servis operasyonları analizi

- Repo adı: `industrial-service-operations-analysis`
- Kısa açıklama: Field-service workforce design, preventive maintenance, emergency work, and cross-training trade-offs explored through notes, diagrams, and a toy simulation.
- Hedef kitle: Operasyon analizi, endüstri mühendisliği, saha servis, bakım planlama ve teknik proje portföyü inceleyen işe alımcılar.
- Avantaj: En güçlü teknik halkayı öne çıkarır; şirket adı, kişi bilgisi ve resmi staj defteri risklerini azaltır; kod, dokümantasyon ve diyagram üretmeye uygundur.
- Risk: Gerçek şirket/staj bağlamı görünmez hale geldiği için anlatının "nereden doğduğu" fazla silik kalabilir.
- Öneri puanı: 9/10

### 2. Marka adı geçen staj türevli analiz

- Repo adı: `siemens-internship-service-operations-analysis`
- Kısa açıklama: Public-safe reflections and toy modeling derived from an internship reading assignment on service operations and field-service cross-training.
- Hedef kitle: Staj geçmişini doğrudan görmek isteyen işe alımcılar ve LinkedIn/GitHub profilini kronolojik inceleyen teknik okuyucular.
- Avantaj: Staj bağlamını hızlı anlaşılır yapar; çalışmanın gerçek bir profesyonel öğrenme ortamından doğduğunu gösterir.
- Risk: Siemens adını kullanmak güvenli kabul edilmemeli; kurum içi görev, kişi, bölüm, imza/kaşe ve "S.E." gibi ifadeler yanlışlıkla görünürse itibar ve gizlilik riski doğar. Marka adı, çalışmanın şirket tarafından onaylandığı gibi de algılanabilir.
- Öneri puanı: 5/10

### 3. Hizmet operasyonları okuma notları ve kavramsal portföy

- Repo adı: `service-operations-reading-notes`
- Kısa açıklama: Reading notes and public-safe reflections on service operations history, service design, and field-service capacity trade-offs.
- Hedef kitle: Akademik okuma, teknik yazı ve mühendislik yönetimi düşünme becerisini görmek isteyen okuyucular.
- Avantaj: Telifli makaleleri kopyalamadan öğrenme sürecini gösterir; Makale 1 ve Makale 2 daha dengeli temsil edilir.
- Risk: Kod/simülasyon tarafı geri planda kalırsa repo teknik portföy yerine kişisel blog notu gibi görünebilir. Makale 1'deki polemik ve kişisel bölümler ciddi temizlik ister.
- Öneri puanı: 7/10

## Ana strateji

Ana strateji olarak 1. seçenek seçilmeli: `industrial-service-operations-analysis`.

Nedeni basit: önceki envanterde en güçlü halka ikinci makaledeki saha servis çapraz eğitim analiziydi. Bu konu GitHub için doğal biçimde kod, diyagram ve açıklayıcı dokümana dönüşüyor. Aynı zamanda şirket adı, kişi adı, staj defteri formu ve telifli PDF içeriği gibi riskli unsurları dışarıda bırakmaya en uygun seçenek bu.

Bu stratejide anlatı şöyle kurulmalı:

> This repository turns an internship reading assignment into a public-safe portfolio project on industrial service operations and field-service workforce flexibility.

Bu cümle staj kökenini saklamaz, ama şirket adı veya kuruma yaslanan bir iddia kurmaz.

## Minimal sürüm

Minimal sürüm, hızlı ve güvenli ilk GitHub yayınıdır.

- README'de proje amacı, kapsam, güvenli paylaşım notu ve hızlı çalıştırma komutu yer alır.
- `src/field_service_toy_simulation.py` çalışır durumda kalır.
- `docs/tr/project-overview.md` kamuya açık, anonim ve kısa proje özeti olur.
- `docs/tr/article-2-field-service-cross-training.md` ikinci makaleden türetilmiş özgün, kısa analiz notu olur.
- `docs/figures/field-service-tradeoff.mmd` temel işgücü tasarım diyagramı olarak kullanılır.
- `REFERENCES.md` içinde iki akademik makale bibliyografik kaynak olarak verilir; PDF dosyaları repoya eklenmez.
- `planning/` klasörü GitHub'a konacaksa içindeki risk analizleri gözden geçirilmeli; daha güvenlisi ilk public sürümde planning dosyalarını repo dışında tutmaktır.

## Güçlü sürüm

Güçlü sürüm, portföy etkisini artıran daha tamamlanmış yayındır.

- Python simülasyonu birkaç senaryoyu karşılaştırır: düşük/yüksek iş yükü, düşük/yüksek cross-training oranı, farklı PM talep oranları.
- Notebook, aynı senaryoları tablo ve grafiklerle açıklar.
- `docs/en/project-overview.md` İngilizce portföy anlatısı olarak tamamlanır.
- `docs/tr/article-1-service-operations-history.md` polemiklerden arındırılmış kısa literatür okuma notuna dönüşür.
- `docs/tr/article-2-field-service-cross-training.md` ana teknik yazı olur; doğrudan/dolaylı etki, backlog, utilization ve service responsiveness kavramları sade biçimde anlatılır.
- Mermaid diyagramları README'de veya docs içinde render edilebilir şekilde bağlanır.
- `public-sharing-note.md` kısa bir gizlilik/telif notu olarak korunur.
- Ham staj defteri, kişi adları, kurum içi bağlam ve telifli PDF'ler kesinlikle eklenmez.

## README ve docs ayrımı

### README'ye gitmeli

- Projenin tek cümlelik amacı
- "Public-safe portfolio project" konumlandırması
- Kısa problem tanımı: saha servisinde esneklik ve uzmanlaşma dengesi
- Repo içeriği: docs, figures, notebook, src
- Simülasyonu çalıştırma komutu
- Kısa örnek çıktı veya beklenen metrikler
- Telif/gizlilik notu: ham staj defteri ve akademik PDF'ler dahil değildir
- Kaynaklara kısa bağlantı: `REFERENCES.md`

### docs altına gitmeli

- `docs/tr/project-overview.md`: Türkçe kapsam ve arka plan
- `docs/en/project-overview.md`: İngilizce portföy özeti
- `docs/tr/article-1-service-operations-history.md`: Makale 1'den türetilmiş sade literatür okuma notu
- `docs/tr/article-2-field-service-cross-training.md`: Ana teknik analiz yazısı
- `docs/tr/lessons-learned.md`: Öğrenilenler, ama kişisel/polemik olmayan biçimde
- `docs/tr/public-sharing-note.md`: Kamuya açık sürümde çıkarılan içerikler ve nedenleri
- `docs/figures/`: Mermaid diyagramları

### README'ye gitmemeli

- Siemens veya başka kurum içi bağlam
- Staj defteri formu, imza/kaşe, kişi adları
- Telifli makale metni, tablo/grafik kopyaları
- Doğrulanmamış üretkenlik, maliyet, kurum veya ülke genellemeleri
- Polemik örnekler ve profesyonel odağı dağıtan kişisel bölümler

## Sonuç önerisi

İlk public sürüm için repo adı mevcut haliyle korunmalı: `industrial-service-operations-analysis`. README kısa ve profesyonel olmalı; ana ağırlık `article-2-field-service-cross-training.md`, oyuncak simülasyon ve Mermaid diyagramlarında olmalı. Marka adı geçen strateji yalnızca özel bir nedenle, tüm metinler yeniden denetlenip kurum onayı algısı yaratmayacak şekilde düzenlendikten sonra düşünülmelidir.
