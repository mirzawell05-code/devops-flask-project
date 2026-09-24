# ==========================================
# Stage 1: Сборка зависимостей (Builder)
# ==========================================
FROM python:3.12-slim AS builder

WORKDIR /app

# Отключаем генерацию .pyc и включаем небуферизованный вывод логов
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Устанавливаем зависимости в изолированную директорию
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# ==========================================
# Stage 2: Финальный минималистичный образ
# ==========================================
FROM python:3.12-slim AS runner

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Копируем только установленные библиотеки из этапа builder
COPY --from=builder /install /usr/local

# Создаем непривилегированного пользователя appuser
RUN adduser --disabled-password --gecos "" appuser && \
    chown -R appuser:appuser /app

# Копируем исходный код
COPY --chown=appuser:appuser . .

# Переключаемся на безопасного пользователя
USER appuser

EXPOSE 5000

# Для Production запуск через Gunicorn (если добавлен в requirements.txt) 
# или оставляем python app.py для локального теста:
CMD ["python", "app.py"]