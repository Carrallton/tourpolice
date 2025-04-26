FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt&& \
    pip install gunicorn  # Явно устанавливаем gunicorn
COPY . .
CMD ["gunicorn", " app.wsgi:application", "--bind", "0.0.0.0:8000"]