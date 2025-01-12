import unittest
from dynamic_array import MyList


class TestDynamicArray(unittest.TestCase):
    def test_append(self):
        arr = MyList()
        arr.append(1)
        arr.append(2)
        self.assertEqual(str(arr), "[1,2]")

    def test_remove(self):
        arr = MyList()
        arr.append(1)
        arr.append(2)
        arr.remove(1)
        self.assertEqual(str(arr), "[2]")

    def test_pop(self):
        arr = MyList()
        arr.append(1)
        popped = arr.pop()
        self.assertEqual(popped, 1)
        self.assertEqual(len(arr), 0)


if __name__ == "__main__":
    unittest.main()
