###############
# Adapter
# Convert the interface of a class into another interface clients expect.
# Adapter lets classes work together that couldn't otherwise because of incompatibleinterfaces
###############

#Target -> defines the domain-specific interface that client uses
class Target:
    def interface(self):
        pass

#Adaptee -> defines an existing interface that needs adapting
class Adaptee:
    def specificInterface(self):
        print("call specific interface")

#Adapter -> adapts the interface of Adaptee to the Target interface
class Adapter(Target):
    adaptee = Adaptee()
    def __init__(self, adaptee=None):
        if adaptee:
            self.adaptee = adaptee
    def interface(self):
        self.adaptee.specificInterface()

#main
if __name__ == "__main__":
    adapter = Adapter()
    adapter.interface()
