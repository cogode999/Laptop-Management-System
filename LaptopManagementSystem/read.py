#defining a function that later on helps to display all land available for renting
def readingfilesrenting():
   
 print( " ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Choose from the lands listed below ! ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ")
 print("+""-------------------------------------------------------------------------------------------------------------""+")
 print("| S.N. | {:<10}  |  {:<7} |  {:<9} | {:<8} |  {:<12}   | {:<9}  |".format("Kitta Number", "City/District", "Direction(Land Faced)", "Anna", "Price", "Availability"))
 print("+""-------------------------------------------------------------------------------------------------------------""+")
 
 with open("lands.txt", "r") as file:
     a = 1
     for line in file:
        lands = line.strip().split(",")
        kitta, city, direction, anna, price, availability = lands
        
        print("| {:<4} | {:<13} | {:<14} | {:<22} |   {:<6} |  {:<14} |{:<14} |".format(a, kitta, city, direction, anna, price, availability))
        a += 1

        print("+""-------------------------------------------------------------------------------------------------------------""+")
    


#defining a function that later on helps to display all lands for returning
def readingFilesreturn():
   
    print( " ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ Which Rented Land do you want to return ! ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ")
    print("\n")
    print("+""-------------------------------------------------------------------------------------------------------------""+")
    print("| S.N. | {:<10}  |  {:<7} |  {:<9} | {:<8} |  {:<12}   | {:<9}  |".format("Kitta Number", "City/District", "Direction(Land Faced)", "Anna", "Price", "Availability"))
    print("+""-------------------------------------------------------------------------------------------------------------""+")
 
    with open("lands.txt", "r") as file:
     a = 1
     for line in file:
        lands = line.strip().split(",")
        kitta, city, direction, anna, price, availability = lands
        
        print("| {:<4} | {:<13} | {:<14} | {:<22} |   {:<6} |  {:<14} |{:<14} |".format(a, kitta, city, direction, anna, price, availability))
        a += 1

        print("+""-------------------------------------------------------------------------------------------------------------""+")
     
     
