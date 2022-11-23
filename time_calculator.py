def add_time(start, duration, sday = ""):

    # extract the start time and part of the day (am/pm)
    start_time = start.split(" ")[0]
    is_pm = start.split(" ")[1] == "PM"

    # record the current time in hours and minutes
    curr_hours = int(start_time.split(":")[0])
    curr_mins = int(start_time.split(":")[1])

    # convert the current time to 24 hour format
    curr_hours_24 = curr_hours
    if is_pm:
        curr_hours_24 += 12

    # extract the duration to add
    hours_to_add = int(duration.split(":")[0])
    mins_to_add = int(duration.split(":")[1])
 

    curr_hours_24 += hours_to_add
    curr_mins += mins_to_add

    if (curr_mins - 59) > 0:
        curr_hours_24 += 1
        curr_mins -= 59

    # day counter

    day_counter = 0

    while curr_hours_24 > 23:
        day_counter += 1
        curr_hours_24 -= 24
    



    # resolve what day it is
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    start_day = sday.lower()
    curr_day = ""
    curr_index = 0

    for i in range(len(days)):
        if start_day == days[i].lower():
            curr_day = days[i]
            curr_index = i
            break
    
    final_day = days[(curr_index + day_counter) - len(days)]

    if (sday != ""):
        new_time = str(curr_hours_24) + ":" + str(curr_mins) + " " + final_day + " (" + str(day_counter) + " days later)"
    else:
        new_time = str(curr_hours_24) + ":" + str(curr_mins) + " (" + str(day_counter) + " days later)"
    

    return new_time