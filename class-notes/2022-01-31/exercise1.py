g = 9.81

towerHeight = float(input("What is the height of the tower in meters? "))
fallTime = float(input("For how many seconds has the ball been falling? "))

# Kinematic EQ for finding displacement with constant acceleration.
distanceFallen = (g * (fallTime ** 2)) / 2

# Find the height of the ball from the ground based on how far it has fallen from the top of the tower.
currentHeight = towerHeight - distanceFallen

# If the current of the ball is less than zero it is on the ground.
if currentHeight > 0:
    print("The current height of the ball is {:3.3f}m".format(currentHeight))
else:
    print("The ball is on the ground.")
