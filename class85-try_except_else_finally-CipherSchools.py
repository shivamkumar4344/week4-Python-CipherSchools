while True:
    try:
        number = int(input("Enter a number:-"))
    except ValueError:
        print("Please enter the integer..")
    except:
        print("unexpected error!!")
    else:
        print(f"user input={number}")
        break
    finally:
        print("Ends here...43")
    
   
    