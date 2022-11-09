#python
import math
from datetime import datetime

# This function calculates the volume of a tire.

print ("This program calculates the volume of a tire.")

width = float (input ("What is the width of the tire in mm: "))

aspect_ratio = float (input ("What is the aspect ratio of the tire: "))

diameter = float (input ("What is the diameter of a tire in inches: "))

volume = (math.pi*width**2*aspect_ratio*(width*aspect_ratio+2540*diameter))/10**10

# This asks the customer for his or her name.

name = input("What is your name ")

print (f"Hello {name}, here is your tire information.")

print (f"volume (liters): {volume:.2f}")

# This opens the volumes text file.

with open("volumes.txt", "a") as volumes_file:
        current_date_and_time = datetime.now()
        print(f"{current_date_and_time:%Y-%m-%d}")
        output = []