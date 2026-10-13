# SUNRISE · Инвентарь ассетов

Рабочая папка заказчика: `C:\Users\G13\Desktop\CLAUDE\DJSUNRISE`

## Исходные файлы рабочей папки

| Файл | Размер | Что это | В репозитории |
|---|---|---|---|
| `PromoKit SunRise.pdf` | 24 МБ, 10 стр. 16:9, растр | структура и весь текст | `source/promokit/PromoKit-SunRise.pdf` + `slide-01..10.jpg` |
| `Logo SUNRISE Png.png` | 2000×2000, RGBA | лого: красное солнце `#D82E2F` + белый вордмарк | `public/brand/logo-sunrise.png` + векторизация `logo-sunrise.svg` |
| `Photo SUNRISE Png.png` | 789×1080, RGBA | фото артиста, вырез | `public/brand/photo-sunrise-cutout.png` |
| `Referens/1.jpg` | 736×1308 | концепт Netflix O'Brien | `source/references/ref-1-netflix-obrien.jpg` |
| `Referens/2.jpg` | 943×1678 | презентация VISTAS | `source/references/ref-2-vistas-deck.jpg` |
| `Текст под ппт.txt`, `ТЗ ДЛЯ ПРЕЗЕНТАЦИИ.md` | — | бриф (не контент) | — |
| 6 видео | 2.94 ГБ суммарно | см. ниже | не в git (`.gitignore`), постеры в `public/video/posters/` |

## Видео (все обязательны на сайте)

| Код | Файл | Разрешение | FPS | Кодек | Длит. | Вес | Содержание (по контакт-листу) | Постер |
|---|---|---|---|---|---|---|---|---|
| V1 | `Grozzman Sunrise after movie 1.mov` | 3840×1920 (2:1) | 25 | H.264 + AAC | 55.7 с | 257 МБ | open-air фестиваль, экран «SUNRISE B2B GROZZMAN», Heineken-сцена, толпа в красном свете | `after-movie-grozzman-16x9.jpg` |
| V2 | `Sunrise & Grozzman 9x16.mov` | 720×1280 | 25 | H.264 + AAC | 55.7 с | 71 МБ | вертикальная версия V1 | `after-movie-grozzman-9x16.jpg` |
| V3 | `SUNRISE Movie 2.mp4` | 1080×1920 | 59.94 | H.264 + AAC | 30.5 с | 269 МБ | Space Plus Bangkok, «SUNRISE × Pete D», лазеры, пульт | `spaceplus-pete-d-9x16.jpg` |
| V4 | `IMG_7875.MP4` | 1080×1920 | 59.94 | H.264 + AAC | 40.0 с | 177 МБ | клубная ночь от первого лица: приезд, пульт Pioneer, экран SUNRISE, красный дым | `img-7875-9x16.jpg` |
| V5 | `Short SUNRISE film.mov` | 1080×1920 | 60 | HEVC + AAC | 39.6 с | 111 МБ | клуб в синем свете, танцпол, экран SUNRISE, финал Space Plus | `short-film-9x16.jpg` |
| V6 | `SUNRISE Movie.mp4` | ? | ? | ? | ? | 2.06 ГБ | **не проверен** (больше лимита передачи файлов) | — |

Примечание: V1 и V2 содержат дополнительную дорожку mjpeg (обложка) и data-дорожку, при перекодировании брать `-map 0:v:0 -map 0:a:0?`.
V5 в HEVC: для Chrome/Firefox обязательно перекодировать в H.264/AV1.

## Перекодирование
`scripts/transcode.ps1` (Windows, PowerShell, нужен ffmpeg в PATH: `winget install Gyan.FFmpeg`). Запуск из корня репозитория:
```powershell
.\scripts\transcode.ps1 -Src "C:\Users\G13\Desktop\CLAUDE\DJSUNRISE"
```
Результат в `public/video/web/`. Точки начала loop-фрагментов (`-ss`) подобраны по контакт-листам, проверить глазами и при необходимости сдвинуть.

## Обновление 13.10.2026
- Видео V1–V5 перекодированы и лежат в `public/video/` (loop без звука + full со звуком). `scripts/transcode.ps1` больше не нужен.
- V6 `SUNRISE Movie.mp4` (2 ГБ) на сайт не идет (вес, содержание не проверено).
- Hero: `public/brand/portrait-hero.jpg` (оригинал 1672×941) + `portrait-cutout.png/.webp` (вырез без фона, сделан автоматически; на краях легкий красный ореол, на рассветном фоне не виден).
- Галерея: `public/gallery/placeholder-01..12-*.jpg` (временные заглушки с логотипом). Запасной вариант: 31 кадр из видео в `source/video-stills/`.
- Афиши: `public/posters/poster-01..10.jpg` (кропы со слайда 9, низкое разрешение; на постере 05 старый номер +7, заменить оригиналом).
- PDF для скачивания: `public/PromoKit-SunRise.pdf`.
- Референсы: добавлены `ref-3-folioblox.jpg`, `ref-4-dominic.jpg`. Доноры awesome-design-md: `docs/design-refs/`.
