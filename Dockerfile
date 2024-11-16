FROM python:3.9

WORKDIR /app

# Сначала копируем файл зависимостей
COPY req.txt /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r req.txt

# Копируем весь проект в контейнер
COPY . /app

CMD ["python", "main.py"]