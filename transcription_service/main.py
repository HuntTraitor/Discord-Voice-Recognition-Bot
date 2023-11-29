import socket
import threading
import sys
from config import ADDR
from src.transcribe import transcribe
from src.convert_to_wav import convert_audio

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

    audio_file = convert_audio(data)
    transcribe(audio_file, username, filename)


def main():

    # main thread
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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


