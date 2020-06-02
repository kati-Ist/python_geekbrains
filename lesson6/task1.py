import time


class TrafficLight:
    def __init__(self):
        self.__color = ["red", "yellow", "green", "yellow"]

    def running(self):
        times = [7, 2, 7, 2]
        colors = ["\033[31m {}", "\033[33m {}", "\033[32m {}", "\033[33m {}"]
        while True:
            for ind, el in enumerate(colors):
                print(colors[ind].format(self.__color[ind]))
                time.sleep(times[colors.index(el)])


a = TrafficLight()
a.running()
