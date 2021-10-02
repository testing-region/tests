
def bill(start_hour, start_min, end_hour, end_min):
    normal_hours = 21 - start_hour
    late_hours = end_hour - 21
    if end_hour <= 21:
        return (normal_hours + (start_min + end_min)/60) * 30
    elif end_hour == 21 and end_min > 0:
        return (normal_hours + start_min/60) * 30 + (end_min/60 * 25)
    elif end_hour > 21:
        return (normal_hours + start_min/60) * 30 + ((late_hours + end_min/60) * 25)
    else:
        return 0

# Test
print(bill(9, 0, 21, 0))
print(bill(9, 0, 21, 30))
