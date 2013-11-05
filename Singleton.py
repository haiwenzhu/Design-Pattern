###############
# Singleton
# Ensure a class has only one instance, and provide a global point to access it.
###############

#Singleton -> define an instance operation to let client access its unique instance
class Singleton:
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
            return cls._instance
    @classmethod
    def instance(cls):
        return cls._instance

#main
if __name__ == "__main__":
    instance1 = Singleton.instance()
    instance2 = Singleton.instance()
    if id(instance1) == id(instance2):
        print('same!')
    else:
        print('different!')
    
