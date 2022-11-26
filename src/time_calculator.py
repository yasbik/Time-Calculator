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
 
    # add the duration to the current time
    curr_hours_24 += hours_to_add
    curr_mins += mins_to_add

    # add 1 hour when 60 minutes pass
    if curr_mins > 59:
        curr_hours_24 += 1
        curr_mins -= 60

    day_counter = 0

    # add 1 day when 24 hours pass
    while curr_hours_24 > 23:
        day_counter += 1
        curr_hours_24 -= 24
    
    # dictionary to store 24 hour to 12 hour conversion values
    time_dict = {   0: "12 AM", 1: "1 AM", 2: "2 AM", 3: "3 AM", 4: "4 AM", 5: "5 AM", 
                    6: "6 AM", 7: "7 AM", 8: "8 AM", 9: "9 AM", 10: "10 AM", 11: "11 AM", 
                    12: "12 PM", 13: "1 PM", 14: "2 PM", 15: "3 PM", 16: "4 PM", 17: "5 PM", 
                    18: "6 PM", 19: "7 PM", 20: "8 PM", 21: "9 PM", 22: "10 PM", 23: "11 PM"    }

    # convert the current time to 12 hour format
    curr_hours_12 = time_dict[curr_hours_24].split(" ")[0]
    am_or_pm = time_dict[curr_hours_24].split(" ")[1]

    # days of the week
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    start_day = sday.lower()
    index = 0

    # calculate the starting day
    for i in range(len(days)):
        if start_day == days[i].lower():
            index = i
            break
    
    # calculate how many days passed
    days_passed = (index + day_counter) - len(days)

    # ensure array does not go out of bounds
    while days_passed > 6:
        days_passed -= 7
    while days_passed < -7:
        days_passed += 7

    # calculate the current day after all the time has passed
    final_day = days[days_passed]
    
    # format part of the output string showing the current day
    days_later = ""
    if day_counter == 0:
        days_later = ""
    elif day_counter == 1:
        days_later = " (next day)"
    else:
        days_later = " (" + str(day_counter) + " days later)"

    # add everything to the formatted string for output
    if sday != "":
        new_time = str(curr_hours_12) + ":" + str(curr_mins).zfill(2) + " " + am_or_pm + ", " + final_day + days_later
    else:
        new_time = str(curr_hours_12) + ":" + str(curr_mins).zfill(2) + " " + am_or_pm + days_later

    return new_time