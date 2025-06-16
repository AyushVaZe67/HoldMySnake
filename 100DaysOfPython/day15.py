import time
hr = int(time.strftime('%H'))
print(hr)
print(type(hr))
if 6 < hr < 12:
    print('GM')
elif 12 < hr < 18:
    print('GE')
else:
    print('GN')