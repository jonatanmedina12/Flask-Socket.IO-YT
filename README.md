# Descargador de YouTube con Flask y Socket.IO

Este proyecto es una aplicación web que permite a los usuarios descargar videos de YouTube utilizando Flask y Socket.IO para una experiencia en tiempo real.

## Características

- Interfaz web para ingresar URLs de YouTube
- Visualización de información del video (título, autor, duración, vistas)
- Simulación de progreso de descarga en tiempo real
- Manejo de errores para URLs inválidas o problemas de conexión

## Requisitos previos

- Python 3.7+
- pip

## Instalación

1. Clona este repositorio:
   ```
   git clone https://github.com/tu-usuario/youtube-downloader.git
   cd youtube-downloader
   ```

2. Crea un entorno virtual e actívalo:
   ```
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   ```

3. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

## Uso

1. Inicia la aplicación:
   ```
   python app.py
   ```

2. Abre tu navegador y ve a `http://localhost:5000`

3. Ingresa la URL de un video de YouTube y haz clic en "Descargar"

## Estructura del proyecto

```
youtube-downloader/
│
├── app.py
├── config.py
├── requirements.txt
├── YTDownloader/
│   ├── __init__.py
│   └── Controller/
│       └── youtubeController.py
└── templates/
    └── youtube.html
```

## Advertencia legal

Este proyecto es solo para fines educativos. Asegúrate de cumplir con los términos de servicio de YouTube y las leyes de derechos de autor aplicables al usar esta aplicación.

## Contribuir

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir cambios mayores antes de hacer un pull request.

## Licencia

[MIT](https://choosealicense.com/licenses/mit/)