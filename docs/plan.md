# План проекта

## 1. Каркас: uv, Django, ruff, pytest, git, .env

- [x] uv + Django, `uv sync`
- [x] `startproject config .`, `migrate`
- [x] Имя проекта в `pyproject.toml`
- [x] `.gitignore` (venv, db.sqlite3, .idea)
- [x] ruff (линтер + форматтер)
- [x] pytest + pytest-django
- [x] `.env` + `.env.example`, секреты из settings.py
- [x] Первый коммит

## 2. Модели и админка

- [x] Service, Project, Review, Lead
- [x] Регистрация в админке, `createsuperuser`

## 3. Pillow: загрузка фото, миниатюры

- [ ] Работа через ветки и PR (с этого этапа)
- [ ] Pillow, `MEDIA_ROOT` / `MEDIA_URL`, `media/` в `.gitignore`
- [ ] Фото у `Service` (`ImageField`)
- [ ] Галерея объекта: модель `ProjectImage` (несколько фото на объект), inline в админке
- [ ] Отдача media в режиме разработки
- [ ] Миниатюры: уменьшение фото при сохранении

## 4. Страницы и шаблоны, Bootstrap

- [ ]

## 5. Форма заявки + уведомление в Telegram

- [ ]

## 6. Тесты моделей и формы

- [ ]

## 7. Docker + docker-compose + gunicorn + PostgreSQL

- [ ]

## 8. GitHub Actions (ruff + pytest на каждый пуш)

- [ ]

## 9. VPS: деплой, HTTPS, домен

- [ ]

## 10. Потом: немного JS (галерея), SEO-основы

- [ ]
