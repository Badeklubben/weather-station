from socket import socket, AF_INET, SOCK_DGRAM
import pickle,sqlite3 as sl

#set up server
sock = socket(AF_INET,SOCK_DGRAM)
sock.bind(("localhost",4444))

#connect to local database
slConn = sl.connect("weather-data.db")

print("Server up")

while True:
    msg,address = sock.recvfrom(2048)
    command = msg.decode().lower()
    if command == "sd":
        break
    elif command == "all":
        data = slConn.execute("SELECT * FROM WEATHER")
    elif command == "temp":
        data = slConn.execute("SELECT * FROM WEATHER ORDER BY temperature")
    elif command == "rain":
        data = slConn.execute("SELECT * FROM WEATHER ORDER BY rain")

    #send in small chunks
    print(f"Sending data to {address}")
    for row in data:
        sock.sendto(pickle.dumps(row),address)
    


print("Server down")
slConn.close()