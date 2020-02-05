# !/usr/bin/python3.5

def addition():
    """Prompts for 2 numbers and adds the first to the second"""

    while True:

        print("\nEnter 'ctrl + c' or 'ctrl + d' to stop the program")

        try:
            num_1 = int(input("\nEnter a number, please:"))

        except ValueError:
            print("\nThats not a number, enter a number please")
        
        else:

            try:
                num_2 = int(input("\nEnter another number, please:"))

            except ValueError:
                print("\nThats not a number, enter a number please")

            else:
                
                result = num_1 + num_2

                print("\n  -- " + str(result) +" -- is the result you were asking for.")

addition()