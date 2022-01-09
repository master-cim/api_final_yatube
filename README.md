# Название проекта 
## «API для Yatube»
api final
# Описание
## API для всех моделей приложения Yatube
Возможности приложения:
- Выдача списка всех публикаций. _При указании параметров limit и offset выдача  результата с пагинацией._
- Добавление новой публикации в коллекцию публикаций. _Анонимные запросы запрещены._
- Выдача публикации по id.
- Обновление публикации по id. _Обновить публикацию может только автор публикации. Анонимные запросы запрещены._
- Частичное обновление публикации по id. _Обновить публикацию может только автор публикации. Анонимные запросы запрещены._
- Удаление публикации по id. _Удалить публикацию может только автор публикации. Анонимные запросы запрещены._
- Выдача всех комментариев к публикации.
- Добавление нового комментария к публикации. _Анонимные запросы запрещены._
- Получение комментария к публикации по id.
- Обновление комментария к публикации по id. _Обновить комментарий может только автор комментария. Анонимные запросы запрещены._
- Частичное обновление комментария к публикации по id. _Обновить комментарий может только автор комментария. Анонимные запросы запрещены._
- Удаление комментария к публикации по id. _Обновить комментарий может только автор комментария. Анонимные запросы запрещены._
- Выдача списка доступных сообществ.
- Выдача информации о сообществе по id.
- Выдача всех подписок пользователя, сделавшего запрос. _Анонимные запросы запрещены._
- Подписка пользователя от имени которого сделан запрос на пользователя переданного в теле запроса. _Анонимные запросы запрещены._
- Выдача JWT-токена.
- Обновление JWT-токена.
- Проверка JWT-токена.
# Технологии в проекте
- Django REST Framework
- Python
# Инструкции по запуску
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/master-cim/api_final_yatube.git
```

```
cd api_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/bin/activate
```
Обновить версию pip
```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```
# Примеры
Получение публикаций
'GET'
```
 /api/v1/posts/
```
:white_check_mark: Создание публикации
```
**POST** /api/v1/posts/

{
"text": "string",
"image": "string",
"group": 0
}
```
Получение, Обновление,  Частичное обновление, Удаление публикации по id.
```
GET, PUT, PATCH, DELETE /api/v1/posts/{id}/
{
"text": "string",
"image": "string",
"group": 0
}
```
Получение всех комментариев к публикации.
```
GET /api/v1/posts/{post_id}/comments/
```
Добавление нового комментария к публикации.
```
POST /api/v1/posts/{post_id}/comments/
{
"text": "string"
}
```
Получение, Обновление, Частичное обновление, Удаление  комментария к публикации по id.
```
'GET, POST, PATCH, DELETE' /api/v1/posts/{post_id}/comments/{id}/
{
"text": "string"
}
```
Получение списка доступных сообществ.
```
GET /api/v1/groups/
```
Получение информации о сообществе по id.
```
GET /api/v1/groups/{id}/
```
Получить Все подписки пользователя
```
GET /api/v1/follow/

```
Подписка пользователя от имени которого сделан запрос на пользователя переданного в теле запроса.
```
POST /api/v1/follow/
{
"following": "string"
}
```
Получение JWT-токена.
```
POST /api/v1/jwt/create/
{
"username": "string",
"password": "string"
}
```
Обновление JWT-токена.
```
POST /api/v1/jwt/refresh/
{
"refresh": "string"
}
```
Проверка JWT-токена.
```
POST /api/v1/jwt/verify/
{
"token": "string"
}
```
# Автор
_Светлана Юревна Петрова_
_(Svetlana Yu. Petrova)_

