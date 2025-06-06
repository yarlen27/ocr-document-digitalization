FROM python:3.11-slim

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    ghostscript \
    qpdf \
    unpaper \
    libjpeg-dev \
    libpng-dev \ 
    pngquant \ 
    && pip install --no-cache-dir "ocrmypdf==13.7.0" "pikepdf==6.2.3"


# Crear directorios de trabajo
WORKDIR /app

# Copiar carpetas necesarias al contenedor
COPY src/ ./src
COPY input/ ./input
COPY output/ ./output

# Ejecutar el script
CMD ["python", "src/ocr_processor.py"]
