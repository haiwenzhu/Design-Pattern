###############
# Proxy
# Provide a surrogate or placeholder for another object to control access to it.
###############

#Subject -> define common interface for RealSubject and Proxy so that a Proxy can be used anywhere  a RealSubject is expected.
class Subject:
    def request(self):
        pass

#RealSubject -> define the RealSubject that the Proxy Represents.
class RealSubject(Subject):
    def request(self):
        print('request in RealSubject.')

#Proxy -> provides a interface identical to Subject's and control access to it.
class Proxy(Subject):
    subject = None
    def request(self):
        if not self.subject:
            self.subject = RealSubject()
        self.subject.request()

#main
if __name__ == '__main__':
    obj = Proxy() #object is expected as a instance of subject
    obj.request()
