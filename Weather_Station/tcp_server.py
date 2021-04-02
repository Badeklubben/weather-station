from station import StationSimulator
from socket import create_server
from time import sleep
import pickle

###
# Weather station TCP server
#   for transmitting of data to external storage 
# ###
print(f"Weather station TCP server\n\twaiting for connection to storage...")
#create server and wait for connection
#no point in transmitting before the storage is connected
sock = create_server(("localhost", 5555))
conn, adress = sock.accept()
print(f"Connected to {adress}\nTransmitting data..")

# Temp,Rain,Loc,Month
weatherData = ["","",0,0]

# Instantiate a station simulator
bergen_station = StationSimulator(simulation_interval=1)
# Turn on the simulator
bergen_station.turn_on()

while True:
    # Sleep for 1 second to wait for new weather data
    # to be simulated
    sleep(1)

    weatherData[0] = bergen_station.location
    weatherData[1] = bergen_station.month
    weatherData[2] = bergen_station.temperature
    weatherData[3] = bergen_station.rain

    #wait for reconnect if the connection is broken
    try:
        conn.sendall(pickle.dumps(weatherData))
    except:
        print(f"Lost connection to storage\nTransmission seized")
        conn, adress = sock.accept()
        print(f"Connected to {adress}\nTransmitting data..")

bergen_station.shut_down()
