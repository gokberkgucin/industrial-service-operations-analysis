# Section Map

Bu dosya, `_work/extracted/report-raw.txt` ve DOCX paragraf/stil yapısının ilk geçiş analizine dayanır. Amaç nihai metni yazmak değil; ham staj defterinin hangi parçalarının README, `docs/internship-part-1.md` ve `docs/internship-part-2.md` dosyalarına dönüşeceğini netleştirmektir.

## Ana Karar

Staj defteri iki ana Markdown dosyasına bölünecek:

- `docs/internship-part-1.md`: Makale Ödevi 1, yani `Hizmet Operasyonları Hakkında bir Deneme`.
- `docs/internship-part-2.md`: Makale Ödevi 2, yani saha servisinde çapraz eğitim ve bakım politikaları analizi.

README yalnızca portal olacak; ham staj defteri gibi uzun anlatı taşımayacak.

## Makale Ödevi Sınırları

| Sınır | Ham rapor izi | Hedef |
|---|---|---|
| Ön bağlam | Satır 57-78: iki akademik makale görevi ve ortak notlar | README'de kısa bağlam |
| Makale Ödevi 1 başlangıcı | Satır 80: `Hizmet Operasyonları Hakkında bir Deneme` | `docs/internship-part-1.md` |
| Makale Ödevi 2 başlangıcı | Satır 235: `Bu makale, bakım hizmeti satan bir şirketin;` | `docs/internship-part-2.md` |
| Yayın dışı form alanı | Satır 437 ve sonrası: öğrenci bilgileri, defter kontrolü, iş yaprağı formları | Public repo dışında |

## Yayın Dışı Kalacak Bölümler

- Kapak ve üniversite/form sayfaları: `KARABÜK ÜNİVERSİTESİ`, `MÜHENDİSLİK FAKÜLTESİ`, `Staj Defteri`, `Staj Genel Bilgileri`.
- Kişisel/kurumsal form alanları: `Staj Yapan Öğrenci`, `Staj Yapılan İş Yeri`, `İş Yeri Yetkilisi`, `Staj Komisyonu`, `Öğrenci Numarası`, `Adı Soyadı`, `İletişim Bilgileri`, `Yetkili İmzası`.
- Defter kontrolü ve iş yaprağı şablonları: `Defter Kontrolü`, `İŞ YAPRAĞI`, `Makale Ödevi 1`, `Makale Ödevi 2` form satırları.
- Kişi adı içeren görev atama cümleleri ham haliyle kullanılmayacak; README'de anonim ve kısa görev bağlamına dönüştürülecek.
- Üçüncü taraf fotoğraflar, üniversite/kurum logoları, makaleden alınmış denklem/figür/table görüntüleri doğrudan public repoya konmayacak.
- Polemik/politik yan sapmalar ham dille taşınmayacak; gerekirse operasyon yönetimi açısından nötr bir cümleye indirgenecek.

## README'ye Kısaca Girecek Bölümler

- Staj sırasında iki akademik makale verildiği ve analiz/yorum görevi yapıldığı.
- İncelenen iki çalışma: hizmet operasyonları tarihçesi ve saha servisinde çapraz eğitim politikaları.
- Public sürümün ham staj defteri değil, seçilmiş portföy sürümü olduğu.
- Okuma yönlendirmesi: Part 2 teknik merkez, Part 1 kavramsal arka plan.
- Telif/gizlilik sınırı: ham PDF/DOCX ve form sayfaları paylaşılmayacak.

## `docs/internship-part-1.md` Bölüm Haritası

Kaynak başlık mantığı korunacak, fakat dil profesyonelleştirilecek.

