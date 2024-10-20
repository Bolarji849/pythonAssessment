import time


current_time = time.time()
total_seconds = int(current_time)

current_seconds = int(total_seconds % 60) 


total_minute = total_seconds / 60

print (current_seconds)




minute = int(total_minute % 60)

hour = total_minute / 60

current_hour = int(hour % 24) + 1


print(f"{current_hour}:{minute}:{current_seconds}")