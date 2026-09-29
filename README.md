# ГеоПроект - Сайт инженерных изысканий

Современный сайт для компании, предоставляющей услуги инженерных изысканий.

## Установка

1. Установите зависимости:
```bash
pip install -r requirements.txt
```

## Запуск

Локальный запуск для разработки:
```bash
python app.py
```

Сайт будет доступен по адресу: http://localhost:5000

## Запуск на хостинге

Для production используйте gunicorn:
```bash
gunicorn app:app --bind 0.0.0.0:8000
```

## Структура проекта

```
├── app.py              # Главный файл приложения
├── requirements.txt    # Зависимости Python
├── static/
│   ├── css/
│   │   └── style.css   # Стили
│   └── js/
│       └── main.js     # JavaScript
└── templates/          # HTML шаблоны
    ├── base.html
    ├── index.html
    ├── services.html
    ├── geodesy.html
    ├── geology.html
    ├── ecology.html
    ├── hydrology.html
    └── contacts.html
```

## Возможности

- Современный адаптивный дизайн
- Информация об услугах
- Форма обратной связи
- Простота и удобство использования
