import wave
import io

def convert_audio(data, channels, width, frame_rate):
    wav_buffer = io.BytesIO()
    with wave.open(wav_buffer, 'wb') as wave_file:
        wave_file.setnchannels(channels)
        wave_file.setsampwidth(width)
        wave_file.setframerate(frame_rate)
        wave_file.writeframes(data)
    wav_buffer.seek(0)
    return wav_buffer
