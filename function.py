userInput = input("Where do you live? ")
# functions for life expectancy
def homeFunction(userInput):
    HomeData1 = f"I live in the {userInput}"
    print(HomeData1)
    return HomeData1
    return userInput
homeData1 = homeFunction(userInput)

genderInput = input("Are you male or female? ")

def gender_function(genderInput):
    genderData = f"I am {genderInput}"
    print(genderData) 
    return genderData
 
gender_function(genderInput)

ageInput = input("How old are you? ")

def age_function(ageInput):
    ageData = f"I am {ageInput} years old"
    print(ageData)
    return ageData
age_function(ageInput)

smokingInput = input("Do you smoke? (yes/no) ")

def smoking_function(smokingInput):
    if smokingInput == "yes" or smokingInput == "Yes":
        smokingData = "I smoke"
    else:
        smokingData = "I do not smoke"
    print(smokingData)
    return smokingData
    return smokingInput
smoking_function(smokingInput)
householdIncomeInput = input("What is your household income? ")
if householdIncomeInput <= 25000 and genderInput == "male":
     print("You can live 73-76 years old ")
elif householdIncomeInput <= 25000 and genderInput == "female":
     print("You can live 78-81 years old")

#0+
if householdIncomeInput >= 28000 and householdIncomeInput <= 25000 and genderInput == "male":
      print("You can live 78 years old")
elif householdIncomeInput >= 28000 and genderInput == "female":
      print("You can live 83 years old")
   
#28000+
if householdIncomeInput >= 46120 and householdIncomeInput <= 28000 and genderInput == "male":
       print("You can live 80 years old")
elif householdIncomeInput >= 46120 and householdIncomeInput <= 28000  and genderInput == "female":
       print("You can live 84 years old")
#46120+
if householdIncomeInput >= 80610 and householdIncomeInput <= 46120 and genderInput == "male":
       print("You can live 81 years old")

elif householdIncomeInput >= 80160 and householdIncomeInput <= 46120 and genderInput == "female":
      print("You can live 86 years old")
    
    #80160+
if householdIncomeInput >= 115000 and householdIncomeInput <= 130000 and genderInput == "male":
       print("You can live 84 years old")
elif householdIncomeInput >= 115000 and householdIncomeInput <= 130000 and genderInput == "female":
       print("You can live 86 years old")

if householdIncomeInput >= 130000 and householdIncomeInput <= 200000 and genderInput == "male":
       print("You can live to 84 years old")
elif householdIncomeInput >= 130000 and householdIncomeInput <= 200000 and genderInput == "female":
       print("You can live 87 years old")
    #200000-286300
if householdIncomeInput >= 200000 and householdIncomeInput <= 286300 and genderInput == "male":
       print("You can live to 86 years old")
elif householdIncomeInput >= 200000 and householdIncomeInput <= 286300 and genderInput == "female":
       print("You can live 87 years old")
    
       








