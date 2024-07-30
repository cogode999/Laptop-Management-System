#importing important function 
from read import readingfilesrenting
from read import readingFilesreturn
from datetime import datetime


# Generate a timestamp to create a unique filename
current_date1 = datetime.now().strftime("%Y-%m-%d")
timestamp1 = datetime.now().strftime("%H:%M:%S")

land_dictionary = {}

# option1 renting the lands 
def option1():
    while True:
        timestamp = datetime.now().strftime("%Y%m%d_%H-%M-%S")
        current_date = datetime.now().strftime("%Y-%m-%d")
        take_input2 = (input("\nEnter the Land Id or Type 'e' to exit -->: "))
        if take_input2 == "e":
            print("----------------------------------------------------------------------------------------------")
            break
        else:
         try:
             land_id = int(take_input2)
         except ValueError:
             print("----------------------------------------------------------------------------------------------")
             print("Invalid input! Enter a valid Land Id.")
             print("----------------------------------------------------------------------------------------------")
             continue
         with open("lands.txt", "r") as file:
              lines = file.readlines()
              if land_id <= len(lines):
                  lands = lines[int(take_input2) - 1].strip().split(",")
                  kitta, city, direction, anna, price, availability = lands
                  price = float(price.replace('$', '').strip())
                  print("----------------------------------------------------------------------------------------------")
                  print(f"You choosed land in {city} with {kitta} kitta and {anna} anna")
                  print("----------------------------------------------------------------------------------------------")
                  renting_quantity = int(input("Enter the quantity you want to Rent -->: "))
                  print("----------------------------------------------------------------------------------------------")
                  #if the quntity is equal to renting quantity then only the system will go further otherwise it will not
                  if renting_quantity == int(anna):
                           total_price = price * renting_quantity
                           customerName = str(input("Enter your name for billing -->: "))
                           print("----------------------------------------------------------------------------------------------")
                           address = str(input("Enter your address -->: "))
                           print("----------------------------------------------------------------------------------------------")
                           phoneNo = int(input("Enter your Phone Number -->: "))
                           print("----------------------------------------------------------------------------------------------")
                        
                           confirmation = str(input("Type 'confirm' to rent the Land. Type 'cancel' to cancel the process. -->: "))
                           print("----------------------------------------------------------------------------------------------")
                           grandTotal = total_price
                           #if typed confirm then only the stock will be updated 
                           if confirmation == "confirm":
                                # Update the quantity in the dictionary
                                updated_anna= int(anna) -renting_quantity
                                land_dictionary[int(take_input2)] = [kitta, city, direction, str(int(anna) - renting_quantity), price, "Not Available" if updated_anna == 0 else availability]
                                # Update the quantity in the text file
                                land_line = ",".join(str(item) for item in land_dictionary[int(take_input2)]) + "\n"
                                lines[int(take_input2) - 1] = land_line
                                # Update the availability in the invoice
                                availability_status = "Not Available" if updated_anna == 0 else availability
                                #making sale invoice
                                with open("lands.txt", "w") as outfile:
                                 outfile.writelines(lines)
                                # Open the file in write mode
                                filename = f"rent_{timestamp}.txt"
                                with open(filename, mode='w') as f:
                                 f.write("\n\t\t\t\t\t\t\tTechnoPropertyNepal")
                                 f.write("\n\t\t\t\t\tKapan, Phone No: 01-9587444")
                                 f.write("\n                  Email: Techno@gmail.com")
                                 f.write("\n")
                                 f.write(f"\n                                                  Date:{current_date}")
                                 f.write(f"\n                                                  Time:{timestamp}")
                                 f.write("\n+------------------------------------------------------------------------")
                                 f.write(f"\n|  Customer Name : {str(customerName)}                          Sale Invoice")
                                 f.write(f"\n|        Address : {str(address)}")                      
                                 f.write(f"\n|       Phone No : {int(phoneNo)}")
                                 f.write("\n+------------------------------------------------------------------------")
                                 f.write(f"\n|    Kitta No : {kitta}")                      
                                 f.write(f"\n|    City/District :{city}")
                                 f.write(f"\n|    Direction : {direction}")
                                 f.write ("\n|    Duration : ( None")
                                 f.write(f"\n|    Anna : {renting_quantity}") 
                                 f.write("\n+------------------------------------------------------------------------")
                                 f.write(f"\n|    Price Per Anna : {price}")
                                 f.write("\n+------------------------------------------------------------------------")
                                 f.write(f"\n|    Grand Total : {grandTotal}")
                                 f.write("\n+-----------------------------------------------------------------------")
                                 f.write("\n|                       Thank You For Choosing Us ")
                                 f.write("\n|                               TechnoPropertyNepal       ")
                                 f.write("\n+------------------------------------------------------------------------")                          
                                 print(f"You have successfully Rented {renting_quantity} anna in {city} city. We have generated the invoice for you!")
                                 print("----------------------------------------------------------------------------------------------")
                                #option if user want to rent land again or not.
                                buyAgain = str(input("Do you want to Rent More Lands (yes/no) -->: "))
                                if buyAgain == "yes":
                                 readingfilesrenting()
                                 option1()
                                 break 
                                else:
                                 print("----------------------------------------------------------------------------------------------")
                                 print("Returning you to our main system")
                                 print("----------------------------------------------------------------------------------------------")
                                 break
                           else: 
                               print("Since you choose to cancel the process we have redirected you to our main system")
                               print("----------------------------------------------------------------------------------------------")
                               break
                  #if user gives renting quntity less than or equal to 0 then it will show this message
                  elif renting_quantity <= 0:
                       print("Please Type positive quantity")
                       print("----------------------------------------------------------------------------------------------")
                       continue
                  else:
                    print(f"Sorry, {renting_quantity} anna of this land is not available")
                    print("----------------------------------------------------------------------------------------------")
                    userInput4 = str(input("We have other Land available with us do want to take a look again (yes/no) -->: "))
                    print("---------------------------------------------------------------------------------------------")
                    if userInput4.lower() == "yes":
                        readingfilesrenting()
                        option1()
                        break  
                    else:
                     break      
              else:
                print("----------------------------------------------------------------------------------------------")
                print(f"Land ID {int(take_input2)} is invalid! ")
                print("----------------------------------------------------------------------------------------------")
                userInputReturn = str(input("Type 'a' to select a Land again or if you want to return to the main system type 'r'-->: "))
                print("----------------------------------------------------------------------------------------------")
                if userInputReturn == "a":
                    readingfilesrenting()
                    option1()   
                else:
                    break
 
         
