Вот пример файла `README.md` для вашего проекта на GitHub:

```markdown
# testBrendwell

## Описание
**testBrendwell** — это Django-приложение для управления продуктами, включающее API для создания и отображения продуктов с использованием HTML и JavaScript на фронтенде. Оно позволяет пользователям добавлять новые продукты, просматривать список продуктов и проверять уникальность наименований продуктов.

## Установка и настройка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/CapitanGrant/testBrendwell.git
   cd testBrendwell
   ```

2. Создайте виртуальное окружение и активируйте его:

   ```bash
   python -m venv env
   source env/bin/activate  # для Linux/MacOS
   env\Scripts\activate  # для Windows
   ```

3. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

4. Выполните миграции базы данных:

   ```bash
   python manage.py migrate
   ```

5. Запустите локальный сервер:

   ```bash
   python manage.py runserver
   ```

6. Перейдите в браузере по адресу `http://localhost:8000/`, чтобы начать работу с приложением.

## Использование

### Добавление продуктов
Для добавления нового продукта на странице введите название, описание и цену продукта в соответствующие поля. Нажмите кнопку "Отправить". Валидация на клиентской и серверной стороне гарантирует, что цена будет положительным числом, а название продукта уникальным.

### Отображение всех продуктов
Нажмите кнопку "Показать все продукты", чтобы получить и отобразить список всех добавленных продуктов.

## Структура API

- `GET /get_products/` — возвращает список всех продуктов в формате JSON.
- `POST /add_products/` — добавляет новый продукт. Принимает данные через POST-запрос:
  - `name`: название продукта (должно быть уникальным)
  - `description`: описание продукта
  - `price`: цена продукта (должна быть положительным числом)

