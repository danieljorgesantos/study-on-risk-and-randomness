import matplotlib.pyplot as plt
import random

random_numbers = [random.randint(-200, 200) - 50 for _ in range(365)]
current_price = [0]
x_axis = list(range(365))

for i in range(1, 365):
    last_price = current_price[-1]
    current_price.append(last_price + random_numbers[i])

x20_1_3_random_buy_or_sell = []
current_position = 0

for number in random_numbers:
    current_position += number
    if current_position > 198:
        x20_1_3_random_buy_or_sell.append(x20_1_3_random_buy_or_sell[-1] + 300)
        current_position = 0
    elif current_position < -66:
        x20_1_3_random_buy_or_sell.append(x20_1_3_random_buy_or_sell[-1] - 100)
        current_position = 0
    else:
        x20_1_3_random_buy_or_sell.append(x20_1_3_random_buy_or_sell[-1])

x20_1_4_random_buy_or_sell = []
current_position_2 = 0

for number in random_numbers:
    current_position_2 += number
    if current_position_2 > 264:
        x20_1_4_random_buy_or_sell.append(x20_1_4_random_buy_or_sell[-1] + 378)
        current_position_2 = 0
    elif current_position_2 < -66:
        x20_1_4_random_buy_or_sell.append(x20_1_4_random_buy_or_sell[-1] - 100)
        current_position_2 = 0
    else:
        x20_1_4_random_buy_or_sell.append(x20_1_4_random_buy_or_sell[-1])

plt.figure()

plt.plot(x_axis, current_price, label='random price')
plt.plot(x_axis, x20_1_3_random_buy_or_sell, label='1/3 x20 buy')
plt.plot(x_axis, x20_1_4_random_buy_or_sell, label='1/4 x20 buy')

plt.xlabel('days')
plt.ylabel('money')
plt.title('Multiple Lines')

plt.legend()
plt.show()

old_value = 1070
new_value = x20_1_2_random_buy_or_sell[-1]

percentage_variation = ((new_value - old_value) / old_value) * 100

print("Percentage variation 1/3 x20 random buy or sell:", percentage_variation)
