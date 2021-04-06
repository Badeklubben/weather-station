from socket import socket,timeout,AF_INET,SOCK_DGRAM
import pickle

#set up client with timeout
sock = socket(AF_INET,SOCK_DGRAM)
sock.settimeout(3)

print("Welcome to FMI!")

while (text:=input("> ").lower()) != "quit":
    #seperate between different commands

    #storage 0 and 1
    if(text in ("bergen","karmøy")):     
        sock.sendto(text.encode(),("localhost",4444))

    
    elif(text == "oslo"):
        sock.sendto(text.encode(),("localhost",2222))

    
    elif text == "help":
        print("Enter location name!")
        continue
    else:
        print("unknown command! (help)")
        continue

    print("Location\tmonth\ttemperature\train")
    #loop as long as the client is recieving data
    while True:
        try:
            data = sock.recv(2048)
            d = pickle.loads(data)
            print(f"{d[1]}\t\t{d[2]}\t{d[3]}\t\t{d[4]}")
        except timeout:
            break
        except:
            print("this local server is down!")
            break



print("Thank you for using FMI!\nWelcome back")
    