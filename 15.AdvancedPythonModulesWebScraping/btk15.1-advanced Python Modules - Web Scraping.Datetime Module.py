# import datetime
# from datetime import date
# from datetime import time

from datetime import datetime  
from datetime import timedelta
now = datetime.now()



def weekday():
    result = now.weekday()
    if result == 0:
        return 'mo'
    elif result == 1:
        return 'tu'
    elif result == 2:
        return 'we'
    elif result == 3:
        return 'th'
    elif result == 4:
        return 'fr'
    elif result == 5:
        return 'sa'
    else:
        return 'su'
print(weekday())



result = datetime.now()
result = datetime.today()
result = now.year
result = now.month
result = now.day
result = now.hour
result = now.minute
result = now.second
result = datetime.ctime(now)            # Mon Dec 16 12:03:58 2024
result = datetime.strftime(now,'%Y')    # 2024
result = datetime.strftime(now,'%d')    # 16
result = datetime.strftime(now,'%D')    # 12/16/24
result = datetime.strftime(now,'%m')    # 12
result = datetime.strftime(now,'%h')    # Dec
result = datetime.strftime(now,'%A')    # Monday
print(result)



t = '21 May 2024 hour 10:12:42'
#day, month, year = t.split()

dt = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')     # 2024-05-21 10:12:42
print(dt)

result = dt.year
print(result)                           # 2024



birthday = datetime(1995,5,9,12,30,00)  # 1995-05-09 12:30:00
print(birthday)                         

result = datetime.timestamp(birthday)   # second             => 800011800.0
result = datetime.fromtimestamp(result) # second to datetime => 1995-05-09 12:30:00
print(result)                           


result = now - birthday                 # timedelta => 10814 days, 0:00:49.476085
#result = result.days
#result = result.seconds
#result = result.microsecond

result += timedelta(days=16)            # timedelta => 10830 days, 0:00:49.476085
result = now + timedelta(days=15)       # timedelta => 2024-12-31 12:39:19.164714

print(result)
