import socket
import wave
import threading
import sys
from transcribe import transcribe
import io
from transformers import pipeline

PORT = 8010
IP = socket.gethostbyname(socket.gethostname())
ADDR = (IP, PORT)

# preload the pipeline
device = "cpu"

pipe = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-small",
    chunk_length_s=30,
    device=device
)

width = 2
channels = 2
frame_rate = 48000

def handle_client(client_socket):

    # first packet you recieve should be the username packet according to TCP
    # This packet has a custom header with the first 4 bytes explaining the username
    header = client_socket.recv(4)
    header_length = int.from_bytes(header, byteorder='little')
    encoded_username = client_socket.recv(header_length)
    username = encoded_username.decode('utf-8')

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

    wav_buffer = io.BytesIO()
    with wave.open(wav_buffer, 'wb') as wave_file:
        wave_file.setnchannels(channels)
        wave_file.setsampwidth(width)
        wave_file.setframerate(frame_rate)
        wave_file.writeframes(data)

    wav_data = wav_buffer.getvalue()
    print("starting transcription...")
    transcribe(pipe, wav_data, username)
    print("closed connection")

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(ADDR)
    server_socket.listen(5)

    print(f"Audio is now listening for connections... on {ADDR}")

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
        sys.exit(0)

if __name__ == '__main__':
    main()


