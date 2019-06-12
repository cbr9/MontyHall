import numpy as np


class MontyHall:
    
    def __init__(self, change_door: bool) -> bool:
        self.__doors = [0, 1, 2]
        self.__prizes = [True, False, False]
        np.random.shuffle(self.__doors)
        np.random.shuffle(self.__prizes)
        self.__prized_doors = dict(zip(self.__doors, self.__prizes))
        self.__selection = np.random.choice(self.__doors)
        self.__opened_door = self.open_door()

        if change_door is True:
            self.__selection = self.change_selection()
            
        self.__correct_door = [door for door in self.__doors if self.__prized_doors[door] is True][0]
        self.final = True if self.__selection == self.__correct_door else False

    def open_door(self):
        wrong_doors = [door for door in self.__doors if self.__prized_doors[door] is False and door != self.__selection]
        to_open = np.random.choice(wrong_doors)
        self.__doors.remove(to_open)
        return to_open

    def change_selection(self):
        new_selection = [door for door in self.__doors if door != self.__selection][0]
        return new_selection


if __name__ == "__main__":
    
    results = []
    for x in range(100000):
        test = MontyHall(change_door=True)
        results.append(test.final)

    print(f"Correct results having changed the selected door: {results.count(True)}")
    print(f"Incorrect results having changed the selected door: {results.count(False)}")
    print("-" * 60)

    results = []
    for x in range(100000):
        test = MontyHall(change_door=False)
        results.append(test.final)

    print(f"Correct results NOT having changed the selected door: {results.count(True)}")
    print(f"Incorrect results NOT having changed the selected door: {results.count(False)}")
