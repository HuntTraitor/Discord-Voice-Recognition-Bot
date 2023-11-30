import wave
import io

#Have to convert audio to wav for transcription API
def convert_audio(data):
    wav_buffer = io.BytesIO()
    with wave.open(wav_buffer, 'wb') as wave_file:
        wave_file.setnchannels(2)
        wave_file.setsampwidth(2)
        wave_file.setframerate(48000)
        wave_file.writeframes(data)
    wav_data = wav_buffer.getvalue()
    return wav_data