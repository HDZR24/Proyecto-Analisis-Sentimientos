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

**Clonar el repositorio**:
```
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_REPOSITORIO>
```



