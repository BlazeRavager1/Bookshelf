class Book:
    def __init__(self, name, author, year, price):
        self.name = name
        self.author = author + " "
        self.year = year
        self.price = price
    
    def getAge(self):
        self.yearsago = 2023 - self.year

        print("The book " + self.name + " Was published by " + self.author+ str(self.yearsago) +" years ago For a price of " + self.price + " rupees")

book1 = Book("Harry Potter", "J.K Rowling", 2000, "1500")

book1.getAge()
