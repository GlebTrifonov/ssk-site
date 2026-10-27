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
- [ ] Telegram-бот: токен и chat_id в `.env`
- [ ] Отправка уведомления о новой заявке (`requests`), ошибка Telegram не ломает заявку

## 6. Тесты моделей и формы

- [ ]

## 7. Docker + docker-compose + gunicorn + PostgreSQL

- [ ]

## 8. GitHub Actions (ruff + pytest на каждый пуш)

- [ ]

## 9. VPS: деплой, HTTPS, домен

- [ ]

## 10. Потом: немного JS (галерея), SEO-основы

- [ ] Отдельная страница объекта (`/projects/<id>/`, `get_object_or_404`) и галерея всех фото
- [ ] Кнопка «Скопировать» для почты в подвале
- [ ] Дизайн: доработать CSS

## Следующий проект: сайт многофункционального здания (фулстек)

- [ ] Начать после выпуска ССК (этапы 1-10)
- [ ] Стек: Django + DRF (API) + Next.js (SSR), всё в одном docker-compose
- [ ] Идеи: арендаторы, помещения, фильтры, карта этажей, возможно бронирование
