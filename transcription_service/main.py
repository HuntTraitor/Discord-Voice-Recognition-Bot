import socket
import threading
import sys
import warnings
import torch
import wave
import io
from config import ADDR
from transformers import pipeline
from src.transcribe import transcribe
from src.convert_to_wav import convert_audio

warnings.filterwarnings("ignore", category=UserWarning, module="transformers")

try:
    num_gpus = torch.cuda.device_count()
    for i in range(torch.cuda.device_count()):
        gpu_names = [(f"cuda:{i}", torch.cuda.get_device_name(i))]
    print("Available GPU(s):", gpu_names)
    device = gpu_names[0][0]
except:
    print("ERROR: cuda not available")

device = device
pipe = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-large",
    chunk_length_s=30,
    device = device
)

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
    finally:
        client_socket.close()

    wav_data = convert_audio(data)
    transcribe(pipe, wav_data, username, filename)


def main():

    # main thread
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(ADDR)
        server_socket.listen(5)
        print(f"Audio is now listening for connections... on {ADDR}")

    # Waiting for a audio stream from discord_bot and send over to handle_client thread
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Accepted connection from {client_address}")
            client_handler = threading.Thread(target=handle_client, args=(client_socket,))
            client_handler.daemon = True
            client_handler.start()
    except KeyboardInterrupt:
        print("Exiting...")
        server_socket.close()
        sys.exit(0)

if __name__ == '__main__':
    main()


