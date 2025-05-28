# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы проекта
COPY . .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт (если потребуется)
EXPOSE 8000

# Запуск приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
