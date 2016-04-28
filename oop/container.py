class Container:
    __capacity = 0
    __level = 0
    __name = None

    def __init__(self, name, capacity):
        """
        Construct a new container
        :param name: the name of the container
        :param capacity: amount of fluid fitting into the container
        """
        self.__capacity = capacity
        self.__name = name

    def fill(self, amount):
        """
        Fill fluid into the container
        :param amount: the amount of fluid to fill
        :return: True, False if over-capacity
        """
        if self.__level + amount > self.__capacity:
            print('Cannot hold this much')
            return False
        else:
            self.__level += amount
            return True

    def pour(self, amount, target):
        """
        Pour fluid into another container from this container
        :param amount: the amount of fluid to pour
        :param target: the target container
        :return: None
        """
        if not isinstance(target, Container):
            print("Can only pour into containers")
        else:
            if self.__level <= amount:
                print("There is not enough left for that")
            else:
                if target.fill(amount):
                    self.__level -= amount
                else:
                    print("The target cannot hold this much!")

    def status(self):
        """
        Print the status of a container
        :return: None
        """
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






