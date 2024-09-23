hotel_rate = 155
age = input("what is your age")
age_int = int(age)
if age_int > 65:
    hotel_rate = hotel_rate - 20
print("your rate", hotel_rate)