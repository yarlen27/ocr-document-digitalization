# OCR Document Digitalization (Dockerized)

Este proyecto aplica OCR a documentos PDF escaneados (sin capa de texto) usando [OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF) dentro de un contenedor Docker. El resultado es un nuevo PDF con capa de texto incrustada, listo para ser indexado por herramientas como SharePoint.

---

## 🚀 Flujo del proceso

1. Coloca los archivos PDF sin OCR en la carpeta `input/`
2. Ejecuta el contenedor con Docker
3. Los archivos procesados con OCR se guardarán en `output/`

---

## 🐳 Cómo usar

### 1. Construir el contenedor

```bash
docker build -t ocr-service ./docker
