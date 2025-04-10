cars = {
  "carA": "Price: $25,000",
  "carB": "Price: $10,000",
  "carA1": "Price: $20,000",
}
print(cars)
carInput = input("What car do you like? ").lower()

# Type of car

if (carInput == "A"):
  carA = {
    "carA": "Price: $25,000",
    "carA1": "Price: $20,000",
  }
  print(carA)
elif (carInput == " B"):
  carB = {
    "carB": "Price: $10,000",
  }
else:
  print("Sorry, Your car could not be found. ")

# Price

if (carInput == "Under $10,000"):
  under10000 = {
    "carB": "Price: $10,000"
  }
  print(under10000)
if (carInput == "Under $20,000"):
  under20000 = {
    "carA1": "Price: $20,000",
    "carB": "Price: $10,000",
  }
  print(under20000)
if (carInput == "Under $30,000"):
  cars = {
  "carA": "Price: $25,000",
  "carB": "Price: $10,000",
  "carA1": "Price: $20,000",
} 
  print(cars)
