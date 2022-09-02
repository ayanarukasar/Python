class RailwayForm:
    formType="RailwayForm"

    def printData(self):
        print(f"Name is",self.name)
        print(f"Train is",self.train)

aamirsApplication =RailwayForm()
aamirsApplication.name="Aamir"
aamirsApplication.train="Rajdhani Express"

aamirsApplication.printData()