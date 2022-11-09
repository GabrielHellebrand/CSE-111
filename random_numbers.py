import numbers
import random
def main():
    numbers = []
    print(numbers)
    append_random_numbers()
    numbers = numbers + 1
    append_random_numbers()
def append_random_numbers(numbers_list, quantity):
    
    quantity = 1
    for i in range (quantity):
        print(random.uniform(1,1000))
