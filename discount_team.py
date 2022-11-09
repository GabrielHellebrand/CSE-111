#Python
from datetime import date
today = date.today().weekday()

today=2

total = float(input("What is the subtotal? $ "))

if total >= 50 and (today == 1 or today == 2):
    total *= 0.9
    print("applying discount")

total *= 1.06

print(f"Total: ${total:.2f}")
