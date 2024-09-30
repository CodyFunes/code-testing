sec = int(input("enter number of seconds:"))

days = 0
hours = 0
minutes = 0

if sec >= 86400:
    days = int(sec/86400)
    sec = sec%86400
if sec >= 3600:
    days = int(sec / 3600)
    sec = sec % 3600
if sec >= 60:
    days = int(sec/60)
    sec = sec%60

print(str(days) + "day(s),  " + str(hours) + " hour(s), " + str(minutes) + " minute(s), and  " + str(sec) + " second(s). ")