import math

buidling_distance = float(input("Enter the building distance in meters:- "))
angle = float(input("Enter the angle:- "))
radians = math.radians(angle)
height_in_meters = buidling_distance * math.tan(radians)
height_in_feet = height_in_meters * 3.28084

print("The building height is :",math.ceil(height_in_feet) , "Feets")
