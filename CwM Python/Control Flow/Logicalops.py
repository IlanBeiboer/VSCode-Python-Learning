
veel_geld = True
goed_crediet = True
student = True

 # If veel_geld AND goed_crediet == True, the statement counts.
if veel_geld and goed_crediet:
    print("Eligible")
else:
    print("Not Eligible")

# If veel_geld OR goed_crediet == True, the statement counts.
if veel_geld or goed_crediet:
    print("Eligible")
else:
    print("Not Eligible")   

# If student == True the NOT operator will make it False and vise versa
if not student:
    print("Eligible")
else:
    print("Not Eligible")  