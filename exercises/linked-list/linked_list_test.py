import unittest

from linked_list import LinkedList


class LinkedListTests(unittest.TestCase):

    def setUp(self):
        self.list = LinkedList()

    def test_push_pop(self):
        self.list.push(10)
        self.list.push(20)
        self.assertEqual(20, self.list.pop())
        self.assertEqual(10, self.list.pop())

    def test_push_shift(self):
        self.list.push(10)
        self.list.push(20)
        self.assertEqual(10, self.list.shift())
        self.assertEqual(20, self.list.shift())

    def test_unshift_shift(self):
        self.list.unshift(10)
        self.list.unshift(20)
        self.assertEqual(20, self.list.shift())
        self.assertEqual(10, self.list.shift())

    def test_unshift_pop(self):
        self.list.unshift(10)
        self.list.unshift(20)
        self.assertEqual(10, self.list.pop())
        self.assertEqual(20, self.list.pop())

    def test_all(self):
        self.list.push(10)
        self.list.push(20)
        self.assertEqual(20, self.list.pop())
        self.list.push(30)
        self.assertEqual(10, self.list.shift())
        self.list.unshift(40)
        self.list.push(50)
        self.assertEqual(40, self.list.shift())
        self.assertEqual(50, self.list.pop())
        self.assertEqual(30, self.list.shift())

    @unittest.skip("extra-credit")
    def test_length(self):
        self.list.push(10)
        self.list.push(20)
        self.assertEqual(2, len(self.list))
        self.list.shift()
        self.assertEqual(1, len(self.list))
        self.list.pop()
        self.assertEqual(0, len(self.list))

    @unittest.skip("extra-credit")
    def test_iterator(self):
        self.list.push(10)
        self.list.push(20)
        iterator = iter(self.list)
        self.assertEqual(10, next(iterator))
        self.assertEqual(20, next(iterator))


if __name__ == '__main__':
    unittest.main()
