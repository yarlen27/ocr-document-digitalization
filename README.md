# OCR Document Digitalization

Este proyecto aplica OCR a documentos PDF escaneados (sin capa de texto) usando Tesseract y OCRmyPDF, generando una nueva versión del archivo con capa de texto, lista para ser indexada (por ejemplo, en SharePoint).

## 🎯 Objetivos

- Aplicar OCR a archivos PDF sin capa de texto.
- Generar un nuevo PDF con la capa de texto incrustada.
- Facilitar un flujo automatizado para digitalización documental.

## 🔧 Tecnologías usadas

- Python 3.11
- Tesseract OCR
- OCRmyPDF
- Docker

## 📁 Estructura del proyecto


├── src/ # Código fuente principal
├── input/ # PDFs originales sin OCR
├── output/ # PDFs con OCR aplicado
├── docker/ # Dockerfile y scripts de despliegue
├── requirements.txt # Dependencias de Python
├── README.md # Este archivo
└── .gitignore



## ▶️ Cómo usar

1. Coloca los archivos PDF escaneados en `input/`.
2. Ejecuta el script o usa Docker.
3. Revisa los archivos con OCR en `output/`.

## 🐳 Docker (opcional)

```bash
docker build -t ocr-processor docker/
docker run --rm -v "$(pwd)/input:/app/input" -v "$(pwd)/output:/app/output" ocr-processor


---

### 📄 `.gitignore`
Guarda este contenido en `.gitignore`: