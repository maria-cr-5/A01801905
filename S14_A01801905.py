age = int(input("Please enter your age:"))
if age < 0:
 print("Age not valid")
if age < 18:
 print("Valid age")   
  
age = int(input("Please enter your age:"))
if 13 <= age and age <= 19:
  print("You are a teenager")
else:
 print("You are not a teenager")

age_input = int(input("Please enter your age: "))
actual_year = 2025
birth_year_approx = actual_year - age_input
print(birth_year_approx)
