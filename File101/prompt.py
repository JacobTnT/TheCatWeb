def lifeSpan(age, country, gender, diet, grandparentAge, smoking):
 userInput = f"I am {age} from {country}, and I am {gender}. My diet is {diet}, My grandparents ages are {grandparentAge}."
 print(userInput)
 return userInput

userInput1 = lifeSpan(5, "USA", "Men", "Protein", "57 and 59", "No")
userInput2 = lifeSpan(25, "Canada", "Women", "McDonalds", "73 and 71", "Yes I Smoke")
userInput = userInput1 + userInput2
if "McDonalds" in userInput:
 print(f"\nAround 60 years with the McDonalds eating")
if "Protein" in userInput:
 print(f"\nAround 70 years for the nice protein")
