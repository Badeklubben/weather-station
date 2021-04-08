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
weatherData = ["",0,"",0,0]

# Instantiate a station simulator
local_station = StationSimulator(simulation_interval=1,location="Bergen")
# Turn on the simulator
local_station.turn_on()
dayOfMonth = 0

while True:
    # Sleep for 1 second to wait for new weather data
    # to be simulated
    sleep(1)

    if(local_station._hour == 0 or dayOfMonth == 0):
        dayOfMonth += 1

    if dayOfMonth > local_station._days_of_month[local_station.month]:
        print("The end is nigh!")
        break

    weatherData[0] = local_station.location
    weatherData[1] = dayOfMonth
    weatherData[2] = local_station.month
    weatherData[3] = local_station.temperature
    weatherData[4] = local_station.rain

    try:
        sock.sendall(pickle.dumps(weatherData))
    except:
        print(f"connection to server lost, terminating session")
        break


local_station.shut_down()


