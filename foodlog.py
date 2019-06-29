# This program is a food log that is used to record the foods you ate in a day and their calories
# Use this at the end of your day (maybe) and it will total your calories and record all the things you ate

import datetime
import time
import pickle


class FoodEntry:
    def __init__(self, date_today, foods, calories, total_calories):
        self.date_today = date_today
        self.foods = foods
        self.calories = calories
        self.total_calories = total_calories


current_day = datetime.datetime.now()
current_day = current_day.strftime("%Y-%m-%d")
food_ate = input('What did you eat today?')
food_cals = input('Approximately how much calories were each of these food items, respectively:')

# Splits the food elements after a comma
food_list = food_ate.split(",")
food_list = [x.strip(' ') for x in food_list]

# Splits the calories for each food and converts into ints
cals_list = food_cals.split(",")
cals_list = list(map(int, cals_list))

# Calculates total calories
total_cals = sum(cals_list)

x = FoodEntry(current_day,food_list, cals_list, total_cals)

pickle_in = open("log.pickle","rb")
new_log = pickle.load(pickle_in)
pickle_in.close()

food_log = new_log
food_log.append(x)

pickle_out = open("log.pickle", "wb")
pickle.dump(food_log, pickle_out)
pickle_out.close()

pickle_in = open("log.pickle","rb")
new_log = pickle.load(pickle_in)
pickle_in.close()

todays_total = x.total_calories

for i in range(len(list(new_log))-1):
    # Checks every other entry before the new x entry
    # if the dates are the same adds thier totals, otherwise leave the total
    if x.date_today == new_log[i].date_today:
        todays_total += new_log[i].total_calories
    else:
        todays_total = x.total_calories

for i in range(len(list(new_log))):
    print(new_log[i].date_today + ': ' + str(new_log[i].total_calories))

print(todays_total)


with open('/Users/mahirahmed/Desktop/Foodlog/foodlog.txt', 'a') as a_writer:
    # Writes down the food log in the "foodlog.txt" file
    a_writer.write('\n')
    a_writer.write('\n')
    a_writer.write(x.date_today)
    for i in range(len(list(x.foods))):
        a_writer.write('\n')
        a_writer.write(x.foods[i] + ': ' + str(x.calories[i]) + ' calories')
    a_writer.write('\n')
    a_writer.write('Total calories: ' + str(x.total_calories))
    a_writer.write('\n')
    a_writer.write('Total calories today: ' + str(todays_total))

# Cool countdown
count_down = 3
while count_down:
    time.sleep(0.5)
    print(count_down)
    count_down -= 1
time.sleep(0.3)
print('Your food entry has been logged, exiting program now...')


# Add functionality to move this date into excel





