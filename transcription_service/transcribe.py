from openai import OpenAI
import io
import os

OPENAI_API_KEY = os.getenv('OPEN_API_KEY')
client = OpenAI(api_key=OPENAI_API_KEY)

def transcribe(audio_data, username, filename, timestamps):
    wav_buffer = io.BytesIO(audio_data)
    output_file = f"transcriptions/{filename}.txt"
    transcription = client.audio.transcriptions.create(
        model = "whisper-1",
        file = audio_data
    )
    print(transcription)

    # with open(output_file, 'a+') as output_file:
    #     output_file.write(f"{timestamps[0]} - {username}: {transcription['data'][0]['text']} = {timestamps[1]}\n")
    