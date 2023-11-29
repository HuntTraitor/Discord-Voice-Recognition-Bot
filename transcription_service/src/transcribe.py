from openai import OpenAI
from config import OPENAI_API_KEY
import tempfile
from pathlib import Path
from .check_words import validTranscription

def transcribe(audio_file, username, filename):

    try:
        client = OpenAI(api_key=OPENAI_API_KEY)
    except Exception as e:
        print(f"Error: Invalid API KEY - {e}")
        exit()

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
        except Exception as e:
            print(f"Error during transcription API call: {e}")
        finally:
            temp_wav_path.unlink()

    with open(output_file, 'a+') as output_file:
        if validTranscription(transcription.text):
            output_file.write(f"{username}: {transcription.text}\n")