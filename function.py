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

if homeData1 == "USA" or "Czech Republic" or "Oman" or "Kuwait" or "Costa Rica" or "Maldives" or "Chile" or "Bahrain" or "UK" or "United Kingdom" or "Germany" or "Slovenia" or "Cyprus" or "Puerto Rico" or "Greece" or "Finland" or "Denmark" or "Austria" or "New Zealand" or "Guadeloupe" or "Belgium" or "Netherlands" or "Luxembourg" or "Qatar" or "Portugal" or "Ireland" or "Isreal" or "Canada" or "Martinique" or "Iceland" or "UAE" or "Macao" or "Sweden" or "Norway" or "Malta" or "Reunion" or "Spain" or "Singapore" or "Italy" or "Australia" or "Switzerland" or "French Polynesia" or "South Korea" or "Japan" or "Hong Kong" and smokingInput == "yes" and genderInput == "male":
    print("Your life expectancy is around 50-65 years")

# Compare the life expectancy of the user with the life expectancy of the country they live in until final result is reached
#if homeData1 == "Czech Republic" or "Oman" or "Kuwait" or "Costa Rica" or "Maldives" or "Chile" or "Bahrain" or "UK" or "United Kingdom" or "Germany" or "Slovenia" or "Cyprus" or "Puerto Rico" or "Greece" or "Finland" or "Denmark" or "Austria" or "New Zealand" or "Guadeloupe" or "Belgium" or "Netherlands" or "Luxembourg" or "Qatar" or "Portugal" or "Ireland" or "Isreal" or "Canada" or "Martinique" or "Iceland" or "UAE" or "Macao" or "Sweden" or "Norway" or "Malta" or "Reunion" or "Spain" or "Singapore" or "Italy" or "Australia" or "Switzerland" or "French Polynesia" or "South Korea" or "Japan" or "Hong Kong":
   # print("Your life expectany is more or equal than 80 years")
#elif homeData1 == "Panama" or "Albania" or "USA" or "United States" or "Estonia" or "Saudi Arabia" or "New Caledonia" or "Poland" or "Croatia" or "Slovakia" or "Uruguay" or "Cuba" or "Bosnia and Herzegovina" or "Jordan" or "Peru" or "Columbia" or "Lebanon" or "Iran" or "Antigua and Barbuda" or "Sri Lanka" or "Turkey" or "Ecuador" or "Argentina" or "North Macedonia" or "Guam" or "Montenegro" or "French Guiana" or "Hungary" or "Curacao" or "Serbia" or "Malaysia" or "Tunisia" or "Thailand" or "Algeria" or "Aruba" or "Barbados" or "Latvia" or "Mayotte" or "Cabo Verde" or "Lithuania" or "Romainia" or "Brazil" or "Armenia" or "Bulgaria" or "U.S Virgin Islands" or "Morocco" or "Brunei" or "Grenada" or "Mexico" or "Mauritius" or "Nicaragua" or "Bangladesh" or "Vietnam" or "Ukraine" or "Bahamas" or "Georgia" or "Belarus" or "Azerbaijian" or "Kazakhstan" or "Paraguay" or "Dominican Republic" or "Belize" or "Suriname" or "North Korea" or "Triniadad and Tobago" or "Bhutan" or "Russia" or "Tonga" or "Honduras" or "Libya" or "Seychelles" or "State of Palestine" or "Saint Lucia" or "Syria" or "Guatemala" or "Venezuela" or "Uzbekistan" or "Iraq" or "El Salvador" or "India" or "Mongolia" or "Tajikistan" or "Egypt" or "Samoa" or "Micronesia" or "Vanuatu" or "Western Sahara" or "Jamaica" or "Saint Vincent and the Grenadines" or "Moldova" or "Indonesia" or "Cambodia" or "Nepal" or "Solomon Inslands" or "Guyana" or "Turkmenistan" or "Sao Tome & Principe" or "Philippines": 
     #print("Your life expectancy is more or equal than 70 years")
#else:
    #print("Your life expectancy is less than 70 years")












