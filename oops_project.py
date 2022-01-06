
"""
create a library class
display book
lend book
add book
return book

"""

class Libery:

    def __init__(self,name,book) -> None:
        self.username = name
        self.booklist = book
        self.lenddict = {}
        
    def displaybook(self):
        print("We have the following books in our libery:")
        for book in self.booklist:
            print(f"[{book}]")
    
    def lendbook(self,user,book):
        
        if book not in self.lenddict.keys():
            
            self.lenddict.update({book:user})
            print("lenddict has been updated...you can take the book")
        else:
            print(f"Book is already take: {self.lenddict[book]}")
            
    def addbook(self,book):
        self.booklist.append(book)
        print("Book has been added in book list.")

    def returnbook(self,book):
        self.lenddict.pop(book)
        print("your book has been retured succesfully.")
        
if __name__=='__main__':
    user_name = input("Enter your name: ")
    book_dict = ["HARRY POTTER","RICH DAD POOR DAD","THE COMPOUND EFFECT","YOU CAN DO IT","HOW TO MAKE MONEY","THE INTELEGENT INVESTER","0 TO 1"]
    Jitesh = Libery(user_name,book_dict)

    while(True):
        print(f"\n'{Jitesh.username}' Welcome to the Jitesh Libery")
    
        user_choice = input(f"\n{Jitesh.username} What you want\n d:-for display book.\n l:-for lendbook\n a:-for addbook\n r:-for returnbook\nplease choose an option: ")
        if user_choice not in ['d','l','a','r']:
            print("please enter a valid option!")
            continue
        else:
            user_choice = str(user_choice)

        if user_choice == 'd':
            Jitesh.displaybook()

        elif user_choice == 'l':
            for book in Jitesh.booklist:
                print(f"[{book}]")
            book = input(f"{Jitesh.username} Please input book name! Which book you want to borrow: ")
            name = input(f"{Jitesh.username} Please input your good name:  ")
            Jitesh.lendbook(name,book)
        
        elif user_choice == 'a':
            book_name = input("Which book you want to add please input book name: ")
            Jitesh.addbook(book_name)

        elif user_choice == 'r':
            returnbook = input("which book you want to return please input book name: ")
            Jitesh.returnbook(returnbook)

        else:
            print("Not a valid option.Please input valid option!")
  
        print("c for continue and q for quit")
        
        user_choice2 = ""
        while (user_choice2 !="c" and user_choice2 !="q"):
            user_choice2 = input("input in small letters: ")

            if user_choice2 == "q":
                print(f"\n Thank you {Jitesh.username} .Come again!")
                exit()

            elif user_choice2 == "c":
                continue