| Ham başlık | Karar |
|---|---|
| `Hizmet Operasyonları Hakkında bir Deneme` | Dosyanın ana gövdesi |
| `1.Atalarımızın meslek seçimi` | Kısa ve dikkatli bağlam; iddialar yumuşatılmalı |
| `2. Sonraki Nesiller?` | Özetlenebilir |
| `3.Sanayiden Hizmete Doğru` | Politik/polemik kısımlar ayıklanarak kavramsal özet |
| `4.ilk Çalışmalar ve İnsan-Fonksiyon` | Korunacak; hizmette insan değişkenliği teması |
| `5.Hizmet Operasyonlarının Başarılı ilk Örneklerinden: McDonald's` | Korunabilir; üçüncü taraf görsel yeniden çizilmeli |
| `6.Hizmet Operasyonlarının Başarılı ilk Örneklerinden: Disney ve ..` | Korunabilir; fotoğraf kullanılmamalı |
| `7.Kişisel Operasyon Yönetimi Deneyimi` | Kısa, profesyonel ve kişisel veri içermeyen özet |
| `8. Süreç: Sonuçlardan Daha Önemli Olabilir` | Korunacak; yönetimsel çıkarım olarak yazılacak |
| `9.İfade Özgürlüğünün bir Sürü ‘Bonusu’ Var.` | Ham başlık ve polemik yayın dışı; gerekirse geri bildirim/öğrenme kültürü olarak dönüştür |
| `10.Sadece ‘Farklılaştırma’ Yetmez ama Olmalı` | Korunabilir; deneyim tasarımı ve hizmet farklılaştırma bağlamına çekilecek |

## `docs/internship-part-2.md` Bölüm Haritası

Bu dosya teknik merkez olacak. Ham başlık mantığı korunacak, fakat denklem/grafik/table görselleri kopyalanmayacak.

| Ham başlık / iz | Karar |
|---|---|
| `Bu makale, bakım hizmeti satan bir şirketin;` | Problem tanımı |
| `Genel Bilgiler, Denklemler, Varsayım ve Kabuller` | Model omurgası |
| `1.Önleyici Bakım - Acil Olmayan Bakım: (PM)` | Bakım türleri |
| `2.Onarıcı Bakım – Acil Bakım` | Bakım türleri |
| `1.Çapraz-Eğitimli Teknisyen (E-FSE)` | Teknisyen türleri |
| `2. Çapraz-Eğitimli Olmayan Teknisyen (N-FSE)` | Teknisyen türleri |
| `Yetenek`, `Maliyet`, `Verimlilikler`, `Bütçe` | Varsayımlar |
| `Önleyici Bakım (PM)`, `Makine Güvenilirliği` | PM ve arıza ilişkisi |
| `Kullanılabilirlik`, `İşgücü Oranı`, `Ceza Puanı` | Performans ölçütleri |
| `Benzetim Deneyinden Çıkan Bazı Sonuçlar ve Onların Yorumlanması` | Ana sonuçlar ve yorum |
| `1. DE: Doğrudan Etki` | Direct effect açıklaması |
| `2. IE: Dolaylı Etki` | Indirect effect açıklaması |
| `Çalışma Saati Garantili Sözleşme Türü` | Sözleşme ve müşteri algısı |
| `SONUÇ` | Kısa teknik kapanış |

## Görsel İlk Geçiş İsimlendirme Önerisi

