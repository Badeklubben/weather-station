from socket import create_server
from time import sleep
import pickle, sqlite3 as sl


###
# Storage TCP server
#   for tstoring data to local database 
# ###
print(f"Storage TCP server\n\twaiting for connection to weather station...")
#create server and wait for first connection

sock = create_server(("localhost", 5555))
conn, adress = sock.accept()
print(f"Connected to {adress}\nReciving data..")

# Temp,Rain,Loc,Month
weatherData = ["","",0,0]

#connect to local database
slConn = sl.connect("weather-data.db")
sql = "INSERT INTO WEATHER (location,month,temperature,rain) values(?,?,?,?)"

while True:
    #recive and decrypt
    response = conn.recv(2048)
    print("recieving...")
    try:
        data = pickle.loads(response)
        print(data)
    except:
        print("weather station error")
        break

    #add data to table
    slConn.execute(sql,data)
    slConn.commit()

slConn.close()