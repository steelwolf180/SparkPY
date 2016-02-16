from collections import namedtuple

Item = namedtuple('Item', 'name weight value'.split())

ITEMS = [
    Item("map", 9, 150),
    Item("compass", 13, 35),
    Item("water", 153, 200),
    Item("sandwich", 50, 160),
    Item("glucose", 15, 60),
    Item("tin", 68, 45),
    Item("banana", 27, 60),
    Item("apple", 39, 40),
    Item("cheese", 23, 30),
    Item("beer", 52, 10),
    Item("suntan cream", 11, 70),
    Item("camera", 32, 30),
    Item("t-shirt", 24, 15),
    Item("trousers", 48, 10),
    Item("umbrella", 73, 40),
    Item("waterproof trousers", 42, 70),
    Item("waterproof overclothes", 43, 75),
    Item("note-case", 22, 80),
    Item("sunglasses", 7, 20),
    Item("towel", 18, 12),
    Item("socks", 4, 50),
    Item("book", 30, 10),
]


def efficiency(item):
    """Return efficiency of item (its value per unit weight)."""
    return float(item.value) / float(item.weight)


def packing(items=ITEMS, max_weight=400):
    """Return a list of items with the maximum value, subject to the
    constraint that their combined weight must not exceed max_weight.

    """

    def pack(item):
        # Attempt to pack item; return True if successful.
        if item.weight <= pack.max_weight:
            pack.max_weight -= item.weight
            return True
        else:
            return False

    pack.max_weight = max_weight
    return list(filter(pack, sorted(items, key=efficiency, reverse=True)))
