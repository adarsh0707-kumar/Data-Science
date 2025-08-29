Maths = int(input("Enter your Maths marks: "))
Science = int(input("Enter your Science marks: "))
English = int(input("Enter your English marks: "))
Hindi = int(input("Enter your Hindi marks: "))
SocialScience = int(input("Enter your Social Science marks: "))


Total = Maths + Science + English + Hindi + SocialScience
Percentage = (Total / 500) * 100

if(Percentage >= 90):
    print("Your Grade is A+")
elif(Percentage >= 80):
    print("Your Grade is A")
elif(Percentage >= 70): 
    print("Your Grade is B+")
elif(Percentage >= 60):
    print("Your Grade is B")
elif(Percentage >= 50):
    print("Your Grade is C")
elif(Percentage >= 40):
    print("Your Grade is D")
else:
    print("You are Fail")