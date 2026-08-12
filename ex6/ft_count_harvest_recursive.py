

def ft_count_harvest_recursive(current, limit):
    print("Days until harvest: ", end="")
    days_total = int(input())

# Gatilho inicial
    if days_total == 0:
        print("Harvest time!")
    else:
        ft_count_harvest_recursive(1, days_total)
