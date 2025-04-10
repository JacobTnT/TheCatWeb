points = 0           
q1 = "1+1 "
q2 = "10+9 "
q3 = "54+57 "
q4 = "4x4 "
q5 = "0.72+0.28 "
q6 = "1/2 x 3/4 "
q7 = "a+3=5 "
q8 = "-3+5 "
q9 = "y + 3x - 1 = 0 "
q10 = "ax(squared) + bx + c = 0 "
q11 = "y = -3x + 4x + 4y = -6 " 
q12 = "In a right triangle ABC, where C is the right angle, if side AB (the hypotenuse) is 10 units long and angle A is 30 degrees, find the length of side BC (the side opposite to angle A). "
q13 = "A ball's height in feet after t seconds is: h(t) = -16t^2 + 64t. Find: a) Velocity at time t.  b) Time at max height.  c) Max height. d) Acceleration at time t. "


answer1 = input(q1)
answer2 = input(q2)
answer3 = input(q3)
answer4 = input(q4)
answer5 = input(q5)
answer6 = input(q6)
answer7 = input(q7)
answer8 = input(q8)
answer9 = input(q9)
answer10 = input(q10)
answer11 = input(q11)
answer12 = input(q12)
answer13 = input(q13)

if (answer1 == "2" or answer2 == "19" or answer3 == "111" or answer4 == "16" or answer5 == "3/8" or answer6 == "a=2" or answer7 == "2" or answer8 == "2" or answer9 == "dy/dx = -3" or answer10 == "x = (-b ± √(b^2 - 4ac)) / 2a" or answer11 == "x = 2, y = -2" or answer12 == "BC = 5"):
    print("Correct!")
    points == 100
    print(f"Your points: {points}")
    
else:
    print("Incorrect!")
    print("Checking answers...")
    if answer1 == "2":
        points += 7.69
    if answer2 == "19":
        points += 7.69
    if answer3 == "111":
        points += 7.69
    if answer4 == "16":
        points += 7.69
    if answer5 == "1":
        points += 7.69
    if answer6 == "3/8":
        points += 7.69
    if answer7 == "2":
        points += 7.69
    if answer8 == "2":
        points += 7.69
    if answer9 == "-3":
        points += 7.69
    if answer10 == "x = (-b ± (b**2 - 4ac)**0.5) / 2a":
        points += 7.69
    if answer11 == "(2, -2)":
        points += 7.69
    if answer12 == "5":
        points += 7.69
    if answer13 == "a) v(t) = -32t + 64, b) 2, c) 64, d) -32":
        points += 7.69
    print(f"Your points: {points} out of 100")
    print()
    print("Thank you for taking the quiz!")