#option 2 for returning the land              
def option2():
    while True:
        #for creating new file everytime when a return is done
        current_date = datetime.now().strftime("%Y-%m-%d")
        timestamp2 = datetime.now().strftime("%H:%M:%S")
        take_input2 = input("\nEnter the Land Id or Press 'e' to exit -->: ")
        #if user types e the system will go to main file
        if take_input2 == "e":
            print("----------------------------------------------------------------------------------------------")
            break
        else:
            #if user types string value in integer place then try/except is used to show the error and continue again
            try:
                land_id = int(take_input2)
            except ValueError:
                print("----------------------------------------------------------------------------------------------")
                print("Invalid input! Enter a valid Land Id.")
                print("----------------------------------------------------------------------------------------------")
                continue

            with open("lands.txt", "r") as file:
                lines = file.readlines()
                if land_id <= len(lines):
                    lands = lines[land_id - 1].strip().split(",")
                    kitta, city, direction, anna, price, availability = lands
                    price = float(price.replace('$', '').strip())
                    print("----------------------------------------------------------------------------------------------")
                    print(f"You have chosen to return the land with Kitta No: {kitta} located in {city} city/region, comprising a total of {anna} anna.")
                    print("----------------------------------------------------------------------------------------------")
                    return_quantity = int(input("Enter the quantity you want to Return -->: "))
                    print("----------------------------------------------------------------------------------------------")
                    #if only the return quantity is greater than or equal to 1 
                    if return_quantity >= 1:
                        total_price = price * return_quantity
                        custName = str(input("Enter your name for Billing: --> "))
                        print("----------------------------------------------------------------------------------------------")
                        custAddress = str(input("Enter your Address: --> "))
                        print("----------------------------------------------------------------------------------------------")
                        custPhone = int(input("Enter your Phone Number: --> "))
                        print("----------------------------------------------------------------------------------------------")
                        confirmation = str(input("Type 'confirm' to return the Land. Type 'cancel' to stop the Returning Process. -->: "))
                        print("----------------------------------------------------------------------------------------------")
                        # if confirmation is confirmed then the land will be returned otherwise it will not
                        if confirmation.lower() == "confirm":
                             # Update the quantity in the dictionary
                             land_quantity = int(anna) + return_quantity
                             new_availability = "Available" if land_quantity > 0 else "Not Available"
                             land_dictionary[int(take_input2)] = [kitta, city, direction, str(int(anna) + return_quantity), price, new_availability]
                             # Update the quantity in the text file
                             land_line = ",".join(str(item) for item in land_dictionary[int(take_input2)]) + "\n"
                             lines[land_id - 1] = land_line
                             with open("lands.txt", "w") as outfile:
                                outfile.writelines(lines)
                                print(f"Land with Kitta No: {kitta} in {city} city/region has been successfully returned. The total area returned is {return_quantity} anna. We have generated the invoice for you!")
                                # Open the file in write mode
                                filename = f"return_{timestamp2}.txt"
                                #making purchase invoice
                                with open(filename, mode='w') as f:
                                 f.write("\n\t\t\tTechnoPropertyNepal")
                                 f.write("\n\t\tKapan, Phone No: 01-9587444")
                                 f.write("\n\t\t\tEmail: Techno@gmail.com")
                                 f.write("\n")
                                 f.write(f"\n                                                  Date:{current_date}")
                                 f.write(f"\n                                                  Time:{timestamp2}")
                                 f.write("\n+------------------------------------------------------------------------")
                                 f.write(f"\n|  Customer Name : {str(custName)}                     Return Invoice")
                                 f.write(f"\n|        Address : {str(custAddress)}")
                                 f.write(f"\n|       Phone No : {int(custPhone)}")
                                 f.write("\n+------------------------------------------------------------------------")
                                 f.write(f"\n|    Kitta No : {kitta}")                 
                                 f.write(f"\n|    City/District : {city}")
                                 f.write(f"\n|    Anna : {return_quantity}")
                                 f.write(f"\n|    Direction : {direction}")
                                 f.write("\n|    Duration : ( None")
                                 f.write("\n      Fine : None ")
                                 f.write(f"\n|    Price Per Anna : {price}")
                                 f.write("\n+------------------------------------------------------------------------")
                                 f.write(f"\n|    Total Price : {total_price}")
                                 f.write("\n+------------------------------------------------------------------------")
                                 f.write(f"\n|    Grand Total : {total_price}")
                                 f.write("\n+------------------------------------------------------------------------")
                                 f.write("\n|                       Thank You For Choosing Us ")
                                 f.write("\n|                               TechnoPropertyNepal         ")
                                 f.write("\n+------------------------------------------------------------------------")

                                 print("----------------------------------------------------------------------------------------------")
                             #option is user want to return land again
                             returnAgain = str(input("Do you want to Return any other Lands? (yes/no) -->: "))
                             print("----------------------------------------------------------------------------------------------")
                             if returnAgain.lower() == "yes":
                                readingFilesreturn()
                                continue
                             else:
                                print("----------------------------------------------------------------------------------------------")
                                print("Returning you to our main system")
                                print("----------------------------------------------------------------------------------------------")
                                break
                        else:
                            print("Since you chose to cancel the process, we have redirected you to our main system")
                            print("----------------------------------------------------------------------------------------------")
                            break
                    else:
                        print("Please give us a positive quantity")
                        print("----------------------------------------------------------------------------------------------")
                        continue
                else:
                    print("----------------------------------------------------------------------------------------------")
                    print(f"Laptop ID {take_input2} is invalid!")
                    print("----------------------------------------------------------------------------------------------")
                    userInputReturn = str(input("Type 'c' to select a Land again or if you want to return to the main system type 'r'-->: "))
                    print("----------------------------------------------------------------------------------------------")
                    if userInputReturn.lower() == "c":
                        readingFilesreturn()
                        option2()
                    else:
                        break
                    
                    
                    
                    
                    
                    
                    
                    



         
         
         
         
         
         

         
         
         
         

       
         
         
         
       
    



    
    
    