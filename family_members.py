def main():
    family = get_family()
    print(family)

    save_my_family(family)

def get_family():
    
    continue_loop = "Y"
    family = []
    
    while continue_loop == "Y":
        name = input("\nEnter name: ")
        age = input("Enter age: ")
        person = {'name': name, 'age': age}
        family.append(person)
        user_input = input('Continue? (Y/n) ')
        continue_loop = 'n' if user_input == 'n' else 'Y'
    
    return family

def save_my_family(family):
    file = open ('family.txt', 'w')
    file.write('Here is a list of your family members. \n\n')
    
    for person in family:
        file.write(person['name'] + 'is' + person['age'] + 'years old.\n')

def edit_family(family):
    pass

main()

    # try:
    #     family_member_age = []
    #     family_member_name = []
    #     family_members = open("family_members.txt", "at")
    #     family_member_name = input("What is the name of your family member? ")
    #     family_member_age = input("What is the age of your family member? ")
    #     family_members.writelines(family_member_name)
    #     family_members.writelines(family_member_age)
    #     family_members.close()
    # except:
    #     ("Sorry couldn't find the text file")
    # # for i in family_member_age:
    # #     pass
    # # for i in family_member_name:
    # # main() 