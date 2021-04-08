from socket import socket, timeout, AF_INET, SOCK_DGRAM
import pickle 

sock = socket(AF_INET,SOCK_DGRAM)
sock.settimeout(3)

oslotemps = []
bergentemps = []
karmøytemps = []



def oslo(x=''):
    text = f"oslo {x}"
    sock.sendto(text.encode(),("localhost",2222))

    while True:
            try:
                data = sock.recv(2048)
                d = pickle.loads(data)
                oslotemps.append(d)
            except timeout:
                break
            except:
                print("this local server is down!")
                break
# oslo()

def bergen():
    text = 'bergen'
    sock.sendto(text.encode(),("localhost",4444))

    while True:
            try:
                data = sock.recv(2048)
                d = pickle.loads(data)
                bergentemps.append(d)
            except timeout:
                break
            except:
                print("this local server is down!")
                break
# bergen()


def karmøy():
    text = 'karmøy'
    sock.sendto(text.encode(),("localhost",4444))
    
    while True:
            try:
                data = sock.recv(2048)
                d = pickle.loads(data)
                karmøytemps.append(d)
            except timeout:
                break
            except:
                print("this local server is down!")
                break
# karmøy()



# print(oslotemps)
# print(avg_temp(oslotemps))