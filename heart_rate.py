#python
txt=input("Please enter your age ")
age=int(txt)
max=220-age 
slowest=max*0.65 
fastest=max*0.85
print(f"When you exercise to strengthen your heart you should keep your heart rate between {slowest:.0f} and {fastest:.0f} beats per minute")