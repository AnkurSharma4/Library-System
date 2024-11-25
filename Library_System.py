print("                                                 Skill Circle Library System                                                         ")
def cont():
    b=int(input("Do you wish to continue?\nPress 1 for Again\nPress 2 to Exit"))
    if (b==2):
        print("Goodbye")    
    else :
        books()
def books():
    a=int(input("Press 1 for 101 Book Information\nPress 2 for 102 Book Information\nPress 3 for 103 Book Information\nPress 4 for 104 Book Information\nPress 5 for 105 Book Information\nPress 6 for 106 Book Information"))
    if (a==1):
        print("Book Title:-Diary of a Wimpy Kid, The Ugly Truth\nAthhor:-Jeff Kinney\n  Price:-$5.00")
        cont()
    elif (a==2):
        print("Book Title:-Diary of a Wimpy Kid, The Third Wheel\nAthhor:-Jeff Kinney\n  Price:-$4.00")
        cont()
    elif (a==3):
        print("Book Title:-Diary of a Wimpy Kid, Hard Luck\nAthhor:-Jeff Kinney\n  Price:-$7.00")
        cont()
    elif (a==4):
        print("Book Title:-Diary of a Wimpy Kid, Double Down\nAthhor:-Jeff Kinney\n  Price:-$14.00")
        cont()
    elif (a==5):
        print("Book Title:-Diary of a Wimpy Kid, The Getaway\nAthhor:-Jeff Kinney\n  Price:-$18.85")
        cont()
    elif (a==6):
        print("Book Title:-Diary of a Wimpy Kid, Wrecking Ball\nAthhor:-Jeff Kinney\n  Price:-$15.25")
        cont()
books()
        
