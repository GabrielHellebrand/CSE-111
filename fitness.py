# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime
import math

def main():
    # Get the user's gender, birthdate, height, and weight.
    gender = input("What is your gender? ")
    weight = input("What is your weight, fatty? ")
    height= input("What is your height, tiny? ")
    birthday= ()

    # Call the compute_age, kg_from_lb, cm_from_in,
    age = compute_age(birthday)
    weight_kilo = kg_from_lb(weight)
    centimeters= cm_from_in(height)
    
    # body_mass_index, and basal_metabolic_rate functions
    # as needed.

    # Print the results for the user to see.
    pass


def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years


def kg_from_lb(pounds):
    pounds=float(input("What is your weight in pounds? "))
    kilo_grams= pounds * 0.453592
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    return kilo_grams


def cm_from_in(inches):
    inches=float(input("What is your height in inches? "))
    centimeters= inches * 2.54
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    return centimeters


def body_mass_index(kilo_grams, centimeters):
    kg_from_lb(kilo_grams)
    cm_from_in(centimeters)
    body_mass_index=10,000 * kilo_grams/centimeters ** 2

    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    return body_mass_index


def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    return


# Call the main function so that
# this program will start executing.

