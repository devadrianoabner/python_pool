

def helper_harvest(current, limit):
    if limit >= current:
        print("Day", current)
        current += 1
        helper_harvest(current, limit)
    elif current > limit:
        print("Harvest time!")


def ft_count_harvest_recursive():
    print("Days until harvest: ", end="")
    days = int(input())
    helper_harvest(1, days)
