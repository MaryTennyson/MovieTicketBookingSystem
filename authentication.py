from account_class import Account, Person
from constants import AccountStatus
from database import SQLiteDB

class Authenticate:

    
    def sign_in(self): #kaydolma methodu
       person_email=input("Email adresinizi giriniz:")
       account_password=input("Şifresinizi giriniz:")
       user= SQLiteDB().authenticate_sign_in(person_email,account_password)
       print("user= ",user)
       return user

    def sign_up(self): 
     person_name=input("Adınızı giriniz")
     person_email=input("Email adresinizi giriniz:")
     account_password= input("Hesap sifrenizi giriniz:")
     person_address=input("Adres giriniz:")
     person_phone=input("Telefon numarası giriniz")
     account= Account(2,account_password,AccountStatus.ACTIVE)
     person= Person(person_name,person_address,person_email,person_phone,account)
     SQLiteDB().authenticate_sign_up(person)



