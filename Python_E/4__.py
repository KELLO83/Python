
class sample():
    def __init__(self):
        self.is_turned_on=True
    def transfer(self):
        self.is_turned_on=False


def transfer(is_turned_on):
    is_turned_on=True
    
    return is_turned_on



is_turned_on=False
print("{}".format(is_turned_on))
test=transfer(is_turned_on)
print("{}".format(test))


a=sample()

print(a.is_turned_on)
a.transfer()
print(a.is_turned_on)