#start
Taylorswift_points = 0
Kanyewest_points = 0

#middle

answer = input("Would you rather A) have a massive following on social media, or B) be a trendsetter in a totally different field, like fashion or design\n")
if answer == "A":
    Taylorswift_points += 1
elif answer == "B":
    Kanyewest_points += 1

answer = input("What lyrics do you like more A) It's new the shape of your body It's blue, or B) And I know it did damage cause the look in your eyes is killin me\n")
if answer == "A":
    Taylorswift_points += 1
elif answer == "B":
    Kanyewest_points += 1

answer = input("would you rather listen to A) story telling music, or B) personal journey music\n")
if answer == "A":
    Taylorswift_points += 1
elif answer == "B":
    Kanyewest_points += 1

answer = input("Would you rather A) Get a shout-out from a celebrety on social media, or B) A personalized Yeezy item from a celebrety?\n")
if answer == "A":
    Taylorswift_points += 1
elif answer == "B":
    Kanyewest_points += 1

answer = input("would you rather listen to a album A) with deeply personal connection, or B) one pushes boundaries with experimental sounds \n")
if answer == "A":
    Taylorswift_points += 1
elif answer == "B":
    Kanyewest_points += 1

#end

if Taylorswift_points > Kanyewest_points:
    print("You are a Taylor Swift fan")
elif Kanyewest_points > Taylorswift_points:
    print("You are a Kanye West fan")
elif Taylorswift_points == Kanyewest_points:
    print("You are a Kanye West fan and a Taylor Swift")

