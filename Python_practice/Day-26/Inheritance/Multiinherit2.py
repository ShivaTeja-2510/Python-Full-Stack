class Frontenddev:
    def Developfrontend(self):
        print("Develop frontend app with HTML, CSS and React")

class Backenddev:
    def Developbackend(self):
        print("Develop backend app with Flask and Python")

class FullStackDev(Frontenddev, Backenddev):
    def DeployFullStack(self):
        print("Deploy full stack app on Cloud Platform")

f=FullStackDev()
f.Developfrontend()
f.Developbackend()
f.DeployFullStack()