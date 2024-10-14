# Grabador de Audio y Análisis de Sentimiento

Este proyecto es una aplicación web que permite a los usuarios grabar audio, transcribirlo y analizar el sentimiento de las transcripciones utilizando modelos de aprendizaje automático. La aplicación utiliza FastAPI en el backend y JavaScript en el frontend.

## Características

- **Grabación de audio**: Los usuarios pueden grabar su voz y enviar la grabación al servidor.
- **Transcripción automática**: Utiliza el modelo Whisper para transcribir el audio grabado.
- **Análisis de sentimiento**: Emplea un modelo de análisis de sentimientos multilingüe para clasificar el tono emocional de la transcripción en categorías como feliz, contento, sorprendido, neutral, triste y enojado.
- **Interfaz de usuario simple**: Una interfaz limpia y fácil de usar para interactuar con las funcionalidades.

## Modelos Utilizados

### Whisper
Whisper es un modelo de transcripción de audio que permite convertir el habla en texto de manera eficiente y precisa. Este modelo es capaz de manejar varios idiomas y diferentes acentos.

### Análisis de Sentimiento
Se utiliza el modelo `nlptown/bert-base-multilingual-uncased-sentiment`, que clasifica el sentimiento en una escala de 1 a 5 estrellas. Las etiquetas de sentimiento se interpretan como:

- **5 estrellas**: feliz
- **4 estrellas**: contento
- **3 estrellas**: neutral/sorprendido (con detección de ciertas palabras)
- **2 estrellas**: triste
- **1 estrella**: enojado

Cabe resaltar que se trata de un modelo multilingüe y que detecta normalmente el español
## Instalación de Dependencias

### Requisitos Previos

Asegúrate de tener instalados los siguientes programas:

- **Python 3.8 o superior**: Verifica la versión instalada con:

    ```bash
    python --version
    ```

    Si no tienes Python, descárgalo desde [python.org](https://www.python.org/downloads/).

### Instalación de Dependencias del Backend

1. **Clona el repositorio** (si aún no lo has hecho):

    ```bash
    git clone https://github.com/tu-usuario/proyecto-grabacion-audio.git
    cd proyecto-grabacion-audio
    ```

2. **Navega a la carpeta del backend**:

    ```bash
    cd backend
    ```

3. **Instala las dependencias necesarias manualmente** ejecutando los siguientes comandos:

    ```bash
    pip install fastapi
    pip install uvicorn
    pip install git+https://github.com/openai/whisper.git
    pip install transformers
    pip install pandas
    ```

### Ejecutar el Frontend

1. **Navega a la carpeta del frontend**:

    ```bash
    cd ../frontend
    ```

2. **Abre el archivo `index.html` en tu navegador**:


### Opción 1: Usar el Explorador de Archivos
1. Navega a la carpeta `frontend` donde se encuentra el archivo `index.html`.
2. Haz doble clic en el archivo `index.html`. Esto abrirá el archivo en tu navegador predeterminado.

### Opción 2: Usar la línea de comandos
1. Abre el símbolo del sistema (CMD).
2. Navega a la carpeta `frontend` utilizando el comando `cd`. Por ejemplo:
   ```bash
   cd C:\ruta\al\proyecto\frontend
   ```
   
## Uso

1. **Presiona el botón Grabar** para iniciar la grabación de tu voz.
2. **Una vez finalizada, presiona Detener.**
3. **Haz clic en Enviar** para cargar la grabación al servidor.
4. **El resultado mostrará** la transcripción del audio y el sentimiento detectado.
5. **El histórico de transcripciones** también será visible en la parte inferior.

## Escalabilidad del modelo de sentimientos

En esta implementación, el modelo de análisis de sentimientos se basa en el modelo `nlptown/bert-base-multilingual-uncased-sentiment` de Hugging Face, que fue entrenado para clasificar opiniones con un sistema de "estrellas" de 1 a 5. Cada número de estrellas en el modelo original refleja una emoción como sigue:

- **1 estrella**: Muy negativo
- **2 estrellas**: Negativo
- **3 estrellas**: Neutral
- **4 estrellas**: Positivo
- **5 estrellas**: Muy positivo

### Adaptación del modelo original

En esta versión del proyecto, hemos adaptado los resultados para que los sentimientos sean más específicos:

- **5 estrellas**: Feliz
- **4 estrellas**: Contento
- **3 estrellas**: Neutral o Sorprendido (dependiendo de palabras clave como "sorprendido" o signos de exclamación).
- **2 estrellas**: Triste
- **1 estrella**: Enojado

### Sentimiento de "Sorprendido"

El sentimiento de sorprendido fue añadido basándonos en características específicas del texto transcrito. Si la transcripción contiene ciertas palabras o signos de exclamación, se clasifica como sorprendido. Esto permite identificar situaciones en las que el usuario expresa una emoción de sorpresa, lo que no está presente en el modelo original de estrellas.


