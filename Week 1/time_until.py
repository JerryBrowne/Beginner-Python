later_hour, later_min = 18, 30

current_hour, current_min = 14, 45


later_total_mins = later_hour * 60 + later_min
current_total_mins = current_hour * 60 + current_min

mins_until_later_time = later_total_mins - current_total_mins


hours = mins_until_later_time // 60

mins = mins_until_later_time % 60

print("Hours: " + str(hours) + " Mins: " + str(mins))

