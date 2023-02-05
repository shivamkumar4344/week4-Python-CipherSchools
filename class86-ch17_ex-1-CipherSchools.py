def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as err:
        print(err)
    except TypeError as err:
        print(err)
    except:
        print("Unexpected error..")

print(divide(4,0))