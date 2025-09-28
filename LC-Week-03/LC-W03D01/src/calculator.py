# src/calculator.py


class Calculator:
    def add(self, num_1, num_2):
        # if num_1 or num_2 is what
        # int, float, complex  (1j)
        accepted_classes = (int, float, complex)
        # accepted_classes = int
        #  1: 4.5   2: 3.5

        if isinstance(num_1, accepted_classes) and isinstance(num_2, accepted_classes):
            return num_1 + num_2
        else:
            raise ValueError
