FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
RUN useradd -u 10001 -m appuser
USER 10001
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
