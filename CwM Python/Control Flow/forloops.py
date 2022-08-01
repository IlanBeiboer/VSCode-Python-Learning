successful = True
for number in range(1, 4):
    print("attempt", number, number * ".")
    if successful:
        print("successful")
        break
else:
    print("Failed")
# else statement only works when successful == False. Break makes it so, if succesful == True else will not work.
# If break is removed, output will repeat 3 times and then report Failed
# range (Begin number, any number before this number, so (number - 1), the step length, so if range(2, 7, 2) range = 2, 4 ,6)