#Python
import math
# a= float(input("Please enter A: "))
# b=float(input("Please enter B: "))
# c= float(input("Please enter C: "))
# d=float(input("Please enter D: "))



#     print(a)
#     print(b)
#     print(c)
#     print(d)
# print(compute_data)(5,4,3,2)
    
#     print(value)
# print(f"The answer for x is {x:.3f}")
# def compute_data(a,b,c):
#     return (-b+(math.sqrt(b**2-4*a*c)))/(2*a)

# print(compute_data(22,66,9))
# data=[]
# data.append([5,4,3,2,0.480769])
# data.append([9,1,4,6,1.55769])
# def compute_data(a,b,c,d):
#     return (a/b)*(a/((c**2)+(d**2)))
# for test in data:
#     print(compute_data(test[0], test[1], test[2], test[3])==test[4])


def compute_area():
    return math.pi*radius**2
radius=float(input("Please enter a radius: "))
print(f"The area is:" + compute_area(radius))