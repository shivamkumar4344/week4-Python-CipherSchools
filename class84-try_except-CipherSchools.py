while True:
    try:
        age = int(input("Enter the age:-"))
        break
    except TypeError:
        print("You have entered string instead of number..,try again.")
    except:
        print("unexpected error..")
        
if age < 18:
    print("You can't vote.")
else:
    print("You can vote.")