# API YaTube

API для проекта социальной сети YaTube. Реализован на bootcamp Yandex.Practicum.

## Особенности / Features

- Получение списка публикаций и конкретного поста
- Создание новых записей и комментариев, а также их обновление и удаление
- Получение информации о доступных сообществах
- Подписки на авторов и сообщества
- Аутентификация по токену JWT

## Стек технологий / Tech

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST framework](https://www.django-rest-framework.org/)
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/) - a JSON Web Token authentication backend for the Django REST Framework
- [PyJWT](https://pyjwt.readthedocs.io/) - a Python library which allows you to encode and decode JSON Web Tokens (JWT)
- [requests 2.26.0](https://pypi.org/project/requests/2.6.0/) - an Apache2 Licensed HTTP library, written in Python, that allows you to send HTTP/1.1 requests easily

### Примеры эндпоинтов / Endpoints

Получить список всех публикаций (GET)
```
http://127.0.0.1:8000/api/v1/posts/
```
Создание новой публикации (POST)
```
http://127.0.0.1:8000/api/v1/posts/
```
Получение публикации по id (GET)
```
http://127.0.0.1:8000/api/v1/posts/{id}/
```
Обновление публикации по id (PUT)
```
http://127.0.0.1:8000/api/v1/posts/{id}/
```
Удаление публикации по id (DELETE)
```
http://127.0.0.1:8000/api/v1/posts/{id}/
```
Подробнее можно посмотреть в документации Redoc после старта сервера по адресу:
```
http://127.0.0.1:8000/redoc/
```

## Как запустить проект / Installation
Клонировать репозиторий на свой компьютер
```
git clone git@github.com:gplakhotnikov/PROJECT_NAME.git
```

Cоздать и активировать виртуальное окружение
```
python3 -m venv env
source env/bin/activate

```
Установить зависимости из файла requirements.txt
```
pip install -r requirements.txt
python3 -m pip install --upgrade pip
```
Выполнить миграции:
```
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```

## О разработчике / Development
Grigory Plakhotnikov
