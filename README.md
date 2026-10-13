# SUNRISE · e-press-kit

Сайт-презентация диджея **SUNRISE (Bangkok // Pattaya)** для букинг-агентств и промоутеров. Заменяет PDF «PromoKit SunRise».

**Этап 1 (готово): подготовка.** Верстка еще не начиналась.

| Документ | Что внутри |
|---|---|
| [`docs/TZ.md`](docs/TZ.md) | техническое задание: структура (из PDF), посекционный сценарий и анимации, видео, тур, стек, приемка |
| [`docs/DESIGN-SYSTEM.md`](docs/DESIGN-SYSTEM.md) | дизайн-система: типографика, сетка, палитра, ритм, пространство, моушн, анти-слоп чек-лист |
| [`docs/CONTENT.md`](docs/CONTENT.md) | весь текст со слайдов: резиденции, 51 позиция артистов, прогресс, 34 площадки, 11 дат тура, контакты |
| [`docs/ASSETS.md`](docs/ASSETS.md) | инвентарь файлов и 6 видео, перекодирование |
| [`CLAUDE.md`](CLAUDE.md) | инструкция для Claude Code в терминале |

```
source/promokit/    PDF + слайды JPG + кроп постера тура
source/references/  референсы стиля
public/brand/       логотип (PNG, SVG с отдельными лучами), фото артиста
public/video/posters/  постеры (первые кадры) для всех видео
scripts/            transcode.ps1, vectorize-logo.py
```

Исходные видео в git не лежат (лимит GitHub), берутся из рабочей папки `C:\Users\G13\Desktop\CLAUDE\DJSUNRISE`.
