# СанСтройКап — сайт строительной компании

![CI](https://github.com/GlebTrifonov/ssk-site/actions/workflows/ci.yml/badge.svg)

Сайт-визитка строительной компании из Гродно: услуги, выполненные объекты с фотогалереей, отзывы клиентов и форма заявки с уведомлением в Telegram.

## Возможности

- Услуги, объекты и отзывы управляются через админку Django, на сайте показываются только активные
- Галерея объекта: несколько фото, при загрузке уменьшаются до 1600 px
- Форма заявки с проверкой телефона
- Уведомление о новой заявке в Telegram; сбой Telegram не мешает сохранить заявку

## Стек

- **Backend:** Python 3.12, Django 5.2, PostgreSQL 17
- **Frontend:** шаблоны Django, Bootstrap 5
- **Инфраструктура:** Docker, docker-compose, gunicorn, nginx
- **Качество:** pytest + pytest-django, ruff, pre-commit, GitHub Actions (линтер и тесты на PostgreSQL при каждом пуше)
- **Зависимости:** uv

## Архитектура

```
браузер → nginx :80 ─┬─ /static/, /media/ → файлы из volume
                     └─ остальное → gunicorn → Django → PostgreSQL
```

## Запуск в Docker

Нужен только Docker.

```bash
git clone https://github.com/GlebTrifonov/ssk-site.git
cd ssk-site
cp .env.example .env
```

Заполните `.env`: `SECRET_KEY` и `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`. Переменные Telegram можно оставить пустыми — уведомления будут выключены.

```bash
docker compose up -d --build
docker compose exec web uv run --no-dev python manage.py migrate
docker compose exec web uv run --no-dev python manage.py createsuperuser
```

Сайт: http://localhost, админка: http://localhost/admin/

## Бэкап и восстановление базы

Вместо `<POSTGRES_USER>` и `<POSTGRES_DB>` — значения из `.env`. Дампы (`*.sql`) содержат персональные данные и в git не попадают.

Бэкап: дамп пишется внутри контейнера и копируется на компьютер.

```bash
docker compose exec db pg_dump -U <POSTGRES_USER> -d <POSTGRES_DB> -f /tmp/backup.sql
docker compose cp db:/tmp/backup.sql ./backup.sql
```

> В Windows PowerShell 5.1 не перенаправляйте вывод через `>`: файл сохранится в UTF-16, и восстановиться из него не получится.

Проверка восстановления в отдельную базу (основная не затрагивается):

```bash
docker compose exec db createdb -U <POSTGRES_USER> restore_test
docker compose exec db psql -U <POSTGRES_USER> -d restore_test -f /tmp/backup.sql
docker compose exec db psql -U <POSTGRES_USER> -d restore_test -c "select count(*) from services_service;"
docker compose exec db dropdb -U <POSTGRES_USER> restore_test
```

Если файла нет в контейнере, сначала скопируйте его: `docker compose cp ./backup.sql db:/tmp/backup.sql`.

## Локальная разработка

Нужен [uv](https://docs.astral.sh/uv/). Без `DATABASE_URL` используется SQLite.

```bash
uv sync
uv run pre-commit install    # ruff и pytest перед каждым коммитом
cp .env.example .env    # заполнить SECRET_KEY
uv run python manage.py migrate
uv run python manage.py createsuperuser
uv run python manage.py runserver
```

## Тесты и линтер

После `pre-commit install` проверки запускаются сами при каждом `git commit`; если что-то упало, коммит не создаётся. Вручную по всему проекту:

```bash
uv run pre-commit run --all-files
```

Или по отдельности:

```bash
uv run pytest
uv run ruff check .
uv run ruff format --check .
```
