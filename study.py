import matplotlib.pyplot as plt

import random

random_numbers = [0]
current_price = [0]
x_axis = [0]

for i in range(1,365):  # Change 10 to the desired number of random numbers
    number = random.randint(-200, 200)
    random_numbers.append(number-50)
    
    # current price
    last_price = current_price[-1]
    current_price.append(last_price + number)
    
    # x_axis
    x_axis.append(i)
    
    # x20_1_2_random_buy_or_sell

x20_1_3_random_buy_or_sell = []
currentPositionPerDay = []

for i in range(len(random_numbers)):
    if i == 0:
        x20_1_3_random_buy_or_sell.append(1070 + random_numbers[i])
        currentPositionPerDay.append(random_numbers[i])
    else:
        currentPositionPerDay.append(currentPositionPerDay[-1] + random_numbers[i])
        array_sum = sum(currentPositionPerDay)

        # x20_1_2_random_buy
        if array_sum > 198:
            x20_1_3_random_buy_or_sell.append(x20_1_3_random_buy_or_sell[-1] + 300)
            currentPositionPerDay = [0]
        elif array_sum < -66:
            x20_1_3_random_buy_or_sell.append(x20_1_3_random_buy_or_sell[-1] - 100)
            currentPositionPerDay = [0]
        else:
            x20_1_3_random_buy_or_sell.append(x20_1_3_random_buy_or_sell[-1])
            
x20_1_4_random_buy_or_sell = []
currentPositionPerDay_2 = []

for i in range(len(random_numbers)):
    if i == 0:
        x20_1_4_random_buy_or_sell.append(1070 + random_numbers[i])
        currentPositionPerDay_2.append(random_numbers[i])
    else:
        currentPositionPerDay_2.append(currentPositionPerDay_2[-1] + random_numbers[i])
        array_sum = sum(currentPositionPerDay_2)

        # x20_1_2_random_buy
        if array_sum > 264:
            x20_1_4_random_buy_or_sell.append(x20_1_4_random_buy_or_sell[-1] + 378)
            currentPositionPerDay_2 = [0]
        elif array_sum < -66:
            x20_1_4_random_buy_or_sell.append(x20_1_4_random_buy_or_sell[-1] - 100)
            currentPositionPerDay_2 = [0]
        else:
            x20_1_4_random_buy_or_sell.append(x20_1_4_random_buy_or_sell[-1])
            
# Data for the first line
x1 = x_axis
y1 = current_price

# Data for the second line
x2 = x_axis
y2 = x20_1_3_random_buy_or_sell

# Data for the third line
x3 = x_axis
y3 = x20_1_4_random_buy_or_sell


# Create a new figure
plt.figure()

# Plot the first line
plt.plot(x1, y1, label='random price')

# Plot the second line
plt.plot(x2, y2, label='1/3 x20 buy')

# Plot the third line
plt.plot(x3, y3, label='1/4 x20 buy')


# Add labels and title
plt.xlabel('days')
plt.ylabel('money')
plt.title('Multiple Lines')

# Display a legend
plt.legend()

# Show the plot
plt.show()


old_value = 1070
new_value = x20_1_2_random_buy_or_sell[-1]

percentage_variation = ((new_value - old_value) / old_value) * 100

print("Percentage variation 1/3 x20 random buy or sell:", percentage_variation)

