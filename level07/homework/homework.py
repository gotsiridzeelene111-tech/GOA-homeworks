# შედარების ოპერატორები
# == - უდრის
print(3 == 3)
print(10 == 10)
print(5 == 5)
print(44 == 44)
print(777 == 777)
# < - ნაკლებია 
print(2 < 10)
print(6 < 10)
print(9 < 10)
print(7 < 10)
print(1 < 10)
# > - მეტია
print(10 > 5)
print(10 > 3)
print(10 > 2)
print(10 > 1)
print(10 > 9)
# <= - ნაკლებია ან ტოლია
print(10 <= 10)
print(3 <= 5)
print(7 <= 15)
print(7 <= 7)
print(21 <= 27)
# >= - მეტია ან ტოლია
print(1 >= 1)
print(10 >= 8)
print(33 >= 15)
print(42 >= 42)
print(55 >= 33)
# != - არ უდრის
print(3 != 5)
print(7 != 8)
print(33 != 19)
print(15 != 99)
print(44 != 66)


# logical operators - გამოიყენება პირობების დასაკავშირებლად და სისწორის ან მცდარობის შესამოწმებლად.
# and-ის დროს: 
# False and False = False; 
# False and True = False; 
# True and False = False; 
# True and True = True;
print(10 > 5 and 5 < 6)
print(5 >= 6 and 15 > 7)
print(6 != 6 and 20 < 5 )
# or-ის დროს:
# False or False = False;
# False or True = True;
# True or False = True;
# True or True = True;
print(50 > 100 or 20 == 20)
print(9 < 3 or 15 < 10)
print(7 == 7 or 10 != 10)
# not-ის დროს
# not False = True;
# not True = False;
print(not(20 > 10))
print(not(3 == 5))
print(8 != 8)

number = int(input("enter any  number: "))
print(number > 77)

name = input("enter your name: ")
print(name == "Elene")

age = int(input("enter your age: "))
print(age > 18)