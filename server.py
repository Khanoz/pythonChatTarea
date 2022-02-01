import socket   
import threading


host = '127.0.0.1'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((host, port))
server.listen()
print(f"Server running on {host}:{port}")


clients = []
usernames = []

def broadcast(message, _client):
    for client in clients:
        if client != _client:
            client.send(message)

def sendPrivateMessage(message, client):
    pass

def handle_messages(client):
    while True:
        try:
            print(clients[0])
            print(type(clients[0]))
            message = client.recv(1024)
            massage = str(message.decode("utf-8"))
            print("El mensaje")
            print(massage)
            print(type(massage))
            if massage[:7] == "PRIVATE":
                #7 tamaño de PRIVATE + 3 digitos forzados al len  = 10 luego quitamos los primeros 7
                sizeOfUsr = int((massage[:10])[7:])
                clientToSend = (massage[:10+sizeOfUsr])[10:]
                print(clientToSend)
                print(sizeOfUsr)
                index = usernames.index(clientToSend)
                msg = massage[10+sizeOfUsr:]
                try:
                    index = usernames.index(clientToSend)
                    msg = massage[10+sizeOfUsr:]
                    print(msg)
                except:
                    sendPrivateMessage(f"usuario: incorrecto".encode('utf-8'), client) 
            print("se envio")
            broadcast(message, client)
        except:
            index = clients.index(client)
            username = usernames[index]
            broadcast(f"ChatBot: {username} disconnected".encode('utf-8'), client)
            clients.remove(client)
            usernames.remove(username)
            client.close()
            break


def receive_connections():
    while True:
        client, address = server.accept()

        client.send("@username".encode("utf-8"))
        username = client.recv(1024).decode('utf-8')

        clients.append(client)
        usernames.append(username)

        print(f"{username} is connected with {str(address)}")

        message = f"ChatBot: {username} joined the chat!".encode("utf-8")
        broadcast(message, client)
        client.send("Connected to server".encode("utf-8"))

        thread = threading.Thread(target=handle_messages, args=(client,))
        thread.start()

receive_connections()

