print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
num = int(input("How many people to split the bill? "))
total = bill + (tip*bill)/100
amtperperson = total/num
amtperperson = round(amtperperson, 2)
print(f"Each person should pay: ${amtperperson}")
