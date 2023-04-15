# TODO

from cs50 import get_float

while True:
    money = get_float("Change owed: ")
    if money >= 0:
        break
    else:
        print("change can't be negative number!")

count_dimes = money * 100 //25
remainder= (money*100- (25 * count_dimes))

count_cents = remainder// 10
remainder -= (10 * count_cents)

count_fives= remainder// 5
remainder-= (5 * count_fives)

count_ones = remainder//1

resultant= count_dimes + count_cents + count_fives + count_ones
print (f"{resultant}")

