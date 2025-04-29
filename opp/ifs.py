##############
# If's
##############
speed_limit = 35
slow = 10
medium = 30
fast = 85
speed = slow

if speed > speed_limit:
    print("You are over the speed limit. Here is a ticket.")


speed = fast

if speed > speed_limit:
    print("You are over the speed limit. Here is a ticket.")

speed = medium


##############
# Else
##############
if speed > speed_limit:
    print("You are over the speed limit. Here is a ticket.")
else:
    print("You are good to go. Enjoy your day.")


##############
# else if
##############
if speed > speed_limit:
    print("You are over the speed limit. Here is a ticket.")
elif speed == speed_limit:
    print("You are going the speed limit. Careful not to go much faster")
else:
    print("You are good to go. Enjoy your day.")


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