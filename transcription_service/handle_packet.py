import socket
import wave
import threading
import sys
from transcribe import transcribe
import io
from transformers import pipeline
from datetime import datetime
import torch
import warnings

# Ignore the efficiency warning, there is no way to fix it and it has no impact on performance
warnings.filterwarnings("ignore", category=UserWarning, module="transformers")

PORT = 8010
IP = socket.gethostbyname(socket.gethostname())
ADDR = (IP, PORT)

# Test to see if you are using a GPU for transcription
try:
    num_gpus = torch.cuda.device_count()
    for i in range(torch.cuda.device_count()):
        gpu_names = [(f"cuda:{i}", torch.cuda.get_device_name(i))]
    print("Available GPU(s):", gpu_names)
except:
    print("ERROR: CUDA not available")

# preload the pipeline
device = "cuda:0" # <- CHOOSE THIS VALUE FROM OUTPUT ABOVE
pipe = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-large",
    chunk_length_s=30,
    device=device
)
width = 2
channels = 2
frame_rate = 48000

# This is listening for a connection from the discord bot audio stream to handle
def handle_client(client_socket):
    # decode the username packet first and store in username
    username_header = client_socket.recv(4)
    username_length = int.from_bytes(username_header, byteorder='little')
    encoded_username = client_socket.recv(username_length)
    username = encoded_username.decode('utf-8')

    # decode the filname packet second and store in filename
    filename_header = client_socket.recv(4)
    filename_length = int.from_bytes(filename_header, byteorder='little')
    encoded_filename = client_socket.recv(filename_length)
    filename = encoded_filename.decode('utf-8')

    # Put audio packets together
    data = b''
    try:
        while True:
            packet = client_socket.recv(1024)
            if not packet:
                break
            data += packet
    except KeyboardInterrupt:
        pass
    client_socket.close()

    # convert to wav
    wav_buffer = io.BytesIO()
    with wave.open(wav_buffer, 'wb') as wave_file:
        wave_file.setnchannels(channels)
        wave_file.setsampwidth(width)
        wave_file.setframerate(frame_rate)
        wave_file.writeframes(data)
    wav_data = wav_buffer.getvalue()

    # Transcribe wav file
    print("starting transcription...")
    transcribe(pipe, wav_data, username, filename)
    print("closed connection")

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(ADDR)
    server_socket.listen(5)
    print(f"Audio is now listening for connections... on {ADDR}")

    # Waiting for a audio stream from discord_bot and send over to handle_client thread
    try:
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Accepted connection from {client_address}")
            client_handler = threading.Thread(target=handle_client, args=(client_socket,))
            client_handler.daemon = True
            client_handler.start()
    except KeyboardInterrupt:  
        print("Exiting...")
        server_socket.close()
    finally:
        warnings.resetwarnings()
        sys.exit(0)

if __name__ == '__main__':
    main()


