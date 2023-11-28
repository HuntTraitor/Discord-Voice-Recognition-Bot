import wave
import io

#Have to convert audio to wav for transcription API
def convert_audio(data):
    try:
        wav_buffer = io.BytesIO()
        with wave.open(wav_buffer, 'wb') as wav_file:
            wav_file.setnchannels(2)
            wav_file.setsampwidth(2)
            wav_file.setframerate(48000)
            wav_file.writeframes(data)
        return wav_buffer
    except Exception as e:
        print(f"Error while converting to WAV: {e}")