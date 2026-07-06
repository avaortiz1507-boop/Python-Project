# 1 display menu
def display_menu():
    print("Welcome to the survey!")
    print("Please select an option:")
    print("1. Participate in the survey(yes/no)")
    print("2. Compare two numbers")
    print("3. Work with text")
    print("4. Exit")
# 2 loop through the menu until the user chooses to exit
running: bool = True
while running:
  
# 3 prompt user to select an option
  display_menu()
  option: str = input("Enter your option (1-4): ").strip()


# 4 validate user input
  if option not in ["1", "2", "3", "4"]:
    print("Invalid option. Please enter a choice between 1 and 4.")
    continue
  

  option: int = int(option)
  # 5 evaluate the corresponding option
  if option == 1:
    answer: str = input("Do you want to participate in the survey? (yes/no): ").strip().lower()
    response: bool = True if answer == "yes" else False
    if response:
      print("Thank you for agreeing to participate in the survey!")
    else:
      print("Thank you for your response. You have chosen not to participate in the survey.")
    pass
  elif option == 2:
    try:
      answer1: str = input("Enter the first number: ").strip()
      answer2: str = input("Enter the second number: ").strip()
      num1: float = float(answer1)
      num2: float = float(answer2)
    except ValueError:
      print("Invalid number. Please enter a valid number.")
    else:
      if num1 > num2:
        print(f"{num1} is greater than {num2}")
      elif num2 > num1:
        print(f"{num2} is greater than {num1}")
      else:
        print(f"{num1} and {num2} are equal")
    pass
  elif option == 3:
    text: str = input("What is your age? ")
    print(f"Your age is {text}")
    pass
  elif option == 4:
    # 6 exit survey
    running = False
    print("Thank you for using the survey. Goodbye!")



