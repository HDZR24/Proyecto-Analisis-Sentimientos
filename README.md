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

## Instrucciones para la Instalación
## Instalación de Dependencias

### Requisitos Previos

Asegúrate de tener instalados los siguientes programas:

- **Python 3.8 o superior**: Verifica la versión instalada con:

    ```bash
    python --version
    ```

    Si no tienes Python, descárgalo desde [python.org](https://www.python.org/downloads/).

- **Node.js y npm**: Verifica si están instalados con:

    ```bash
    node --version
    npm --version
    ```

    Si no tienes Node.js, descárgalo desde [nodejs.org](https://nodejs.org/).

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

### Instalación de Dependencias del Frontend

1. **Navega a la carpeta del frontend**:

    ```bash
    cd ../frontend
    ```

2. **Si tienes un archivo `package.json`**, ejecuta el siguiente comando para instalar todas las dependencias listadas:

    ```bash
    npm install
    ```

   Si no tienes un archivo `package.json` y no necesitas bibliotecas adicionales, puedes omitir este paso.

### Resumen

- Asegúrate de tener Python y Node.js instalados.
- Clona el repositorio y navega a las carpetas correspondientes.
- Instala las dependencias del backend manualmente utilizando `pip`.
- Si es necesario, instala las dependencias del frontend utilizando `npm`.



