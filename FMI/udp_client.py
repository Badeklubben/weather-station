from socket import socket,timeout,AF_INET,SOCK_DGRAM
import pickle

#set up client with timeout
sock = socket(AF_INET,SOCK_DGRAM)
sock.settimeout(3)

print("Welcome to FMI!")

while (text:=input("> ").lower()) != "quit":
    #seperate between different commands
    if text in ("all","temp","rain","sd"):

        sock.sendto(text.encode(),("localhost",4444))

        if text == "sd":
            print("Server shut down")
            break

        print("Location\tmonth\ttemperature\train\t\tentry number")
        #loop as long as the client is recieving data
        while True:
            try:
                data = sock.recv(2048)
                d = pickle.loads(data)
                print(f"{d[1]}\t\t{d[2]}\t{d[3]}\t\t{d[4]}\t\t{d[0]}")
            except timeout:
                break

    elif text == "help":
        print("all\t\tall data sorted by time\ntemp\t\tall data sorted by temperature\nrain\t\tall data sorted by amount of rain\nsd\t\tshut down server")
    else:
        print("unknown command! (help)")



print("Thank you for using FMI!\nWelcome back")
    