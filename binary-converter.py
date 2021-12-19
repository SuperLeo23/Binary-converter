print("""
Thank you for using this binary converter!
""")
def start():
    while True:
        try:
            original = int(input("Number to convert: "))
        except:
            print("Unvalid character")
            start()
        result = ""
        def isInteger(num):
            num = (int(num)/2)
            return(float(num).is_integer())

        while int(original) > 0:
            isInt = (isInteger(original))
            original = int(original) / 2
            if isInt == True:
                result += "0"
            else:
                result += "1"
        if original == 1:
            result += "1"
        else:
            result += "0"
        if result != "0":
            print(result[::-1])
start()