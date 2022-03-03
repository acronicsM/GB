class Road:
    __unit_price = 25

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def mass(self, thickness):
        return self.__length * self.__width * Road.__unit_price * thickness

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def get_unit_price(self):
        return self.__unit_price


r1 = Road(20, 5000)
print(f'{r1.get_length()}м *{r1.get_width()}м *{r1.get_unit_price()}кг *{5}см = {int(r1.mass(5)/1000)}т.')

r1 = Road(10, 200)
print(f'{r1.get_length()}м *{r1.get_width()}м *{r1.get_unit_price()}кг *{5}см = {int(r1.mass(5)/1000)}т.')

r1 = Road(5, 50000)
print(f'{r1.get_length()}м *{r1.get_width()}м *{r1.get_unit_price()}кг *{5}см = {int(r1.mass(5)/1000)}т.')
