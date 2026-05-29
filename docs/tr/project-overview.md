# Proje Özeti

Bu proje, saha servis operasyonlarında esnek işgücü ile uzmanlaşmış işgücü arasındaki dengeyi anlamak için hazırlanmış kamuya açık bir portföy çalışmasıdır.

## Amaç

Önleyici bakım, acil müdahale, iş yükü ve teknisyen yetkinliği arasındaki ilişkiyi sade bir modelle açıklamak.

## Kapsam

- Hizmet operasyonları literatüründen kısa arka plan
- Saha servisinde çapraz eğitim ve uzmanlaşma ayrımı
- Kamuya açık, anonim bir demo simülasyon
- Mermaid diyagramları ile kavramsal anlatım

## Demo Simülasyon

Repoda yer alan `src/field_service_toy_simulation.py` dosyası eğitim amaçlı küçük bir demo modeldir. Bu model makaledeki simülasyonun kopyası değildir; makale sonuçlarını yeniden üretme iddiası taşımaz.

Modelin amacı, şu temel gerilimi görünür kılmaktır: Esnek teknisyenler hem acil işlere hem de PM işlerine atanabilirken, PM odaklı teknisyenler planlı bakım gecikmesini azaltabilir. Ancak PM odaklı teknisyen oranı arttıkça acil işlere cevap verebilen esnek kapasite azalabilir.

Oynanabilir parametreler:

- `workload`: günlük servis talebi baskısı
- `preventive_maintenance_interval`: planlı bakım aralığı
- `machine_reliability_proxy`: sentetik makine güvenilirliği göstergesi
- `dedicated_technician_ratio`: PM odaklı teknisyen oranı

Notebook çıktıları üç öğretici metriği görselleştirir: emergency response proxy, PM timeliness proxy ve toplam penalty-like score.

## Sınır

Bu proje gerçek organizasyon verisi veya kurum içi belge içermez. Simülasyon öğretici amaçlıdır.