| Eski ad | Önerilen yeni ad | Hangi markdown | Aksiyon | Not |
|---|---|---|---|---|
| `image1.png` | `karabuk-universitesi-logo.png` | Yayın dışı | private_do_not_publish | Kapak/form logosu; public portföyde gereksiz. |
| `image2.svg` | `digital-photo-placeholder.svg` | Yayın dışı | private_do_not_publish | Dijital fotoğraf/placeholder; kişisel form alanı. |
| `image3.png` | `digital-photo-placeholder.png` | Yayın dışı | private_do_not_publish | Dijital fotoğraf/placeholder; kişisel form alanı. |
| `image4.jpg` | `siemens-energy-business-units-context.jpg` | README.md | redraw_or_summarize | Kurumsal bağlam için ancak sade yeniden çizimle kullanılmalı. |
| `image5.jpg` | `mcdonalds-burgernomics-concept.jpg` | docs/internship-part-1.md | redraw_only | Üçüncü taraf görsel; doğrudan değil, kavram olarak yeniden çizilmeli. |
| `image6.jpeg` | `disney-service-experience-example-01.jpeg` | docs/internship-part-1.md | private_or_redraw | Üçüncü taraf fotoğraf; doğrudan yayınlanmamalı. |
| `image7.jpeg` | `disney-service-experience-example-02.jpeg` | docs/internship-part-1.md | private_or_redraw | Üçüncü taraf fotoğraf; doğrudan yayınlanmamalı. |
| `image8.jpeg` | `service-experience-critical-moment-example-01.jpeg` | docs/internship-part-1.md | private_do_not_publish | Kişi/fotoğraf içeren örnek; public sürümde metinsel örnek veya yeniden çizim kullanılmalı. |
| `image9.jpg` | `service-experience-critical-moment-example-02.jpg` | docs/internship-part-1.md | private_do_not_publish | Kişi/fotoğraf içeren örnek; public sürümde metinsel örnek veya yeniden çizim kullanılmalı. |
| `image10.jpeg` | `service-experience-critical-moment-example-03.jpeg` | docs/internship-part-1.md | private_do_not_publish | Kişi/fotoğraf içeren örnek; public sürümde metinsel örnek veya yeniden çizim kullanılmalı. |
| `image11.jpg` | `service-experience-critical-moment-example-04.jpg` | docs/internship-part-1.md | private_do_not_publish | Kişi/fotoğraf içeren örnek; public sürümde metinsel örnek veya yeniden çizim kullanılmalı. |
| `image12.JPG` | `penalty-function-equation.jpg` | docs/internship-part-2.md | redraw_only | Makaledeki denklem/figür parçası; Markdown'da özgün yazım veya yeniden çizim kullanılmalı. |
| `image13.JPG` | `intensity-functions-small-chart.jpg` | docs/internship-part-2.md | redraw_only | Makaledeki denklem/figür parçası; Markdown'da özgün yazım veya yeniden çizim kullanılmalı. |
| `image14.JPG` | `availability-formula-fragment.jpg` | docs/internship-part-2.md | redraw_only | Makaledeki denklem/figür parçası; Markdown'da özgün yazım veya yeniden çizim kullanılmalı. |
| `image15.JPG` | `workforce-ratio-formula-fragment.jpg` | docs/internship-part-2.md | redraw_only | Makaledeki denklem/figür parçası; Markdown'da özgün yazım veya yeniden çizim kullanılmalı. |
| `image16.JPG` | `penalty-equation-fragment.jpg` | docs/internship-part-2.md | redraw_only | Makaledeki denklem/figür parçası; Markdown'da özgün yazım veya yeniden çizim kullanılmalı. |
| `image17.JPG` | `penalty-symbol-p.jpg` | docs/internship-part-2.md | redraw_only | Makaledeki denklem/figür parçası; Markdown'da özgün yazım veya yeniden çizim kullanılmalı. |
| `image18.JPG` | `downtime-symbol-l.jpg` | docs/internship-part-2.md | redraw_only | Makaledeki denklem/figür parçası; Markdown'da özgün yazım veya yeniden çizim kullanılmalı. |
| `image19.JPG` | `penalty-weight-pl.jpg` | docs/internship-part-2.md | redraw_only | Makaledeki denklem/figür parçası; Markdown'da özgün yazım veya yeniden çizim kullanılmalı. |
| `image20.JPG` | `emergency-response-time-symbol.jpg` | docs/internship-part-2.md | redraw_only | Makaledeki denklem/figür parçası; Markdown'da özgün yazım veya yeniden çizim kullanılmalı. |
| `image21.JPG` | `emergency-penalty-weight-symbol.jpg` | docs/internship-part-2.md | redraw_only | Makaledeki denklem/figür parçası; Markdown'da özgün yazım veya yeniden çizim kullanılmalı. |
| `image22.JPG` | `normal-penalty-weight-symbol.jpg` | docs/internship-part-2.md | redraw_only | Makaledeki denklem/figür parçası; Markdown'da özgün yazım veya yeniden çizim kullanılmalı. |
| `image23.JPG` | `normal-response-time-symbol.jpg` | docs/internship-part-2.md | redraw_only | Makaledeki denklem/figür parçası; Markdown'da özgün yazım veya yeniden çizim kullanılmalı. |
| `image24.JPG` | `normal-response-delay-equation.jpg` | docs/internship-part-2.md | redraw_only | Makaledeki denklem/figür parçası; Markdown'da özgün yazım veya yeniden çizim kullanılmalı. |
| `image25.jpeg` | `normal-job-count-symbol.jpg` | docs/internship-part-2.md | redraw_only | Makaledeki denklem/figür parçası; Markdown'da özgün yazım veya yeniden çizim kullanılmalı. |
| `image26.JPG` | `scheduled-maintenance-time-symbol.jpg` | docs/internship-part-2.md | redraw_only | Makaledeki denklem/figür parçası; Markdown'da özgün yazım veya yeniden çizim kullanılmalı. |
| `image27.jpeg` | `actual-arrival-time-symbol.jpg` | docs/internship-part-2.md | redraw_only | Makaledeki denklem/figür parçası; Markdown'da özgün yazım veya yeniden çizim kullanılmalı. |
| `image28.jpeg` | `normal-response-time-symbol-2.jpg` | docs/internship-part-2.md | redraw_only | Makaledeki denklem/figür parçası; Markdown'da özgün yazım veya yeniden çizim kullanılmalı. |
| `image29.emf` | `part-2-equation-or-diagram-fragment-29.emf` | docs/internship-part-2.md | redraw_only | EMF denklem/şema parçası; doğrudan yayın yerine yeniden yazım/çizim. |
| `image30.emf` | `part-2-equation-or-diagram-fragment-30.emf` | docs/internship-part-2.md | redraw_only | EMF denklem/şema parçası; doğrudan yayın yerine yeniden yazım/çizim. |
| `image31.emf` | `part-2-equation-or-diagram-fragment-31.emf` | docs/internship-part-2.md | redraw_only | EMF denklem/şema parçası; doğrudan yayın yerine yeniden yazım/çizim. |
| `image32.emf` | `part-2-equation-or-diagram-fragment-32.emf` | docs/internship-part-2.md | redraw_only | EMF denklem/şema parçası; doğrudan yayın yerine yeniden yazım/çizim. |
| `image33.emf` | `part-2-equation-or-diagram-fragment-33.emf` | docs/internship-part-2.md | redraw_only | EMF denklem/şema parçası; doğrudan yayın yerine yeniden yazım/çizim. |
| `image34.emf` | `part-2-equation-or-diagram-fragment-34.emf` | docs/internship-part-2.md | redraw_only | EMF denklem/şema parçası; doğrudan yayın yerine yeniden yazım/çizim. |
| `image35.emf` | `part-2-equation-or-diagram-fragment-35.emf` | docs/internship-part-2.md | redraw_only | EMF denklem/şema parçası; doğrudan yayın yerine yeniden yazım/çizim. |
| `image36.emf` | `part-2-equation-or-diagram-fragment-36.emf` | docs/internship-part-2.md | redraw_only | EMF denklem/şema parçası; doğrudan yayın yerine yeniden yazım/çizim. |
| `image37.emf` | `part-2-equation-or-diagram-fragment-37.emf` | docs/internship-part-2.md | redraw_only | EMF denklem/şema parçası; doğrudan yayın yerine yeniden yazım/çizim. |
| `image38.emf` | `part-2-equation-or-diagram-fragment-38.emf` | docs/internship-part-2.md | redraw_only | EMF denklem/şema parçası; doğrudan yayın yerine yeniden yazım/çizim. |
| `image39.emf` | `part-2-equation-or-diagram-fragment-39.emf` | docs/internship-part-2.md | redraw_only | EMF denklem/şema parçası; doğrudan yayın yerine yeniden yazım/çizim. |
| `image40.emf` | `part-2-equation-or-diagram-fragment-40.emf` | docs/internship-part-2.md | redraw_only | EMF denklem/şema parçası; doğrudan yayın yerine yeniden yazım/çizim. |
| `image41.emf` | `part-2-equation-or-diagram-fragment-41.emf` | docs/internship-part-2.md | redraw_only | EMF denklem/şema parçası; doğrudan yayın yerine yeniden yazım/çizim. |
| `image42.emf` | `part-2-equation-or-diagram-fragment-42.emf` | docs/internship-part-2.md | redraw_only | EMF denklem/şema parçası; doğrudan yayın yerine yeniden yazım/çizim. |
| `image43.emf` | `part-2-equation-or-diagram-fragment-43.emf` | docs/internship-part-2.md | redraw_only | EMF denklem/şema parçası; doğrudan yayın yerine yeniden yazım/çizim. |
| `image44.emf` | `part-2-equation-or-diagram-fragment-44.emf` | docs/internship-part-2.md | redraw_only | EMF denklem/şema parçası; doğrudan yayın yerine yeniden yazım/çizim. |
| `image45.emf` | `part-2-equation-or-diagram-fragment-45.emf` | docs/internship-part-2.md | redraw_only | EMF denklem/şema parçası; doğrudan yayın yerine yeniden yazım/çizim. |
| `image46.emf` | `part-2-equation-or-diagram-fragment-46.emf` | docs/internship-part-2.md | redraw_only | EMF denklem/şema parçası; doğrudan yayın yerine yeniden yazım/çizim. |
| `image47.emf` | `part-2-equation-or-diagram-fragment-47.emf` | docs/internship-part-2.md | redraw_only | EMF denklem/şema parçası; doğrudan yayın yerine yeniden yazım/çizim. |
| `image48.emf` | `part-2-equation-or-diagram-fragment-48.emf` | docs/internship-part-2.md | redraw_only | EMF denklem/şema parçası; doğrudan yayın yerine yeniden yazım/çizim. |
| `image49.emf` | `part-2-equation-or-diagram-fragment-49.emf` | docs/internship-part-2.md | redraw_only | EMF denklem/şema parçası; doğrudan yayın yerine yeniden yazım/çizim. |
| `image50.emf` | `part-2-equation-or-diagram-fragment-50.emf` | docs/internship-part-2.md | redraw_only | EMF denklem/şema parçası; doğrudan yayın yerine yeniden yazım/çizim. |
| `image51.emf` | `part-2-equation-or-diagram-fragment-51.emf` | docs/internship-part-2.md | redraw_only | EMF denklem/şema parçası; doğrudan yayın yerine yeniden yazım/çizim. |
| `image52.emf` | `part-2-equation-or-diagram-fragment-52.emf` | docs/internship-part-2.md | redraw_only | EMF denklem/şema parçası; doğrudan yayın yerine yeniden yazım/çizim. |
| `image53.emf` | `part-2-equation-or-diagram-fragment-53.emf` | docs/internship-part-2.md | redraw_only | EMF denklem/şema parçası; doğrudan yayın yerine yeniden yazım/çizim. |
| `image54.emf` | `part-2-equation-or-diagram-fragment-54.emf` | docs/internship-part-2.md | redraw_only | EMF denklem/şema parçası; doğrudan yayın yerine yeniden yazım/çizim. |
| `image55.emf` | `part-2-equation-or-diagram-fragment-55.emf` | docs/internship-part-2.md | redraw_only | EMF denklem/şema parçası; doğrudan yayın yerine yeniden yazım/çizim. |
| `image56.emf` | `part-2-equation-or-diagram-fragment-56.emf` | docs/internship-part-2.md | redraw_only | EMF denklem/şema parçası; doğrudan yayın yerine yeniden yazım/çizim. |
| `image57.emf` | `part-2-equation-or-diagram-fragment-57.emf` | docs/internship-part-2.md | redraw_only | EMF denklem/şema parçası; doğrudan yayın yerine yeniden yazım/çizim. |
| `image58.JPG` | `response-time-availability-tradeoff-chart.jpg` | docs/internship-part-2.md | redraw_only | Makale/ödev grafiği; public sürümde sentetik veya yeniden çizilmiş görsel kullanılmalı. |
| `image59.emf` | `part-2-equation-or-diagram-fragment-59.emf` | docs/internship-part-2.md | redraw_only | EMF denklem/şema parçası; yeniden çizilmeli. |
| `image60.emf` | `part-2-equation-or-diagram-fragment-60.emf` | docs/internship-part-2.md | redraw_only | EMF denklem/şema parçası; yeniden çizilmeli. |
| `image61.JPG` | `direct-effect-formula.jpg` | docs/internship-part-2.md | redraw_only | DE formülü; metinde yeniden yazılmalı. |
| `image62.JPG` | `indirect-effect-formula.jpg` | docs/internship-part-2.md | redraw_only | IE formülü; metinde yeniden yazılmalı. |
| `image63.emf` | `part-2-equation-symbol-63.emf` | docs/internship-part-2.md | redraw_only | Denklem sembolü; doğrudan görsel olarak gereksiz. |
| `image64.emf` | `part-2-equation-symbol-64.emf` | docs/internship-part-2.md | redraw_only | Denklem sembolü; doğrudan görsel olarak gereksiz. |
| `image65.emf` | `part-2-equation-symbol-65.emf` | docs/internship-part-2.md | redraw_only | Denklem sembolü; doğrudan görsel olarak gereksiz. |
| `image66.emf` | `part-2-equation-symbol-66.emf` | docs/internship-part-2.md | redraw_only | Denklem sembolü; doğrudan görsel olarak gereksiz. |
| `image67.emf` | `part-2-equation-symbol-67.emf` | docs/internship-part-2.md | redraw_only | Denklem sembolü; doğrudan görsel olarak gereksiz. |
| `image68.JPG` | `part-2-results-table-01.jpg` | docs/internship-part-2.md | summarize_only | Tablo görseli; public sürümde tablo kopyası yerine yorum/özet. |
| `image69.emf` | `part-2-results-table-02.emf` | docs/internship-part-2.md | summarize_only | Tablo görseli; public sürümde tablo kopyası yerine yorum/özet. |
| `image70.JPG` | `part-2-results-table-03.jpg` | docs/internship-part-2.md | summarize_only | Tablo görseli; public sürümde tablo kopyası yerine yorum/özet. |
| `image71.JPG` | `part-2-results-table-04.jpg` | docs/internship-part-2.md | summarize_only | Tablo görseli; public sürümde tablo kopyası yerine yorum/özet. |
| `image72.JPG` | `part-2-results-table-05.jpg` | docs/internship-part-2.md | summarize_only | Tablo görseli; public sürümde tablo kopyası yerine yorum/özet. |
| `image73.emf` | `part-2-equation-symbol-73.emf` | docs/internship-part-2.md | redraw_only | EMF denklem/sembol parçası; doğrudan yayınlanmamalı. |
| `image74.emf` | `part-2-equation-symbol-74.emf` | docs/internship-part-2.md | redraw_only | EMF denklem/sembol parçası; doğrudan yayınlanmamalı. |
| `image75.emf` | `part-2-equation-symbol-75.emf` | docs/internship-part-2.md | redraw_only | EMF denklem/sembol parçası; doğrudan yayınlanmamalı. |
| `image76.emf` | `part-2-equation-symbol-76.emf` | docs/internship-part-2.md | redraw_only | EMF denklem/sembol parçası; doğrudan yayınlanmamalı. |
| `image77.emf` | `part-2-equation-symbol-77.emf` | docs/internship-part-2.md | redraw_only | EMF denklem/sembol parçası; doğrudan yayınlanmamalı. |
| `image78.emf` | `part-2-equation-symbol-78.emf` | docs/internship-part-2.md | redraw_only | EMF denklem/sembol parçası; doğrudan yayınlanmamalı. |
| `image79.emf` | `part-2-equation-symbol-79.emf` | docs/internship-part-2.md | redraw_only | EMF denklem/sembol parçası; doğrudan yayınlanmamalı. |
| `image80.JPG` | `intensity-functions-annotated-chart.jpg` | docs/internship-part-2.md | redraw_only | Grafik fikri yeniden çizilebilir; orijinal görsel kopyalanmamalı. |
