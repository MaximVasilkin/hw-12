import types


# first task

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_lists = list_of_list

    def __iter__(self):
        self.sub_list = iter([])
        self.counter = 0
        return self

    def __next__(self):
        try:
            elem = next(self.sub_list)
        except StopIteration:
            if self.counter + 1 > len(self.list_of_lists):
                raise StopIteration
            self.sub_list = iter(self.list_of_lists[self.counter])
            elem = next(self.sub_list)
            self.counter += 1
        return elem


def test_one():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


# second task

def flat_generator(list_of_lists):
    return (item for list_ in list_of_lists for item in list_)


# def flat_generator(list_of_lists):
#     yield from (item for list_ in list_of_lists for item in list_)


def test_two():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_one()
    test_two()
