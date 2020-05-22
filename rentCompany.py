
codeString = input("Enter any code to start and q or Q to end: \n")

Budeget = 0
Days = 0
charge= 0
mile = 0
weeks =  0
mileIntheStart = 0
mileAtTheEnd= 0

while (codeString != ("Q" )) and codeString != "q" :
    codeString = input("Enter (b or B to the budget plan)(d or D to the daily plan) (w or W to the weekly plan) "
                       "(q or Q to end)): \n")

    if codeString == "B" or codeString =="b":
        print("Enter the number of days: ")
        Days = int(input())
        charge = (Days * 40)
        mileIntheStart = int(input("Enter the mile at the start of the rental  : \n"))
        mileAtTheEnd = int(input("Enter the mile at the end of rental \n"))
        mile = mileAtTheEnd - mileIntheStart
        print("The vichle was rented for ", Days, "days")
        print("The vichle mile read at the start of rent is ", mileIntheStart, "miles")
        print("The vichle mile read at the end of the rent is ", mileAtTheEnd,"miles")
        print("The mile driven by the costumer is ", mile, "miles")
        charge = charge + (mile*0.25)
        print("The total charge is " , charge )


    elif codeString == "D" or codeString == "d":
        print("Enter the number of days ")
        Days = int(input())
        charge = 190 * Days
        mileIntheStart = int(input("Enter the mile at the start of the rental  : \n"))
        mileAtTheEnd = int(input("Enter the mile at the end of rental \n"))
        mile = mileAtTheEnd - mileIntheStart
        print("The vichle was rented for ", Days, "days")
        print("The vichle mile read at the start of rent is ", mileIntheStart, "miles")
        print("The vichle mile read at the end of the rent is ", mileAtTheEnd, "miles")
        print("The mile driven by the costumer is ", mile,"miles")

        if mile > 100 :
            charge = charge + ((mile-100)*0.25)

        print("The total charge is " , charge )



    elif codeString == "w" or codeString =="d":
        print("Enter the number of weeks ")
        weeks = int(input())
        charge = 190 * weeks
        mileIntheStart = int(input("Enter the mile at the start of the rental  : \n"))
        mileAtTheEnd = int(input("Enter the mile at the end of rental \n"))
        mile = mileAtTheEnd - mileIntheStart

        print("The vichle was rented for ", weeks, "weeks")
        print("The vichle mile read at the start of rent is ", mileIntheStart, "miles")
        print("The vichle mile read at the end of the rent is ", mileAtTheEnd,"miles")
        print("The mile driven by the costumer is ", mile ,"miles")
        if mile > 900 and mile < 1500:
         charge = charge + (weeks * 100)
        elif mile > 1500:
            charge = charge+(weeks *200)+((mile-1500) * 0.25)
        print("The total charge is " , charge )



print("Done")
