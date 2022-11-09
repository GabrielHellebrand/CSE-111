#python
import math
print("This program outputs the time it takes for a pendulom to swing.")
pendulom_length=float(input("What is the length of the pendulom in meters: "))
time_in_seconds=2*math.pi*math.sqrt(pendulom_length/9.81)
print (f"Time (seconds): {time_in_seconds:.2f}")
