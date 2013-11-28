###############
# Command
# Encapsulate a request as an object, thereby letting you parameterize clients with different requests, queue or log request, and support undoable operation.
###############

#Command -> declares an interface for executing operation
class Command:
    receiver = None
    def __init__(self, receiver):
        self.receiver = receiver
    
    def execute(self):
        pass

#ConcreteCommand -> define a binding between a Receiver object and an action
class ConcreteCommand(Command):
    def execute(self):
        self.receiver.action()

#Receiver -> know how to perform the operations associated with carrying out a request.
class Receiver:
    def action(self):
        print('do operation!')

#main
if __name__ == '__main__':
    command = ConcreteCommand(Receiver())
    command.execute()
