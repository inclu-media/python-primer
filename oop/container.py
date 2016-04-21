class Container:
    __capacity = 0
    __level = 0
    __name = None

    '''
    Constructor
    ''' 
    def __init__(self, name, capacity):
        self.__capacity = capacity
        self.__name = name

    '''
    A Method: fill amount fluid into this container
    '''
    def fill(self, amount):
            if self.__level + amount > self.__capacity:
                print('Cannot hold this much')
                return False
            else:
                self.__level += amount;
                return True

    '''
    A Method: pour amount fluid from this container into a target container
    '''
    def pour(self, amount, target):
        if not isinstance(target, Container):
            print("Can only pour into containers")
        else:
            if self.__level < amount:
                print("There is not enough left for that")
            else:
                if target.fill(amount):
                    self.__level -= amount
                else:
                    print("The target cannot hold this much!")

    '''
    A Method: print the status of this container
    '''
    def status(self):
        print("Name: " + self.__name)
        print("Capacity: " + str(self.__capacity))
        print("Level: " + str(self.__level))
        print("----------------------\n\n")


pot = Container("Kaffeekanne", 20)
pot.fill(20)
pot.status()

cup = Container("Kaffeetasse", 5)
cup.status()

pot.pour(5, cup)
cup.status()
pot.status()






