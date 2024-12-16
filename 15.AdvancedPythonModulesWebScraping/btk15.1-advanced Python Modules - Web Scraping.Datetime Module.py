# import datetime
# from datetime import date
# from datetime import time

from datetime import datetime  
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


