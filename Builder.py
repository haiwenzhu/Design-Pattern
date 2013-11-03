###############
# Builder
# Seperate the construction of a complex object from its representation so that the same construction can make different representations
###############

#Builder -> declare an interface for creating parts of a product object
class Builder:
    def buildPart1(self):
        pass
    def buildPart2(self):
        pass
    def getResult(self):
        pass

#ConcreteBuilder -> constructs and assembles parts of the product by implementing the Builder interface and also responsbile for representing its create
class ConcreteBuilderA(Builder):
    def __init__(self):
        self.result = []
    def buildPart1(self):
        self.result.append("A_Part1")
    def buildPart2(self):
        self.result.append("A_Part2")
    def getResult(self):
        print("\n".join(self.result))
class ConcreteBuilderB(Builder):
    def __init__(self):
        self.result = []
    def buildPart1(self):
        self.result.append("B_Part1")
    def buildPart2(self):
        self.result.append("B_Part2")
    def getResult(self):
        print("\n".join(self.result))

#Director -> constructs an object using the Builder interface
class Director:
    def __init__(self, builder):
        self.builder = builder
    def construct(self):
        self.builder.buildPart1()
        self.builder.buildPart2()
        self.builder.getResult()

if __name__ == "__main__":
    director = Director(ConcreteBuilderA())
    director.construct()
    director = Director(ConcreteBuilderB())
    director.construct()
