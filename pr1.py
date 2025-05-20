
admins = ["Ahmed", "Osama", "Ameer", "Mohamed"]
# admins.remove("Ahmed")
# print(admins)
name = input("please type your name ").strip().capitalize()
if name in admins :
    print(f"Hello {name} welcome")
    option = input("Delete Or Update your Name?").strip().capitalize()
    if option == "Update" or option == "U" :
        newName = input("type your new name please ")
        admins[admins.index(name)] = newName
        print(f"name {name} is updated to {newName}")
        print(admins)
    elif option == "Delete" or option == "D" :
        admins.remove(name)
        print(f"name {name} is deleted")
        print(admins)
else :
    print("not")
