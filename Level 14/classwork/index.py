#დავალება: მომხმარებელს შემოატანინეთ რიცხვი, და შემდეგ დადგინეთ, ეს რიცხვი უდრის თუ არა თქვენს ასაკს, თუ რიცხვი უდრის თქვენს ასაკს მაშინ დაგვიპრინტოს True, ხოლო სხვა შემთხვევაში False




#user_age1 = int(input("enter your first number :"))

#user_age2 = int(input("enter my age :"))


#if user_age1 == user_age2:
#    print("True")
#elif user_age2 > user_age1:
#    print("False")





# შექმენით Python პროგრამა, რომელიც მოუწოდებს მომხმარებელს შეიყვანოს თავისი ასაკი და შემდეგ განსაზღვრავს, შეუძლიათ თუ, რომ მიიღობ მონაწილეობა შემდეგ აქტივობებში:


# მომხმარებელი უნდა იყოს მინიმუმ 18 წლის, მაგრამ არაუმეტეს 60 წლის, რომ იყოს უფლებამოსილი.
# მომხმარებელი ან უნდა იყოს დასაქმებული ან იყოს სტუდენტი დადასტურებისთვის.


user_age1 = int(input("enter your age :"))
user_experience = input("enter your job or student status:  ")

user_age_confim = user_age >= 18 and user_age < 60
user_experiens_confim, " and user is ",
user_experience == "Students"

print("user is", user_age_confim, "and user")

if user_age1 < 18 or user_age1 > 60 :
    print("False")
else user is a tudent or have job :
    print("True")






