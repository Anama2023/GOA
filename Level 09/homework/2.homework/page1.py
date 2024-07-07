# 2) დაწერეთ პროგრამა, რომელიც იღებს ორი ადამიანის ასაკს და განსაზღვრავს ვინ არის უფროსი.

# ნაბიჯები:

# შესთავაზეთ მომხმარებელს შეიყვანოს პირველი პირის ასაკი.
# სთხოვეთ მომხმარებელს შეიყვანოს მეორე პირის ასაკი.
# შეადარეთ ორი ასაკი შედარების ოპერატორების გამოყენებით.
# გამოიტანეთ შეტყობინება, რომელიც მიუთითებს იმაზე, თუ ვინ არის უფროსი ან იმავე ასაკის.


user_age1 = int(input("enter your age:"))

user_age2 = int(input("enter your age:"))


if user_age1 > user_age2:
    print("The first person is older")
elif user_age2 > user_age1:
    print("The second person is older")
else:
    print("both are same age")