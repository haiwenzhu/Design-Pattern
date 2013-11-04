###############
# Prototype
# Specify the kinds of object to create by using a prototypical instance, and create new object by copying this prototype
###############

#Prototyep -> declare an interface for cloning itself
class Prototype:
    def clone(self):
        return self.__class__()

#ConcretePrototype -> implementation the interface for cloning itself
class ConcretePrototype1(Prototype):
    def operation(self):
        print(self.__class__.__name__)
class ConcretePrototype2(Prototype):
    def operation(self):
        print(self.__class__.__name__)

#Client -> create new object by ask prototype to clone itself
class Client:
    def operation(self, prototype):
        object = prototype.clone()
        object.operation()

#main
if __name__ == "__main__":
    client = Client()
    prototype1 = ConcretePrototype1()
    client.operation(prototype1)
    prototype2 = ConcretePrototype2()
    client.operation(prototype2)
