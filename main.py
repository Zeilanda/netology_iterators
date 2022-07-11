class FlatIterator:
    def __init__(self, some_list):
        self._stopped = False
        self._list = some_list
        self._i = 0
        self._j = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self._stopped:
            while self._i < len(self._list):
                if self._j < len(self._list[self._i]):
                    part = self._list[self._i][self._j]
                    self._j += 1
                    return part

                self._i += 1
                self._j = 0
            self._stopped = True
        raise StopIteration


def flat_generator(some_list):
    for element in some_list:
        for part in element:
            yield part


def main():
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]

    for item in FlatIterator(nested_list):
        print(item)

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)

    for item in flat_generator(nested_list):
        print(item)


main()
