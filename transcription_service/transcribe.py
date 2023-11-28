from openai import OpenAI
import os
from dotenv import load_dotenv
import tempfile
from pathlib import Path

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

def transcribe(audio_file, username, filename, timestamps):
    output_file = f"transcriptions/{filename}"

    with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_wav_file:
        temp_wav_file.write(audio_file.getvalue())
        temp_wav_path = Path(temp_wav_file.name)
        temp_wav_file.close

        try:
            transcription = client.audio.transcriptions.create(
                model = "whisper-1",
                file = temp_wav_path
            )
        finally:
            temp_wav_path.unlink()

    with open(output_file, 'a+') as output_file:
        output_file.write(f"{timestamps[0]} - {username}: {transcription.text} - {timestamps[1]}\n")
    