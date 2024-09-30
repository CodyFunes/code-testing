print("This program will determine if both students are taking 15 credits")

bob_credits = int(input("Please enter the number of Bob's credits:"))
mary_credits = int(input("Please enter the number of Mary's credits:"))

print("Are bob and mary taking at least 15 credits:")

totalcredit = "Yes"
if bob_credits and mary_credits >= 15:
    totalcredit= "Yes"
elif bob_credits and mary_credits < 15:
    totalcredit= "No"

print(totalcredit)


23