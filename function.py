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

def income_function(householdIncomeInput):
    householdIncomeInput = input("What is your household income? ")
    if householdIncomeInput <= 25000 and genderInput == "male":
     print("You can live 73-76 years old ")
    elif householdIncomeInput <= 25000 and genderInput == "female":
     print("You can live 78-81 years old")
    else:
     print("You can live 78.5 years old")
    
    if householdIncomeInput >= 28000 and householdIncomeInput <= 25000 and genderInput == "male":
      print("You can live 78 years old")
    elif householdIncomeInput >= 28000 and genderInput == "female":
      print("You can live 83 years old")
    else:
        print("You can live 80.5 years old")
    
    if householdIncomeInput >= 46120 and householdIncomeInput <= 25000 and genderInput == "male":
       print("You can live 80 years old")
    elif householdIncomeInput >= 46120 and householdIncomeInput <= 28000  and genderInput == "female":
       print("You can live 84 years old")
    else:
        print("You can live 82 years old")
    if householdIncomeInput >= 74000 and householdIncomeInput <= 46120 and genderInput == "male":
       print("You can live 82 years old")

    elif householdIncomeInput >= 74000 and householdIncomeInput <= 46120 and genderInput == "female":
       

    if homeData1 == "USA" and smokingInput == "yes" and genderInput == "male":
      print("Your life expectancy is around 50-65 years")









