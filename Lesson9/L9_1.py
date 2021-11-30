from time import sleep
from itertools import cycle


class TrafficLight:
    __colors_map = ['зеленый', 'желтый', 'красный', 'желтый', 'зеленый', 'желтый']

    def __init__(self, color, green_time=1, yellow_time=2, red_time=7):
        self.__color = color
        self.__colors_time = {'зеленый': green_time,
                              'желтый': yellow_time,
                              'красный': red_time}

    def state(self):
        return self.__color

    def running(self, duration=None):
        t = duration
        color_cycle = cycle(self.__colors_map[self.__colors_map.index(self.state()):])
        for i in color_cycle:
            self.__color = i
            timeout = self.__colors_time[i]
            if t is not None:
                if t < timeout:
                    break
                else:
                    sleep(timeout)

                t -= timeout


tl = TrafficLight('зеленый')
print(f'Текущий цвет: {tl.state()}')

try:
    tl.running()
except KeyboardInterrupt:
    print('Принудительная остановка')

print(f'Новый цвет: {tl.state()}')
