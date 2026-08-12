

def ft_water_reminder():
    print("Days since last watering: ", sep="", end="")
    days = int(input())
    if days <= 2:
        print("Plants are fine")
    else:
        print("Water the plants!")
