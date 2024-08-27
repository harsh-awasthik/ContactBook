import re

class Person:
    def __init__(self, firstname = "", phone = "", lastname="", email="", address=""):
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone
        self.email = email
        self.address = address
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}: {self.phone}"
    
    @property
    def firstname(self):
        return self._firstname
    
    @firstname.setter
    def firstname(self, firstname):
        if not re.fullmatch(r"[a-zA-Z]*", firstname):
            raise ValueError("Invalid FirstName")
        self._firstname = firstname

    @property
    def lastname(self):
        return self._lastname
    
    @lastname.setter
    def lastname(self, lastname):
        if not re.fullmatch(r"[a-zA-Z]*", lastname):
            raise ValueError("Invalid LastName")
        self._lastname = lastname

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        if email:
            if not re.fullmatch(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
                raise ValueError("Invalid Email")
        self._email = email

    @property
    def phone(self):
        return self._phone
    
    @phone.setter
    def phone(self, phone):
        if phone:
            if not re.fullmatch(r"\+?[\d\s.-]{7,15}", phone):
                raise ValueError("Invalid Phone Number")
        self._phone = phone
    
