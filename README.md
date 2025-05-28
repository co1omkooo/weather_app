# Прогноз погоды — Django + Open-Meteo API

Веб-приложение на Django, где пользователь вводит название города и получает почасовой прогноз погоды на ближайшее время. Проект использует бесплатное API от [open-meteo.com](https://open-meteo.com/).

---

## Что реализовано

- Поиск прогноза по названию города
- Геокодинг через Open-Meteo Geocoding API
- Таблица с температурой и осадками на каждый час
- Автозаполнение города (autocomplete) с подсказками
- Красивый и адаптивный интерфейс на Bootstrap
- Контейнеризация проекта с Docker

---

## Технологии

- Python 3.9
- Django 3.x
- Bootstrap 5
- jQuery UI (для автодополнения)
- Open-Meteo API (для прогноза и геокодинга)
- Docker + Docker Compose

---

## Установка и запуск (через Docker)

> Убедитесь, что установлены Docker и docker-compose.

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/co1omkooo/weather-app.git
cd weather-app
```

### 2. Соберите и запустите контейнер

```bash
docker-compose up --build
```

> Приложение будет доступно по адресу http://localhost:8000