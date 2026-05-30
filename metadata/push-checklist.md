# Push Checklist

Tarih: 2026-05-30 21:04:24

Bu dosya, yerel repo GitHub'a gönderilmeden önce izlenecek kontrol listesini ve exact PowerShell / git komutlarını verir. Push işlemi otomatik başlatılmadı.

## Repo Durumu

| Kontrol | Sonuç |
|---|---|
| Git repo initialized mı? | Evet |
| Aktif branch | `main` |
| Remote tanımlı mı? | Hayır |
| QA raporu geçti mi? | Evet |

## Checklist

| Madde | Durum | Not |
|---|---|---|
| QA geçti mi? | PASS | `python .\scripts\verify_repo.py` son çalıştırma sonucu `metadata/qa-report.md` içine yazıldı. |
| Görsel linkleri çalışıyor mu? | PASS | QA raporu görsel linklerini kontrol ediyor. |
| README linkleri çalışıyor mu? | PASS | README iki ana yazıya relative link içeriyor. |
| Publication note hazır mı? | PASS | `docs/publication-note.md` mevcut. |
| `.gitignore` doğru mu? | PASS | `_work/`, `__pycache__/`, `.venv/`, `*.log`, `Thumbs.db`, `.DS_Store` kontrol edildi. |
| Gereksiz `_work` dosyaları commit dışı mı? | PASS | `git status --ignored` çıktısında `_work/` ignored görünüyor. |

## Git Init Durumu

Bu klasörde Git zaten initialized görünüyor. Eğer farklı bir klasörde aynı akışı sıfırdan kurmak gerekirse:

```powershell
Set-Location 'D:\TOPLANDIK\GitHub\industrial-service-operations-analysis'
git init
git branch -M main
```

## Remote Durumu

Bu kontrolde `origin` remote tanımlı görünmüyor. Ana önerilen remote SSH:

```powershell
git remote add origin git@github.com:gokberkgucin/industrial-service-operations-analysis.git
```

HTTPS alternatifi:

```powershell
git remote add origin https://github.com/gokberkgucin/industrial-service-operations-analysis.git
```

Remote zaten tanımlıysa `add` yerine şu komut kullanılmalı:

```powershell
git remote set-url origin git@github.com:gokberkgucin/industrial-service-operations-analysis.git
```

## Önerilen Exact Push Akışı

Komutlar kullanıcı tarafından elle çalıştırılmalıdır. Credential isteme veya otomatik push yapılmadı.

```powershell
Set-Location 'D:\TOPLANDIK\GitHub\industrial-service-operations-analysis'
python .\scripts\verify_repo.py
git status --short --ignored
git add .gitignore README.md LICENSE.md docs assets metadata scripts
git status --short
git commit -m "docs: publish curated internship service operations analysis" -m "Publish the cleaned public GitHub version of the internship analysis repository, including the two main Markdown articles, curated images, metadata, QA checks, publication notes, references, and license placeholder."
git branch -M main
git remote add origin git@github.com:gokberkgucin/industrial-service-operations-analysis.git
git push -u origin main
```

HTTPS ile göndermek istenirse remote satırı şöyle değiştirilmeli:

```powershell
git remote add origin https://github.com/gokberkgucin/industrial-service-operations-analysis.git
```

## Mevcut `git status --short --ignored` Çıktısı

```text
M .gitignore
 M README.md
?? LICENSE.md
?? assets/
?? docs/
?? metadata/
?? scripts/
!! _work/
!! scripts/__pycache__/
```

## Mevcut `git remote -v` Çıktısı

```text
(remote yok)
```

## Not

`git add .gitignore README.md LICENSE.md docs assets metadata scripts` komutu `_work/` klasörünü stage etmez; `.gitignore` bu klasörü dışarıda bırakır. Eski kök taslak dosyaların nihai minimal repoda kalıp kalmayacağı ayrı bir temizlik kararıdır.
