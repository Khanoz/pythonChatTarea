import socket   
import threading

username = input("Enter your username: ")

host = '127.0.0.1'
port = 55555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))


def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')

            if message == "@username":
                client.send(username.encode("utf-8"))
            else:
                print(message)
        except:
            print("An error Ocurred")
            client.close
            break

def write_messages():
    while True:
        print("estoy corriendo y no se porque")
        messg = f"{input('')}"
        if len(messg) >= 7 and messg[:7].upper() == "PRIVATE":
            usr = str(input('Escriba el nombre del usuario: '))
            msg = str(input('Escriba el mensaje: '))
            message = f"PRIVATE{len(usr):03}{usr}{username} envio por mensaje privado: {msg}"
            print(message)
        else:
            message = f"{username}: {messg}"
            print("aca")
        client.send(message.encode('utf-8'))

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

write_thread = threading.Thread(target=write_messages)
write_thread.start()
