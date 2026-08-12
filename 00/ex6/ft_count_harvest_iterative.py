

def ft_count_harvest_iterative():
    print("Days until harvest: ", sep="", end="")
    days = int(input())
    for i in range(1, days + 1):
        print("Day ", i)
    if i == days:
        print("Harvest time!")
