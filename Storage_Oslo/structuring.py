
def avg_temp(locationData):
    dailySumTemp = 0
    dailyAverageTemp = 0

    dailySumPrep = 0
    dailyAveragePrep = 0
    hourCount = 0

    snitt = []
    for item in locationData:
        dailySumTemp += item[4]
        dailySumPrep += item[5]
        if hourCount == 23:
            dailyAverageTemp = dailySumTemp/24
            dailyAverageTemp = round(dailyAverageTemp, 2)
            
            dailyAveragePrep = dailySumPrep/24
            dailyAveragePrep = round(dailyAveragePrep, 2)

            snitt.append([None,item[1], item[2], item[3], dailyAverageTemp, dailyAveragePrep])

            hourCount = 0
        hourCount += 1

    return snitt
