class validation:

    @staticmethod
    def isInt(val):
        try:
            int(val)
            return True
        except:
            return False
        

    @staticmethod
    def isPositive(val):
        if not validation.isInt(val):
            return "Value should be number"
        return val >= 0


    @staticmethod
    def a_bigger_b(a, b):
        if a == b:
            return False
        return a > b


    @staticmethod
    def Exit(val):
        if val != 'exit':
            print("If you want to exit, type 'exit'")
        else:
            exit()


    @staticmethod
    def get_strictly_positive():
        while True:
            num = validation.get_positive_number()
            if num == 0:
                print("Value can't be a zero")
                continue
            return num

    
    @staticmethod
    def get_positive_number():
        while True:
            num = input()
            if not validation.isInt(num):
                print("Value should be a number")
                # validation.Exit(num)
                continue
            num = int(num)

            if not validation.isPositive(num):
                print("Value should be a positive number")
                # validation.Exit(num)
                continue
            return num


    @staticmethod
    def get_number():
        while True:
            num = input()
            if not validation.isInt(num):
                print("Value should be a number")
                # validation.Exit(num)
                continue
            return int(num)


    @staticmethod
    def get_index(len):
        while True:
            index = input()
            
            if not validation.isInt(index):
                print("Value should be a positive integer")
                validation.Exit(index)
                continue
            index = int(index)
            if index < 0 or index >= len:
                print("invalid index")
                continue
            
            return index
