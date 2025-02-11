# Використовуємо офіційний Python 3.12 як базовий образ
FROM python:3.12

# Встановлюємо необхідні пакети для обробки аудіо
RUN apt-get update && apt-get install -y ffmpeg sox libsndfile1 && rm -rf /var/lib/apt/lists/*

# Встановлюємо робочу директорію
WORKDIR /app

# Копіюємо файл із залежностями окремо (щоб кеш не перезаписувався)
COPY dependencies.txt /app/

# Встановлюємо залежності
RUN pip install --no-cache-dir -r dependencies.txt

# Копіюємо весь проєкт у контейнер
COPY . /app

# Вказуємо, що main.py буде запускатися за замовчуванням
# CMD ["python", "main.py"]
