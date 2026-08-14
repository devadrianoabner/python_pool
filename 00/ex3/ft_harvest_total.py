def ft_harvest_total():
    i = 0
    total = 0
    while i < 3:
        print(f"Day {i + 1} harvest: ", end="")
        total += int(input())
        i += 1
    print("Total harvest:", total)
