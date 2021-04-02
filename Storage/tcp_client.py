from socket import create_connection
import pickle, sqlite3 as sl


###
# Storage TCP client
#   for reciving weather data and storing it in a local database 
# ###

print("--Storage TCP client--")
#create connection to server
try:
    sock = create_connection(("localhost", 5555))
except:
    print("Server down!")
    exit()


#connect to local database
slConn = sl.connect("weather-data.db")
sql = "INSERT INTO WEATHER (location,month,temperature,rain) values(?,?,?,?)"

while True:
    #recive and decrypt
    response = sock.recv(2048)
    print("recieving...")
    try:
        data = pickle.loads(response)
    except:
        print("Server down!")
        break

    #add data to table
    slConn.execute(sql,data)
    slConn.commit()

slConn.close()


