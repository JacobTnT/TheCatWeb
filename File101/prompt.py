prompt = "\nPlease enter the name of a city you have visited"
prompt += "\nEnter 'quit' if you would stop working and retire"

while True:
  city = input(prompt)

  if city == 'quit':
    break
  else:
    print(f"Id love to go to {city.title()}!")