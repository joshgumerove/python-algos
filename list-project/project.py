# how many days above average temperature

def average(daily_highs):
    daily_high_sum = sum(daily_highs)
    days = len(daily_highs)
    return daily_high_sum / days


def days_above_average(daily_temps):
    daily_average = average(daily_temps)
    days_above = [day for day in daily_temps if day > daily_average]
    return len(days_above)

number_of_days = input("how many days temperature: ")
number_of_days_value = int(number_of_days)

temps_list = []

for i in range(number_of_days_value):
    day_temp = input(f"enter the temp for day {i + 1}: ")
    day_temp_value = float(day_temp)
    temps_list.append(day_temp_value)
    
print("the average temperature: ", average(temps_list))
print("days above: ", days_above_average(temps_list))