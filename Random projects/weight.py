weight = int(input("What is your weight: "))
unit = input ("(K)g or (L)bs? ")
if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))
else:
    convertedd = weight * 0.45
    print("Weight in Kgs: " + str(convertedd))
