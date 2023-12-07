class Weather:
    def __init__(self, weekday, temp_c, is_sunny):
        self.weekday = weekday
        self.temp_c = temp_c
        self.is_sunny = is_sunny

    def to_farenheit(self):
        return (self.temp_c * (9 / 5)) + 32


def get_hottest_sunny_day(list_objs):
    sunny_days = []
    for objs in list_objs:
        if objs.is_sunny:
            sunny_days.append(objs)

    if len(sunny_days) == 0:
        return None

    hottest_day = sunny_days[0]

    for i in range(1, len(sunny_days)):
        if sunny_days[i].temp_c > hottest_day.temp_c:
            hottest_day = sunny_days[i]

    return hottest_day


monday = Weather("Monday", 35, False)
tuesday = Weather("Tuesday", 35, True)
wednesday = Weather("Wednesday", 55, True)
thursday = Weather("Thursday", 95, True)
friday = Weather("Friday", 35, False)

print(monday.to_farenheit())

weathers = [monday, tuesday, wednesday, thursday, friday]
sunny_day = get_hottest_sunny_day(weathers)
print(sunny_day.weekday)
