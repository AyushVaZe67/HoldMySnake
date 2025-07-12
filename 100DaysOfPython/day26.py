import time
hour = int(time.strftime('%H'))
print(hour)

if (hour > 0 and hour < 12):
    print('GM')
elif (hour > 12 and hour < 17):
    print('GA')
else:
    print('GN')
