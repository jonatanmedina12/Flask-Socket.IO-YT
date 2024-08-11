from flask import render_template, request, Blueprint
from flask_socketio import emit
from pytube import YouTube
import urllib.parse
import urllib.request
import json
import re

from Descargar import socketio

yt_bp = Blueprint('youtube', __name__, url_prefix='/')


@yt_bp.route('/', methods=['GET', 'POST'])
def youtube_downloader():
    return render_template('index.html')


def extract_video_id(url):
    query = urllib.parse.urlparse(url).query
    params = urllib.parse.parse_qs(query)
    return params.get('v', [None])[0]


def get_video_info(video_id):
    url = f"https://www.youtube.com/watch?v={video_id}"
    html = urllib.request.urlopen(url).read().decode()
    video_info = re.search(r"var ytInitialPlayerResponse\s*=\s*({.*?});", html).group(1)
    video_info = json.loads(video_info)
    return video_info['videoDetails']


@socketio.on('start_download')
def handle_download(data):
    url = data['url']
    try:
        video_id = extract_video_id(url)
        if not video_id:
            raise ValueError("No se pudo extraer el ID del video de la URL proporcionada.")

        # Obtener información del video sin usar pytube
        video_info = get_video_info(video_id)

        emit('video_info', {
            'title': video_info['title'],
            'author': video_info['author'],
            'length': int(video_info['lengthSeconds']),
            'views': video_info['viewCount']
        })

        # Simular progreso de descarga
        for i in range(0, 101, 10):
            socketio.sleep(1)
            emit('download_progress', {'progress': i})

        # Aquí normalmente descargarías el video
        # Pero como no podemos usar pytube, necesitarías implementar tu propia lógica de descarga

        emit('download_complete', {
            'message': 'Información del video obtenida con éxito. La descarga real no está implementada en esta versión.'})
    except ValueError as e:
        emit('download_error', {'error': str(e)})
    except Exception as e:
        emit('download_error', {'error': f"Error inesperado: {str(e)}"})