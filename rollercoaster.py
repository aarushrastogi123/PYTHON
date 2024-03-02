print("THE ROLLERCOASTER RIDE")
height=int(input("Enter the height:"))
if height>120:
    print("You can ride the rollercoaster.")
    age=int(input("Enter the age of the customer:"))
    bill=0
    if(age<12):
        bill=100
        print("Kids Ticket: Rs 100")
    elif(12<=age<18):
        bill= 200
        print("Youth Tickets: Rs 200")
    elif(45<=age<=55):
        print("Midlife Crisis Tickets: Rs 0")
    else:
        bill=500
        print("Adult Tickets: Rs 500")

    want_photos=input("Do you want photos taken? Y or N:")
    
    if want_photos=="Y":
        bill+=50    

    print("Your final bill is:",bill)

else:
    print("Sorry, grow taller and then come back.")    
