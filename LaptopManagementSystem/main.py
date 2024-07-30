#importing important function from different files
from read import readingfilesrenting
from read import readingFilesreturn
from operations import option1
from operations import option2

    

while True:
  #welcome message
  print("~ ~ ~ ~ ~ ~ ~ ~ Welcome to TechnoPropertyNepal ~ ~ ~ ~ ~ ~ ~ ~ ~ ")
  print("\n")
  print("Choose from the options below!")
  print("-------------------------------------------------------+")
  print("Press (1) to Rent Land                                 |")
  print("Press (2) to Return the Rented Land                    |")
  print("Press (3) to Exit the system                           |")
  print("-------------------------------------------------------+")
  
 
  # ask the user to input 1/2/3
  userInput = (input("Enter a number (1/2/3) --->: "))
  print("----------------------------------------------------------------------------------------------")
  #if user type 1 then two function will be called
  if userInput == "1" :
    readingfilesrenting()
    option1()  
  #if user type 2 then two function will be called
  elif userInput == "2" :
    readingFilesreturn()
    option2()
  #if user types 3 then the system will get terminated
  elif userInput == "3" :
    print("Thank for using the System. We hope you have a wonderfull day!!")
    break
  #instead of giving 1/2/3 user give 5 then this message will get displayed
  else:
    print("----------------------------------------------------------------------------------------------")
    print('Option' ,userInput, 'is not valid. Please choose from (1/2/3)')
  

