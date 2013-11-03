###############
# FactoryMethod
# Factory Method define an interface for creating an object, but let subclass to decide which class to instantiate.in other words, Factory Method defer instantiation to its subclass.
###############

#Product -> define the interface of objects the factory method create
class Product:
    def action(self):
        pass

#ConcreteProduct -> implements the Product interface
class ConcreteProduct(Product):
    def action(self):
        print(self.__class__.__name__)

#Creator -> declare the factory method, which may has its default implementation
class Creator:
    def factoryMethod(self):
        #also can has its default implementation
        pass
    def operation(self):
        self.obj = self.factoryMethod()
        self.obj.action()
                         
#ConcreteCreator -> overrides the factory method to return a concreate product object
class ConcreteCreator(Creator):
    def factoryMethod(self):
        return ConcreteProduct()

#main
if __name__ == "__main__":
    creator = ConcreteCreator()
    creator.operation()
