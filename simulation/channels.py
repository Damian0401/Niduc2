import komm
import random


def binary_symmetric(probability: int):
    return komm.BinarySymmetricChannel(probability)

def gilbert_elliot(reverse_good: float, reverse_bad: float, error_chance: float):
    def channel(input):
        output = []
        is_bad = False

        for i in input:
            if is_bad:
                if random.random() < error_chance:
                    output.append((i + 1) % 2)
                else:
                    output.append(i)
                is_bad = random.random() < reverse_good
                continue

            output.append(i)
            is_bad = random.random() < reverse_bad

        return output

    return channel

