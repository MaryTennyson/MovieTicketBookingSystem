from account_class import Account, Admin, Person
from authentication import Authenticate
from constants import AccountStatus
from database import SQLiteDB
from show_class import Movie, Show


def main():

   # admin_account = Account(2,"12345",AccountStatus.ACTIVE)  # You need to create an Account instance
   # admin = Admin("Admin User", "456 Admin St", "ebrar@hotmai.com", "555-5678", admin_account)
    movie= Movie(7,"Batman","Bu bir uçak!",224,"İngilizce","2007","ABD","Fantastik","admin")


    show=Show(4,"Çarşamba",0,3,"11.00","13.00")
 
 


    user_id=Authenticate().sign_in()
    
    if(user_id!=-1):
       admin_account = Account(5,"12345",AccountStatus.ACTIVE)  # You need to create an Account instance
       admin = Admin(name="Admin User", address="456 Admin St", email="ebrar@gmail.com", phone="555-5678", account=admin_account)
       
      # user=SQLiteDB().fetch_person(int(user_id))
      
      # admin.add_show(show)
       admin.add_movie(movie)
    else:
       print("Üye Olmanız Gerekmektedir.")
       Authenticate().sign_up()    
        
   

 


if __name__ == "__main__":
    main()