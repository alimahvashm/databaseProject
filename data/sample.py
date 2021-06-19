import sqlite3
from datetime import date, datetime

db = sqlite3.connect(':memory:')
cursor = db.cursor()
cursor.execute('''
    CREATE TABLE users1(userid TEXT PRIMARY KEY, name TEXT,
                       deptid TEXT, foreign key(deptid) references users2(deptid), foreign key(userid) references reserve(userid))                  
'''
)
cursor.execute('''
    CREATE TABLE users2(deptid TEXT PRIMARY KEY, deptname TEXT)                  
'''
)
cursor.execute('''
    CREATE TABLE books1(accessino TEXT PRIMARY KEY, isbn TEXT, foreign key(isbn) references books2(isbn),foreign key(accessino) references reserve(accessino))                  
'''
)
cursor.execute('''
    CREATE TABLE books2(isbn TEXT PRIMARY KEY, title TEXT, publisher TEXT,
                       author TEXT)                  
'''
)

cursor.execute('''
    CREATE TABLE reserve(userid TEXT ,accessino TEXT , created_at DATE,primary key(userid,accessino)
)                  
'''
)

db.commit()

cursor = db.cursor()
while True:
    print("1-add user")
    print("2-add department")
    print("3-add book access number")
    print("4-add book detail")
    print("5-reserve a book")
    print("6-remove reservation book")    
    choose = int(input("choose one of the options:"))
    if choose == 1:
        
         userid = input("Enter your userid: ")
         name = input("Enter your name: ")
         deptid =  input("Enter your deptid: ")
         cursor.execute(f'SELECT userid, name, deptid FROM users1 where userid={userid}')
         all_rows = cursor.fetchall()
         if len(all_rows) == 0:
            cursor.execute('''INSERT INTO users1(userid, name ,deptid)   
                      VALUES(?,?,?)''', (userid,name, deptid))
            print("user added successfully")
            cursor.execute('''SELECT userid, name, deptid FROM users1''')

            all_rows = cursor.fetchall()
            for row in all_rows:
             print('userid: {0} , name: {1}, deptid: {2}'.format(row[0], row[1], row[2]))
        
         else:
            print("user with this userid has already been added")
       

    if choose == 2:
         deptid =  input("Enter your deptid: ")
         deptname =  input("Enter your deptname: ")
         cursor.execute(f'SELECT deptid, deptname FROM users2 where deptid={deptid}')
         all_rows = cursor.fetchall()
         if len(all_rows) == 0:
            cursor.execute('''INSERT INTO users2(deptid, deptname)   
                      VALUES(?,?)''', (deptid, deptname))                  
            print('department added successfully')
            cursor.execute('''SELECT deptid, deptname FROM users2''')

            all_rows = cursor.fetchall()
            for row in all_rows:
             print('deptid: {0} , deptname: {1}'.format(row[0], row[1]))
         else:
            print("dapartment with this deptid has already been added")

    if choose == 3:
         accessino =  input("Enter book access number: ")
         isbn =  input("Enter book isbn: ")
         cursor.execute(f'SELECT accessino, isbn FROM books1 where accessino = {accessino}')
         all_rows = cursor.fetchall()
         if len(all_rows) == 0:         
            cursor.execute('''INSERT INTO books1(accessino, isbn)   
                    VALUES(?,?)''', (accessino, isbn))                  
            print('book access number added successfully')
            cursor.execute('''SELECT accessino, isbn FROM books1''')

            all_rows = cursor.fetchall()
            for row in all_rows:
             print('accessino: {0} , isbn: {1}'.format(row[0], row[1]))
         else:
            print("book with this accessino has already been added")             
    if choose == 4:
          isbn =  input("Enter book isbn: ")
          title =  input("Enter book title: ")
          publisher =  input("Enter book publisher: ") 
          author =  input("Enter book author: ")
          cursor.execute(f'SELECT isbn FROM books2 where isbn = {isbn}')
          all_rows = cursor.fetchall()
          if len(all_rows) == 0:               
            cursor.execute('''INSERT INTO books2(isbn,title,publisher,author)   
                    VALUES(?,?,?,?)''', (isbn, title,publisher,author))                  
            print('book detail added successfully')
            cursor.execute('''SELECT isbn, title,publisher ,author FROM books2''')

            all_rows = cursor.fetchall()
            for row in all_rows:
             print('isbn: {0} , title: {1},publisher: {2},author: {3} '.format(row[0], row[1], row[2], row[3]))
          else:
            print("book with this isbn has already been added")    
    if choose == 5:
         userid =  input("Enter your userid: ") 
         accessino =  input("Enter book access number: ")
         today = date.today()
         cursor.execute(f'SELECT userid,accessino FROM users1, books1 where userid = {userid} and  accessino={accessino} ')
         all_rows = cursor.fetchall()
         if len(all_rows) != 0:               
            cursor.execute('''INSERT INTO reserve(userid,accessino,created_at)   
                    VALUES(?,?,?)''', (userid, accessino,today))                  
            print('reserved successfully')
            cursor.execute('''SELECT userid, accessino, created_at FROM reserve''')

            all_rows = cursor.fetchall()
            for row in all_rows:
             print('userid: {0} , bookid: {1}, reserved Date: {2}'.format(row[0], row[1], row[2]))  
         else:
            print("book or user with this information does not exist") 
    if choose == 6:
         print("enter the information that you want to cancel reservation")
         userid =  input("Enter your userid: ") 
         accessino =  input("Enter book access number: ")
         today = date.today()
         cursor.execute(f'SELECT userid, accessino FROM reserve where userid = {userid} AND  accessino = {accessino} ')
         all_rows = cursor.fetchall()    
         
         if len(all_rows) != 0:
            cursor.execute(f'DELETE FROM reserve where userid = {userid} and  accessino={accessino} ')               
            print("deleted successfully") 
         else:
            print("book or user with this information does not exist") 

    # deptid =  input("Enter your name: ")
    # deptid =  input("Enter your name: ")
    # deptid =  input("Enter your name: ")
    # deptid =  input("Enter your name: ")

    print("--------------------------------------")
    db.commit()



db.close()

print("sa")