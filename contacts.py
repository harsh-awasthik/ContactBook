import csv
import os
from person import Person
from pandas import read_csv 

def main():
    print("-------------------------")
    print("OPTIONS: \n")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print()
    o = get_option(5)
    print("-------------------------")

    if o == 1:
        AddContact()
    
    if o > 1:
        if not os.path.isfile("contacts.csv"):
            print("The Contact Book is not Created Yet.")
            return
    
    if o == 2:
        ViewContactList()

    elif o == 3:
        s = input("Enter Name of the contact to search: ")
        ls = SearchContact(s)

        if len(ls) == 0:
            print("NOT Found.")
        
        else:
            for p in range(len(ls)):
                print(str(p+1) + ".")
                for index in ls[p]:
                    print(f"{index}: {ls[p][index]}")
                print()
                
    elif o == 4:
        name = input("Enter the name of the contact: ")

        UpdateContact(name)
    
    elif o == 5:
        name = input("Enter the name of the contact you want to DELETE: ")
        DeleteContact(name)


def get_option(n):
    o = 0

    while o not in list(range(1,n+1)):
        try:
            o = int(input("Select Option Number: "))
        except ValueError:
            print("Invalid Option.")
            pass
    return o


def AddContact():
    
    file_exist = os.path.isfile("contacts.csv")
    
    firstname = input("Enter FirstName: ")
    lastname = input("Enter LastName: ")

    with open("contacts.csv", "r") as file:
        rows = csv.DictReader(file)
        for row in rows:
            if firstname.lower() == row["FirstName"].lower() and lastname.lower() == row["LastName"].lower():
                raise NameError("This contact is already present. Do you want to Update It?")
                
        
    p = Person(firstname = firstname, lastname = lastname)
   
    p.phone = input("Enter PhoneNumber: ")
    p.email = input("Enter Email: ")
    p.address = input("Enter Address: ")

    fieldnames = ["FirstName", "LastName", "PhoneNumber", "Email", "Address"]

    with open("contacts.csv", mode = "a" if file_exist else "w", newline = "" ) as file:

        writer = csv.DictWriter(file, fieldnames = fieldnames)

        if not file_exist:
            writer.writeheader()

        row = {"FirstName": p.firstname, "LastName": p.lastname, "PhoneNumber": p.phone, "Email": p.email, "Address": p.address}

        writer.writerow(row)
        

def ViewContactList():

    lst = read_csv("contacts.csv", dtype = str)
    print(lst.to_string())


def SearchContact(name):
    with open("contacts.csv", "r") as file:
        ls = []
        name = name.lower()
        rows = csv.DictReader(file)

        for row in rows:
            if name in f"{row['FirstName']} {row['LastName']}":
                ls.append(row)            
                continue
        return ls
        

def UpdateContact(name):
    with open("contacts.csv", "r") as file:
        fieldnames = ["FirstName", "LastName", "PhoneNumber", "Email", "Address"]
        rows = csv.DictReader(file)
        listofdict = []
        for row in rows:
            listofdict.append(row)
 
    for i in listofdict:

        if name.lower() in f"{i['FirstName'].lower()} {i['LastName'].lower()}":
            
            for key in i:
                print(f"{key}: {i[key]}")

            q = ""
            while q not in ["yes", "y", "no", "n"]:
                q = input("Want to Update this or another Contact.(Yes/No): ").lower()
                print("-------------------------")
                if q in ["yes", "y"]:

                    print("Select from the options: ")
                    print("1. Update FirstName\n2. Update LastName\n3. Update PhoneNumber\n4. Update Email\n5. Update Address\n")
                    action = get_option(5)

                    contact = Person()

                    if action == 1:
                        contact.firstname = input("Enter FirstName: ")
                        i['FirstName'] = contact.firstname
                    elif action == 2:
                        contact.lastname = input("Enter LastName: ")
                        i['LastName'] = contact.lastname
                    elif action == 3:
                        contact.phone = input("Enter PhoneNumber: ")
                        i['PhoneNumber'] = contact.phone
                    elif action == 4:
                        contact.email = input("Enter Email: ")
                        i['Email'] = contact.email
                    elif action == 5:
                        contact.address = input('Enter Address: ')
                        i['Address'] = contact.address
                    
                    with open("contacts.csv" , 'w', newline = "") as file:
                        fieldnames = ["FirstName", "LastName", "PhoneNumber", "Email", "Address"]
                        writer = csv.DictWriter(file, fieldnames = fieldnames)
                        writer.writeheader()

                        for a in listofdict:
                            writer.writerow(a)
                    return
    else:
        print("Name Not Found. ")


def DeleteContact(name):
    with open("contacts.csv", "r") as file:
        fieldnames = ["FirstName", "LastName", "PhoneNumber", "Email", "Address"]
        rows = csv.DictReader(file)
        listofdict = []
        for row in rows:
            listofdict.append(row)
 
    found = False
    for i in listofdict:
        if name.lower() in f"{i['FirstName'].lower()} {i['LastName'].lower()}":
            found = True
            for key in i:
                print(f"{key}: {i[key]}")

            q = ""
            while q not in ["yes", "y", "no", "n"]:
                q = input("Want to DELETE this Contact.(Yes/No): ").lower()
                print("-------------------------")
                if q in ["yes", "y"]:
                    listofdict.remove(i)

    if not found:
        print("Name Not Found. ")

    with open("contacts.csv" , 'w', newline = "") as file:
        fieldnames = ["FirstName", "LastName", "PhoneNumber", "Email", "Address"]
        writer = csv.DictWriter(file, fieldnames = fieldnames)
        writer.writeheader()

        for a in listofdict:
            writer.writerow(a)

if __name__ == "__main__":
    main()