# encapusulation
class car:
    def __init__(self):
        self.__update()
    def drive(self):
        print("driving")
        
    def __update(self):
        print("update car")
blackcar=car()
blackcar.drive()
# blackcar.update()