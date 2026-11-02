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

- [x] Работа через ветки и PR (с этого этапа)
- [x] Pillow, `MEDIA_ROOT` / `MEDIA_URL`, `media/` в `.gitignore`
- [x] Фото у `Service` (`ImageField`)
- [x] Галерея объекта: модель `ProjectImage` (несколько фото на объект), inline в админке
- [x] Отдача media в режиме разработки
- [x] Миниатюры: уменьшение фото при сохранении (оригинал ужимается до 1600 px, отдельные миниатюры не нужны)

## 4. Страницы и шаблоны, Bootstrap

- [x] Приложение `pages`, первая страница: view → url → template
- [x] Базовый шаблон `base.html`, наследование (`extends`, `block`)
- [x] Bootstrap 5 через CDN
- [x] Шапка и подвал
- [x] Главная: «Наши услуги» карточками (из БД, только активные)
- [x] Главная: блок «Кто мы»
- [x] Объекты карточками: первое фото, `prefetch_related`
- [x] Отзывы карточками
- [x] Статика: свой CSS, логотип (`STATIC`, `{% static %}`)

## 5. Форма заявки + уведомление в Telegram

- [x] `LeadForm` (`ModelForm`) в `leads/forms.py`
- [x] View заявки (`CreateView`): GET — пустая форма, POST — валидация, сохранение, redirect
- [x] Шаблон формы и URL `/lead/`: `{% csrf_token %}`, поля, ошибки
- [x] Bootstrap для полей формы (`widgets`), ссылка на форму в шапке
- [x] Сообщение «Заявка отправлена» (`messages`, `SuccessMessageMixin`)
- [x] Telegram-бот: токен и chat_id в `.env`
- [x] Отправка уведомления о новой заявке (`requests`), ошибка Telegram не ломает заявку

## 6. Тесты моделей и формы

- [x] Структура: `tests/` в приложениях, `test_*.py` по темам
- [x] Тесты формы `LeadForm`: валидный и невалидный телефон
- [x] Тесты `LeadCreateView`: GET, POST (сохраняет и redirect), невалидный телефон не сохраняется
- [x] Telegram выключен во всех тестах (`conftest.py`, autouse)
- [x] Тест Telegram через mock: сообщение уходит, сбой не ломает заявку
- [x] Тест главной: только активные услуги, объекты и отзывы

## 7. Docker + docker-compose + gunicorn + PostgreSQL

- [x] Docker Desktop установлен (`docker --version`, `docker compose version`)
- [x] `Dockerfile`: образ сайта (Python 3.12 + uv + зависимости + код)
- [x] `.dockerignore`: без `.venv`, `.env`, `db.sqlite3`, `media/`
- [x] gunicorn вместо `runserver` в контейнере
- [x] `docker-compose.yml`: `web` + `db` (PostgreSQL), volume для данных базы
- [x] Настройки базы из `.env` (`DATABASE_URL`), драйвер `psycopg`
- [x] `migrate` и `createsuperuser` в контейнере
- [x] Статика: `STATIC_ROOT`, `collectstatic`
- [x] nginx в compose: reverse proxy к gunicorn, отдача `/static/` и `/media/` (вместо whitenoise)
- [x] Media в volume
- [x] Тесты проходят на PostgreSQL

## 8. GitHub Actions (ruff + pytest на каждый пуш)

- [x] Workflow `.github/workflows/ci.yml`: запуск на push и pull request
- [x] Job: checkout, uv, Python 3.12, `uv sync --locked`
- [x] `ruff check` и `ruff format --check`
- [ ] `pytest` на PostgreSQL (service container)
- [ ] Зелёная галочка в PR, бейдж CI в README

## 9. VPS: деплой, HTTPS, домен

- [ ] Тот же compose на сервере, HTTPS (Let's Encrypt) в конфиге nginx

## 10. Потом: немного JS (галерея), SEO-основы

- [ ] Отдельная страница объекта (`/projects/<id>/`, `get_object_or_404`) и галерея всех фото
- [ ] Кнопка «Скопировать» для почты в подвале
- [ ] Дизайн: доработать CSS

## Следующий проект: сайт многофункционального здания (фулстек)

- [ ] Начать после выпуска ССК (этапы 1-10)
- [ ] Стек: Django + DRF (API) + Next.js (SSR), всё в одном docker-compose
- [ ] Идеи: арендаторы, помещения, фильтры, карта этажей, возможно бронирование
