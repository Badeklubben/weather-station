from station import StationSimulator
from socket import create_connection
import pickle, sqlite3 as sl
from time import sleep


###
# Weather station TCP client
#   for transmitting of data to external storage 
# ###

print("--Weather station TCP client--")
#create connection to server
try:
    sock = create_connection(("localhost", 5555))
except:
    print("Server down!")
    exit()


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

    sock.sendall(pickle.dumps(weatherData))


bergen_station.shut_down()


