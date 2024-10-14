from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import os
import whisper
import pandas as pd
from transformers import pipeline

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = 'uploads'  
DATASET_FILE = 'transcriptions.csv'

# Asegúrate de que la carpeta de subida existe
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Asegúrate de que el archivo CSV existe
if not os.path.exists(DATASET_FILE):
    df = pd.DataFrame(columns=['id', 'filename', 'transcription', 'sentiment'])
    df.to_csv(DATASET_FILE, index=False)

# Cargar el modelo de Whisper
model = whisper.load_model("base")

# El modelo de análisis de sentimiento se utiliza en modo multilenguaje
sentiment_analysis = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

@app.post("/upload/")
async def upload_audio_file(file: UploadFile = File(...)):
    # Verifica si el archivo se recibió
    if not file:
        return {"error": "No se recibió ningún archivo"}

    # Guardar el archivo de audio en el servidor
    file_location = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_location, "wb+") as file_object:
        file_object.write(await file.read())

    # Transcribir el archivo de audio con Whisper
    result = model.transcribe(file_location)
    transcription_text = result['text']

    # Analizar el sentimiento de la transcripción
    sentiment_result = sentiment_analysis(transcription_text)[0]
    sentiment_label = sentiment_result['label']  # '1 star', '2 stars', ..., '5 stars'
    sentiment_score = sentiment_result['score']

    # Asignar sentimiento basado en la clasificación de estrellas del modelo original
    if sentiment_label == "5 stars":
        final_sentiment = "feliz"
    elif sentiment_label == "4 stars":
        final_sentiment = "contento"
    elif sentiment_label == "3 stars":
        # Agregar una lógica para detectar sorpresa, por ejemplo:
        if "¡" in transcription_text or "sorprendido" in transcription_text.lower():
            final_sentiment = "sorprendido"
        else:
            final_sentiment = "neutral"
    elif sentiment_label == "2 stars":
        final_sentiment = "triste"
    elif sentiment_label == "1 star":
        final_sentiment = "enojado"

    # Guardar la transcripción y el sentimiento en el archivo CSV
    df = pd.read_csv(DATASET_FILE)

    new_id = len(df) + 1
    new_entry = pd.DataFrame({
        'id': [new_id],
        'filename': [file.filename],
        'transcription': [transcription_text],
        'sentiment': f"{final_sentiment} ({sentiment_label})"
    })

    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv(DATASET_FILE, index=False)

    return {"transcription": transcription_text, "sentiment": final_sentiment}

@app.get("/transcriptions/")
async def get_transcriptions():
    df = pd.read_csv(DATASET_FILE)
    return df.to_dict(orient='records')
