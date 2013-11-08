###############
# Bridge
# Decouple an abstraction from its implementation so that the two way can vary independently
###############

# Abstraction -> defines the abstraction interface, and maintain a reference to an object of Implementor
class Abstraction:
    def __init__(self, implementor):
        self.implementor = implementor
    def operation(self):
        self.implementor.operationImp()

#RefineAbstractor -> extends the interface defined by abstraction
class RefineAbstraction(Abstraction):
    pass

#Implementor -> defines the interface for implementation classes
class Implementor:
    def operationImp(self):
        pass

#ConcreteImplementor -> implements the Implementor interface
class ConcreteImplementor(Implementor):
    def operationImp(self):
        print(self.__class__.__name__ + "'s operation implementaion")

#main
if __name__ == "__main__":
    ra = RefineAbstraction(ConcreteImplementor())
    ra.operation()
