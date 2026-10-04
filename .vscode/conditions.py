age=int(input("Enter your age:"))
country=(input("Enter your country name:")).capitalize()
if age>18:
   if country=="Pakistan":
      print("Eligible Voter!")
else:
   print("Not Eligible!")


date=input("Enter the date:")
if date=="29June":
      print("Available")
else:
   print("Select another date!")

117
marks=int(input("Enter your marks:"))
if (marks>90):
    print("A+")
elif marks>80:
    print("B+")
else:
    print("Try again")