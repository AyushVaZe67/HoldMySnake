class Myclass:
    def __init__(self,value):
        self._value = value

    def show(self):
        print(self._value)

    @property
    def ten_value(self):
        return 10 * self._value

    @ten_value.setter
    def ten_value(self,new_value):
        self._value = new_value / 10


obj = Myclass(50)
obj.ten_value = 69
print(obj.ten_value)
obj.show()