###############
# AbstractFactory
# AbstractFactory provide an interface for creating families of relate or dependent objects without specifying their concrete classes
###############

#declares an interface for operations that create abstract product object.
#client use this interface to get the product they want but no need to know the product name.
class AbstractFactory:
    def createProductA(self):
        pass
    def createProductB(self):
        pass

#ConcreteFactory
#ConcreteFactory implements the operations defined by abstract factory to create concrete products.
class ConcreteFactory1:
    def createProductA(self):
        return ProductA1()
    def createProductB(self):
        return ProductB1()
class ConcreteFactory2:
    def createProductA(self):
        return ProductA2()
    def createProductB(self):
        return ProductB2()

#The following is Abstract product
#Abstract product declares an interface for a type of product
#client use this interface to operation product.
class AbstractProductA():
    def operation(self):
        pass
class AbstractProductB():
    def operation(self):
        pass

#ConcreteProduct
#ConcreteProduct implements the of AbstractProduct interface
#ConcreteFactory create object use ConcreteProduct
class ProductA1():
    def operation(self):
        print("call " + self.__class__.__name__ + "'s operation method")
class ProductB1():
    def operation(self):
        print("call " + self.__class__.__name__ + "'s operation method")
class ProductA2():
    def operation(self):
        print("call " + self.__class__.__name__ + "'s operation method")
class ProductB2():
    def operation(self):
        print("call " + self.__class__.__name__ + "'s operation method")

#Client
#Client use only interfaces declared by AbstractFactory and AbstractProduct
class Client:
    def __init__(self):
        self.factory = AbstractFactory()
    def setFactory(self, factory):
        self.factory = factory
    def run(self):
        self.factory.createProductA().operation()
        self.factory.createProductB().operation()

if __name__ == '__main__':
    client = Client()
    client.setFactory(ConcreteFactory1())
    client.run()
    client.setFactory(ConcreteFactory2())
    client.run()
