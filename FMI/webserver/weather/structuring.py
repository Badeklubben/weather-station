# import weather as w

# def avg_temp(loc):
#     hrs_day = 0
#     dailySum = 0
#     days = []
#     w.karmøy()

#     for x in loc:
#         dailySum += x[2]
#         hrs_day += 1
#         if hrs_day == 23:
#             hrs_day = 0
#             dailySum = dailySum/24
#             days.append(dailySum)
#     print(days)
#     return days 

# avg_temp(w.karmøytemps)