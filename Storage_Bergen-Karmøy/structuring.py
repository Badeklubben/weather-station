
def avg_temp(locationData):
    temps = {}
    preps = {}

    for item in locationData:
        if not item[2] in temps.keys():
            temps[item[2]] = [0,0]
            preps[item[2]] = [0,0]
        temps[item[2]][0] += item[4]
        preps[item[2]][0] += item[5]
        temps[item[2]][1] += 1
        preps[item[2]][1] += 1
    
    snitt = []
    for key in temps.keys():
        snitt.append([None,item[1], key, item[3], round(temps[key][0]/temps[key][1],2), round(preps[key][0]/preps[key][1],2)])
    
    return snitt
