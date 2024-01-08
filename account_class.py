from abc import ABC
from constants import AccountStatus

from show_class import Movie


class Account:
    def __init__(self, id, password, status=AccountStatus.ACTIVE):
        self.id = id
        self.password = password
        self.status = status

    def reset_password(self):
        None


# from abc import ABC, abstractmethod
class Person:
    def __init__(self, name, address, email, phone, account:Account):
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone
        self.account= account


class Customer(Person):
    def make_booking(self, booking):
        None

    def get_bookings(self):
        None


class Admin(Person):
    def add_movie(self, movie:Movie):
        from database import SQLiteDB
        SQLiteDB().add_movie(movie)

    def add_show(self, show):
         from database import SQLiteDB
         SQLiteDB().add_show(show)

    def block_user(self, customer):
        None


class FrontDeskOfficer(Person):
    def create_booking(self, booking):
        None


class Guest:
    def register_account(self):
        None

        
# def main():

 #   admin_account = Account(2,"12312321",AccountStatus.ACTIVE)  # You need to create an Account instance
 #   admin = Admin(name="Admin User", address="456 Admin St", email="admin@example.com", phone="555-5678", account=admin_account)

  #  movie= Movie("Dövüş Kulübü","Dövüş Kulübü mü o da ne?",150,"İngilizce","1999","ABD","Dram","admin")
    
  #  admin.add_movie(movie)

