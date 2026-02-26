# Private (getter, setter)
class Temp:
    __var=10
    def get(self):
        print(self.__var)
    def set(self, new_val):
        self.__var=new_val
obj=Temp()
obj.get() #10
obj.set(50) 
obj.get() #50 