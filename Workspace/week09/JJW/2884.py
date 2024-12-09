hour, minute = input().split()

int_hour = int(hour)
new_minute = int(minute) - 45

if new_minute < 0:
    int_hour -= 1
    new_minute = 60 + new_minute

if int_hour < 0:
    int_hour = 24 + int_hour

print("%d %d" % (int_hour, new_minute))