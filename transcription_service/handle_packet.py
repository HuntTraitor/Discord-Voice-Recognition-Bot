import socket
import wave
import threading

PORT = 8090
IP = socket.gethostbyname(socket.gethostname())
ADDR = (IP, PORT)

width = 2
channels = 2
frame_rate = 48000

output_file = 'output.wav'

def handle_client(client_socket):
    data = b''
    try:
        while True:
            packet = client_socket.recv(1024)
            if not packet:
                break
            data += packet
            print(packet)
    except KeyboardInterrupt:
        pass
    client_socket.close()


    with wave.open(output_file, 'wb') as wave_file:
        wave_file.setnchannels(channels)
        wave_file.setsampwidth(width)
        wave_file.setframerate(frame_rate)
        wave_file.writeframes(data)

    print("closed connection")

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(ADDR)
    server_socket.listen(5)

    print(f"Audio is now listening for connections...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == '__main__':
    main()


