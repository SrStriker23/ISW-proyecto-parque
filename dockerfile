# Imagen base
FROM python:3.12-slim

# Evita que Python genere archivos .pyc
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Directorio de la app
WORKDIR /app

# Instalar dependencias
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el proyecto
COPY . /app/

# Exponer el puerto
EXPOSE 8000

# Comando por defecto
CMD ["gunicorn", "Proyecto.wsgi:application", "-b", "0.0.0.0:8000"]

