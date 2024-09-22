"""task_for_week_two"""

numbers = input("Enter a list of numbers separated with commas > ")
numbers = numbers.split(",")
print(numbers)

accum = 0
for w in numbers:
    accum = accum + int(w)
print(accum)

#TASK 2
favorite_books = ("Think and Grow Rich", "What Makes The Great Great","Rich Dad", "God's General", "Purple Hibiscus")
for favorite_book in favorite_books:
    print(favorite_book)

#TASK 3
person = {}

person["name"] = input("What is your name? ")
person["age"] = input("How old are you? ")
person["favorite_color"] = input("What's your favorite color? ")
print(person)

#TASK 4
pgm = set()
A = input("Enter a sequence of numbers separated with commas > ")
A = A.split(",")
A1 = []
for a in A:   #For converting the string element into an integer
    A1.append(int(a))

B = input("Enter another sequence of numbers separated with commas > ")
B = B.split(",")
B1 = []
for b in B:  #For converting the string element into an integer
    B1.append(int(b))

A2 = set()
B2 = set()
A2.update(A1)
B2.update(B1)
pgm.update(A2,B2)
print(A2)
print(B2)
print(pgm)

set_common_to_A2_and_B2 = A2.intersection(B2)

print(f"The intersection between set A2 and set B2 are: {set_common_to_A2_and_B2}")


#TASK 5
lst_of_words = ["apple", "banana", "Orange", "Pineapple"]
new_lst = []
for w in lst_of_words:
    if len(w) % 2 == 0:
        pass
    else:
        new_lst.append(w)

print(new_lst, "\n")