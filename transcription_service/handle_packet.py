import socket
import wave
import threading
import sys
from transcribe import transcribe
import io

PORT = 8010
IP = socket.gethostbyname(socket.gethostname())
ADDR = (IP, PORT)

width = 2
channels = 2
frame_rate = 48000

def handle_client(client_socket):
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
    transcribe(wav_data)
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


