from socket import socket, AF_INET, SOCK_DGRAM
import pickle,sqlite3 as sl
import structuring as st


#set up server
sock = socket(AF_INET,SOCK_DGRAM)
sock.bind(("localhost",4444))

#connect to local database
slConn = sl.connect("weather-data.db")

print("Server up")

while True:
    msg,address = sock.recvfrom(2048)
    command = msg.decode().lower().capitalize()

    data = slConn.execute(f"SELECT * FROM WEATHER WHERE location = '{command}'")


    comm_div = command.split(" ")
    if len(comm_div) > 1:
        if isinstance(comm_div[1],int):
            day = int(comm_div[1])
            if day > 32:
                data = slConn.execute(f"SELECT * FROM WEATHER WHERE location = '{command}' and day = {day}")

    #data = st.avg_temp(data)
    #snitt = (plass,dag,månad,snitt_temp,snitt_regn)
    #data = (snitt,snitt,snitt,...)

    #send in small chunks
    print(f"Sending data to {address}")
    for row in data:
        sock.sendto(pickle.dumps(row),address)
    


print("Server down")
slConn.close()
