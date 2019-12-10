import numpy as np
from typing import Dict


class MontyHall:
    
    def __init__(self, change_door: bool):
        self.doors, self.prizes, self.correct_door = self.create_doors()
        self.selection = self.open_door(change_door)

    def check_result(self) -> bool:
        if self.selection == self.correct_door:
            return True
        else:
            return False

    def create_doors(self) -> Dict:
        doors = [0, 1, 2]
        prizes = [True, False, False]
        np.random.shuffle(doors)
        np.random.shuffle(prizes)
        return doors, prizes, prizes.index(True)


    def open_door(self, change_door: bool) -> int:
        selection = np.random.choice(self.doors)
        if change_door:
            wrong_doors = [door for door in self.doors if self.prizes[door] is False and door != selection]
            to_open = np.random.choice(wrong_doors)
            self.doors.remove(to_open)
            selection = np.random.choice([door for door in self.doors if door != selection])

        return selection


if __name__ == "__main__":
    
    results = []
    for x in range(100000):
        test = MontyHall(change_door=True)
        results.append(test.check_result())

    print(f"Correct results having changed the selected door: {results.count(True)}")
    print(f"Incorrect results having changed the selected door: {results.count(False)}")
    print("-" * 60)

    results = []
    for x in range(100000):
        test = MontyHall(change_door=False)
        results.append(test.check_result())

    print(f"Correct results NOT having changed the selected door: {results.count(True)}")
    print(f"Incorrect results NOT having changed the selected door: {results.count(False)}")
