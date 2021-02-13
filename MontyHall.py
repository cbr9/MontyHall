import numpy as np
from typing import List


class MontyHall:
    
    def __init__(self, change_door: bool):
        self.doors, self.prizes, self.correct_door = self.create_doors()
        self.selection = self.open_door(change_door)

    def check_result(self) -> bool:
        return self.selection == self.correct_door

    def create_doors(self) -> (List[int], List[bool], int):
        doors = [0, 1, 2]
        prizes = [True, False, False]
        np.random.shuffle(doors)
        np.random.shuffle(prizes)
        return doors, prizes, prizes.index(True)

    def open_door(self, change_door: bool) -> int:
        selection = np.random.choice(self.doors)
        if change_door:
            wrong_doors = [door for door in self.doors if self.prizes[door] is False and door != selection]
            to_open = np.random.choice(wrong_doors)  # door that is opened by the TV host
            selection = np.random.choice([door for door in self.doors if door != selection and door != to_open])
        return selection


if __name__ == "__main__":
    
    def print_results(change_door: bool) -> None:
        results = []
        for x in range(100000):
            test = MontyHall(change_door)
            results.append(test.check_result())
        message_modifier = " NOT " if not change_door else " "
        print("-" * 60)
        print("Correct results" + message_modifier + f"having changed the selected door: {results.count(True)}")
        print("Incorrect results" + message_modifier + f"having changed the selected door: {results.count(False)}")
        print("-" * 60)

    print_results(change_door=True)
    print_results(change_door=False)
