        var socket = io();

        document.getElementById('download-form').onsubmit = function(e) {
            e.preventDefault();
            var url = document.getElementById('url').value;
            socket.emit('start_download', {url: url});
            document.getElementById('info-message').innerHTML = 'Procesando URL...';
            document.getElementById('progress-bar').style.display = 'none';
            document.getElementById('download-status').innerHTML = '';
            document.getElementById('error-message').innerHTML = '';
            document.getElementById('video-info').innerHTML = '';
        };

        socket.on('video_info', function(data) {
            document.getElementById('info-message').innerHTML = 'Información del video obtenida. Iniciando descarga...';
            var infoHtml = `
                <h2>${data.title}</h2>
                <p>Autor: ${data.author}</p>
                <p>Duración: ${Math.floor(data.length / 60)}:${data.length % 60} minutos</p>
                <p>Vistas: ${data.views}</p>
            `;
            document.getElementById('video-info').innerHTML = infoHtml;
            document.getElementById('progress-bar').style.display = 'block';
        });

        socket.on('download_progress', function(data) {
            var progressBar = document.getElementById('progress');
            progressBar.style.width = data.progress + '%';
            progressBar.innerHTML = data.progress + '%';
        });

        socket.on('download_complete', function(data) {
            document.getElementById('download-status').innerHTML = data.message;
            document.getElementById('info-message').innerHTML = '';
        });

        socket.on('download_error', function(data) {
            document.getElementById('error-message').innerHTML = data.error;
            document.getElementById('progress-bar').style.display = 'none';
            document.getElementById('download-status').innerHTML = '';
            document.getElementById('info-message').innerHTML = '';
        });