# Proyecto-Analisis-Sentimientos
Proyecto creado con HTML,CSS, JavaScript, Python.
# Proyecto de Grabación de Audio y Análisis de Sentimientos

Este proyecto permite grabar audio desde el frontend, transcribirlo usando Whisper y realizar un análisis de sentimiento utilizando un modelo multilingüe en el backend.

## Características

- Grabación de audio en el navegador.
- Transcripción automática del audio con Whisper.
- Análisis de sentimiento utilizando un modelo multilingüe.
- Soporte para múltiples sentimientos: feliz, contento, neutral, triste, enojado y sorprendido.

## Instalación

### 1. Clonar el repositorio

cd backend
pip install -r requirements.txt


2. Instalar dependencias en el backend
Asegúrate de tener Python 3.8+ instalado. Luego, instala las dependencias del backend utilizando pip:

cd backend
pip install -r requirements.txt


Dependencias principales:

fastapi: Framework para construir la API backend.
whisper: Para la transcripción de audio.
transformers: Biblioteca que incluye el modelo de análisis de sentimientos.
pandas: Para manejar y guardar los datos de transcripciones.
3. Ejecutar el backend
Una vez instaladas las dependencias, puedes ejecutar el servidor de FastAPI:


uvicorn main:app --reload

El backend estará disponible en http://127.0.0.1:8000.

4. Ejecutar el frontend
Ve a la carpeta frontend y abre el archivo index.html en tu navegador:




Este archivo permite interactuar con la API del backend para grabar audio, enviar la grabación y ver los resultados del análisis de sentimientos.

Uso
Presiona el botón Grabar para iniciar la grabación de tu voz.
Una vez finalizada, presiona Detener.
Haz clic en Enviar para cargar la grabación al servidor.
El resultado mostrará la transcripción del audio y el sentimiento detectado.
El histórico de transcripciones también será visible en la parte inferior.
Escalabilidad del modelo de sentimientos
En esta implementación, el modelo de análisis de sentimientos se basa en el modelo nlptown/bert-base-multilingual-uncased-sentiment de Hugging Face, que fue entrenado para clasificar opiniones con un sistema de "estrellas" de 1 a 5. Cada número de estrellas en el modelo original refleja una emoción como sigue:

1 estrella: Muy negativo
2 estrellas: Negativo
3 estrellas: Neutral
4 estrellas: Positivo
5 estrellas: Muy positivo
Adaptación del modelo original
En esta versión del proyecto, hemos adaptado los resultados para que los sentimientos sean más específicos:

5 estrellas: Feliz
4 estrellas: Contento
3 estrellas: Neutral o Sorprendido (dependiendo de palabras clave como "sorprendido" o signos de exclamación).
2 estrellas: Triste
1 estrella: Enojado
Sentimiento de "Sorprendido"
El sentimiento de sorprendido fue añadido basándonos en características específicas del texto transcrito. Si la transcripción contiene ciertas palabras o signos de exclamación, se clasifica como sorprendido. Esto permite identificar situaciones en las que el usuario expresa una emoción de sorpresa, lo que no está presente en el modelo original de estrellas.

Consideraciones sobre la escalabilidad
El modelo original de análisis de sentimientos está limitado a cinco clasificaciones de "estrellas", pero puede ser escalado o ajustado con diferentes técnicas:

Ajuste fino (Fine-tuning): Se puede entrenar el modelo con un conjunto de datos específicos de más emociones (incluyendo sorpresa o miedo).
Post-procesamiento: Añadiendo reglas que interpreten patrones específicos en las transcripciones, como hicimos con "sorprendido".
Este tipo de adaptación asegura que el modelo sea flexible y pueda crecer a medida que se necesiten más matices emocionales.
