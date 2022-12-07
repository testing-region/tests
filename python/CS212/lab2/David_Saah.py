# time of leaving house = 6:52 am
# 1 mile at 8 mins 15 seconds
# 3 miles at 7 mins 12 seconds
# 1 mile at 8 mins 15 seconds
# GOAL: Time to get home?
# Time to get home is sum of times after 6:52 am


easy_mile_mins = 8
easy_mile_secs = 15
 
# since easy pace time occurs at the beginning and the ending
easy_mile_time = 2 * ((easy_mile_mins * 60) + easy_mile_secs)

tempo_mile_distance = 3     
tempo_mile_mins = 7
tempo_mile_secs = 12

# tempo pace time occurs per second for total distance
tempo_mile_time = tempo_mile_distance * ((tempo_mile_mins * 60) + tempo_mile_secs)

total_time = easy_mile_time + tempo_mile_time
total_time_mins = total_time // 60

# 8 mins is needed for the time to reach 7 am
# let the breakfast hour be 7
# the remainder of the minutes would be the minutes to breakfast time
breakfast_mins = total_time_mins - 8

print("Breakfast time: ", 7, ':', breakfast_mins, "am")
