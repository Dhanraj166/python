# There are four Mobile Phones in a house. At 5 a.m, all the four Mobile
# Phones will ring together. Thereafter, the first one rings every 15 minutes, the second one
# rings every 20 minutes, the third one rings every 25 minutes and the fourth one rings
# every 30 minutes. At what time, will the four Mobile Phones ring together again?


phone1 = 15
phone2 = 20
phone3 = 25
phone4 = 30
start_hour = 5

minutes_passed = 30

while True:
    if (minutes_passed % phone1 == 0 and 
        minutes_passed % phone2 == 0 and 
        minutes_passed % phone3 == 0 and 
        minutes_passed % phone4 == 0):
        break 
    minutes_passed += 5

hours_passed = minutes_passed // 60

final_hour = start_hour + hours_passed

print(f"Total minutes ring together: {minutes_passed} minutes")
print(f"Total hours passed: {hours_passed} hours")
print(f"The phones will ring together: {final_hour}:00 a.m.")
