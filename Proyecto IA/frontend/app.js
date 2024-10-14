// Variables para la grabación
let mediaRecorder;
let audioChunks = [];

// Seleccionar botones y elementos para mostrar resultados
const recordBtn = document.getElementById('recordBtn');
const sendBtn = document.getElementById('sendBtn');
const sentimentResult = document.getElementById('sentimentResult');
const transcriptionResult = document.getElementById('transcriptionResult');
const transcriptionsList = document.getElementById('transcriptionsList'); // Elemento para mostrar transcripciones anteriores

// Función para cargar las transcripciones existentes
async function loadTranscriptions() {
    const response = await fetch('http://127.0.0.1:8000/transcriptions/');
    if (response.ok) {
        const transcriptions = await response.json();
        transcriptionsList.innerHTML = ''; // Limpiar la lista
        transcriptions.forEach(entry => {
            const listItem = document.createElement('li');
            listItem.textContent = `Transcripción: ${entry.transcription} - Sentimiento: ${entry.sentiment}`;
            transcriptionsList.appendChild(listItem);
        });
    } else {
        console.error('Error al cargar las transcripciones');
    }
}

// Llamar a la función al cargar la página
window.onload = loadTranscriptions;

// Configurar la grabación
recordBtn.addEventListener('click', async () => {
    if (!mediaRecorder || mediaRecorder.state === 'inactive') {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        mediaRecorder = new MediaRecorder(stream);

        mediaRecorder.ondataavailable = event => {
            audioChunks.push(event.data);
        };

        mediaRecorder.onstop = () => {
            sendBtn.disabled = false;
        };

        mediaRecorder.start();
        recordBtn.textContent = 'Detener';
    } else {
        mediaRecorder.stop();
        recordBtn.textContent = 'Grabar';
    }
});

sendBtn.addEventListener('click', async () => {
    const audioBlob = new Blob(audioChunks, { type: 'audio/mpeg' });
    const formData = new FormData();
    formData.append('file', audioBlob, 'grabacion.mp3');

    const response = await fetch('http://127.0.0.1:8000/upload/', {
        method: 'POST',
        body: formData,
    });

    if (response.ok) {
        alert('Grabación enviada con éxito');
        const data = await response.json();

        transcriptionResult.textContent = `Transcripción: ${data.transcription}`;
        sentimentResult.textContent = `Sentimiento: ${data.sentiment}`;
        
        // Recargar las transcripciones
        loadTranscriptions();
    } else {
        const errorText = await response.text();
        alert('Error al enviar la grabación: ' + errorText);
    }

    audioChunks = [];
    sendBtn.disabled = true;
});
