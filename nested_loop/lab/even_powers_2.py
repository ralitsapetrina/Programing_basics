max_power = int(input())

for power in range(0, max_power+1, 2):
    print(pow(2, power))
    # or print(2 ** power)