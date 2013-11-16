###############
# Decorator
# Attach additional responsibilities to an object dynamically, Decorator provide a flexible alternative to subclassing for extending functionality.
###############

#Component -> defines the interface for objects that can have responsibilities add to then dynamically
class Component:
    def operation(self):
        print("do operation.")

#ConcreteComponent -> implement the interface defined by component
class ConcreteComponent(Component):
    def operation(self):
        print("do specific operation.")

#Decorator -> maintains a reference to Component object and defines an interface that conforms to Component's interface
class Decorator:
    def __init__(self, component):
        if isinstance(component, Component):
            self._component = component
        else:
            self._component = Component()

    def operation(self):
        self._component.operation()

#ConcreteDecorator -> add responsibilities to the component
class ConcreteDecorator(Decorator):
    def operation(self):
        self._component.operation()
        self.addResponsibility()
    def addResponsibility(self):
        print("do operation end.")

#main
if __name__ == "__main__":
    obj = ConcreteDecorator(ConcreteComponent())
    obj.operation()
