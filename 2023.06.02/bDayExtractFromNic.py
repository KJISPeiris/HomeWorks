NIC = input("Enter your NIC number: ")

if len(NIC) == 12 or (len(NIC)==10 and (NIC[9] == 'v' or NIC[9] == 'V')):
    if len(NIC) == 12:
        year = int(NIC[0:4])
        days = int(NIC[4:7])
    else:
        year = int("19" + NIC[0:2])
        days = int(NIC[2:5])
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        numberOfDaysInFeb = 29
    else:
        numberOfDaysInFeb = 28
    if days > 500:
        gender = "Female"
        days -= 500
    else:
        gender = "Male"
    monthDays = [31, numberOfDaysInFeb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if days > 0 and days <= 366:
        month = 0
        while days > monthDays[month]:
            days -= monthDays[month]
            month += 1
        month += 1
    else: 
        print("Invalid NIC number")
    print("Date of Birth: " + str(year) + "-" + str(month) + "-" + str(days-1))
    print("Gender: " + gender)
else:
    print("Invalid NIC number")