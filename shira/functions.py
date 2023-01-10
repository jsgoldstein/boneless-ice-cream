##############
# Recall: else if
##############
speed_limit = 35
slow = 10
medium = 30
fast = 85
speed = slow

if speed > speed_limit:
    print("You are over the speed limit. Here is a ticket.")
elif speed == speed_limit:
    print("You are going the speed limit. Careful not to go much faster")
elif speed == 0:
    print("You are not moving. Did you remember to start your car?")
elif speed < 0:
    print("Reverse? Maybe? Maybe we shouldn't allow this type of input?")
else:
    print("You are good to go. Enjoy your day.")


##############
# functions
##############
def speed_check(speed):
    speed_limit = 35
    print("The speed limit is " + speed_limit + " and you are going " + speed)

    if speed > speed_limit:
        print("You are over the speed limit. Here is a ticket.")
    elif speed == speed_limit:
        print("You are going the speed limit. Careful not to go much faster")
    elif speed == 0:
        print("You are not moving. Did you remember to start your car?")
    elif speed < 0:
        print("Reverse? Maybe? Maybe we shouldn't allow this type of input?")
    else:
        print("You are good to go. Enjoy your day.")


speed_check(10)
speed_check(35)
speed_check(fast)
impossible_speed = -100
speed_check(impossible_speed)


def better_speed_check(speed, speed_limit=35):
    print("The speed limit is " + speed_limit + " and you are going " + speed)

    if speed > speed_limit:
        print("You are over the speed limit. Here is a ticket.")
    elif speed == speed_limit:
        print("You are going the speed limit. Careful not to go much faster")
    elif speed == 0:
        print("You are not moving. Did you remember to start your car?")
    elif speed < 0:
        print("Reverse? Maybe? Maybe we shouldn't allow this type of input?")
    else:
        print("You are good to go. Enjoy your day.")


better_speed_check(10)
better_speed_check(35, 50)
better_speed_check(fast, slow)
better_speed_check(slow, speed_limit=fast)
impossible_speed = -100
better_speed_check(impossible_speed)


##############
# Returns
##############
def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


five = 5
ten = 10
print(addition(five, ten))
number = subtraction(ten, five)
print(number)
