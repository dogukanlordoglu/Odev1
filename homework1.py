import math
numbers = int(input("How many coordinates you need?:"))
coordinates = [[0 for a in range(2)] for a in range(numbers)]
distances = [0 for a in range(numbers)]
for i in range(0,numbers):
    for k in range(0,2):
        if k == 0:
            coordinates[i][k] = float(input ("Pick the x :"))
        if k == 1:
            coordinates[i][k] = float(input ("Pick the y :"))
                   
sumx = 0
sumy = 0
for j in range(0,numbers):
    sumx = sumx + coordinates[j][0]
    sumy = sumy + coordinates[j][1]
xcenter = sumx/numbers
ycenter = sumy/numbers
print("xcenter is", xcenter)
print("ycenter is", ycenter)
for i in range(0,numbers):
    for k in range(0,2):
        if k == 0:
            xdistance = abs (coordinates[i][k] - xcenter)
        if k == 1:
            ydistance = abs (coordinates[i][k] - ycenter)
    distances[i] = math.sqrt(xdistance*xdistance + ydistance * ydistance)
lowest = 10000
highest = 0
for i in range(0,numbers):
    if distances[i] < lowest:
        lowest = distances[i]
    if distances[i] > highest:
        highest = distances[i]
print("Farthest distance is:" , highest)
print("Closest distance is;" , lowest)

        
        
            
            
        
        
    
    





