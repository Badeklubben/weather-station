import subprocess,sys
from time import sleep

s0 = "Storage_Bergen-Karmøy"
s1 = "Storage_Oslo"
w = ["Weather_Station_Bergen","Weather_Station_Karmøy","Weather_Station_Oslo"]


servers = [f"{s0}/tcp_server.py",f"{s0}/udp_server.py",
        f"{s1}/tcp_server.py",f"{s1}/udp_server.py"]

weather_stations = [f"{w[0]}/tcp_client.py",f"{w[1]}/tcp_client.py",f"{w[2]}/tcp_client.py"]

os = sys.platform
if os == "linux":
    os_open = "gnome-terminal --"
else:
    os_open = "start /wait"

serv_comm = ""
for i,fil in enumerate(servers):
    serv_comm += f"{os_open} python3 {fil}"
    if(i < len(servers)-1):
        serv_comm += " & "

cli_comm = ""
for i,fil in enumerate(weather_stations):
    cli_comm += f"{os_open} python3 {fil}"
    if(i < len(weather_stations)-1):
        cli_comm += " & "


subprocess.run(serv_comm,shell = True)
print("Servers_running..")
sleep(3)
subprocess.run(cli_comm,shell = True)
print("Weather_Stations_Running..")
sleep(2)
subprocess.run(f"{os_open} python3 FMI/udp_client.py",shell = True)