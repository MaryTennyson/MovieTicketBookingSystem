import sqlite3
from account_class import Account, Person
from show_class import Movie, Show


class SQLiteDB:
    def __init__(self) :
        self.connection = None
        self.cursor = None
        self.connect()

    def connect(self):
        try:
            self.connection=sqlite3.connect('movieticketbooking.db')
            self.cursor= self.connection.cursor()
            
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")

    def create_tables(self):
         
        try:
            # Create Account table
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS ACCOUNTS (
                    id INT PRIMARY KEY NOT NULL,
                    password TEXT NOT NULL,
                    status TEXT NOT NULL
                )
            ''')

            # Create Person table
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS PERSONS (
                    name TEXT NOT NULL,
                    address TEXT NOT NULL,
                    email TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    id INT NOT NULL,       
                    FOREIGN KEY (id) REFERENCES ACCOUNTS(id)
                )
            ''')

            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS MOVIE (
                    name TEXT NOT NULL,
                    address TEXT NOT NULL,
                    email TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    id INT NOT NULL,       
                    FOREIGN KEY (id) REFERENCES ACCOUNTS(id)
                )
            ''')



            self.connection.close()
            print("Tables created successfully.")
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")

    def fetch_person(self,person_id) :

        try:
          query_check_movie = "SELECT * FROM PERSONS WHERE ID = ?"
          self.cursor.execute(query_check_movie, (person_id))
          person_data = self.cursor.fetchone()
          return person_data
        except sqlite3.Error as e:
         print(f"Error authenticating user: {e}")
         return None     
    


    def authenticate_sign_in(self, email, password):
        try:
            query = '''
                SELECT ACCOUNTS.id, ACCOUNTS.password, ACCOUNTS.status
                FROM ACCOUNTS
                JOIN PERSONS ON ACCOUNTS.id = PERSONS.id
                WHERE PERSONS.email = ? AND ACCOUNTS.password = ?
            '''
            self.cursor.execute(query, (email, password))
            account_data = self.cursor.fetchone()

            if account_data:
                print(account_data)
                return account_data[0]
            else:
                return -1
        except sqlite3.Error as e:
            print(f"Error authenticating user: {e}")
            return None      
        

    def authenticate_sign_up(self,person:Person): 
       
        try:
            # Add account
            query_account = "INSERT INTO ACCOUNTS VALUES (?, ?, ?)"
            self.cursor.execute(query_account, (person.account.id,person.account.password,person.account.status.value))

            # Add person
            query_person = "INSERT INTO PERSONS VALUES (?, ?, ?, ?, ?)"
            self.cursor.execute(query_person, (person.name, person.address, person.email, person.phone, person.account.id))

            self.connection.commit()
            print("Person added successfully.")
        except sqlite3.Error as e:
            print(f"Error adding person: {e}")


    def add_movie(self,movie:Movie):
        
         try: 
            query_add_movie= "INSERT INTO movie VALUES (?,?,?,?,?,?,?,?,?)"
            self.cursor.execute(query_add_movie, (movie.movie_id,movie.title,movie.description,movie.duration_in_mins,movie.language,movie.release_date,movie.country,movie.genre,movie.movie_added_by))
            self.connection.commit()
            print("Movie Added Succesfully")

         except sqlite3.Error as e:
             print({e})
            

    def modify_movie(self,movie:Movie):
       try:
        query_check_movie = "SELECT * FROM movie WHERE title = ?"
        self.cursor.execute(query_check_movie, (movie.title,))
        existing_movie = self.cursor.fetchone()

        if existing_movie:
            # If the movie exists, update the existing record
            query_update_movie = "UPDATE movie SET description=?, duration_in_mins=?, language=?, release_date=?, country=?, genre=?, movie_added_by=? WHERE title=?"
            self.cursor.execute(query_update_movie, (
                movie.description, movie.duration_in_mins, movie.language, movie.release_date,
                movie.country, movie.genre, movie.movie_added_by, movie.title
            ))
            print("Movie Updated Successfully")
        else:
            SQLiteDB.add_movie(movie)
            print("Movie Added Successfully")
          

       except sqlite3.Error as e:
             print({e})
            
    def add_show(self,show:Show):
         
         try: 
            query_add_show= "INSERT INTO SHOW VALUES (?,?,?,?,?,?)"
            self.cursor.execute(query_add_show, (show.show_id,show.created_on,show.start_time, show.end_time,show.cinemahall_id,show.movie_id))
            self.connection.commit()
            print("Show Added Succesfully")

         except sqlite3.Error as e:
             print({e})



        

