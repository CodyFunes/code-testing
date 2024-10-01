money_str = float(input("please enter the amount of money you have to spend"))
travel_str = float(input('please enter thr cost of plane'))
hotel_str = float(input("please enter thr cost of hotel"))

money_left = money_str - travel_str - hotel_str

if money_left < 200:
    print("you cant go you will have:", money_left)
else:
    print("you can go and this is how much extra you have", money_left)