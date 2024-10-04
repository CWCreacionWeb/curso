import unittest
import random
from functools import reduce
from math import factorial
from statistics import stdev, mode
from string import ascii_lowercase, ascii_uppercase, digits


def test_greater(fn):
    class TestKnown(unittest.TestCase):
        def __init__(self, input, output):
            super(TestKnown, self).__init__()
            self.input = input
            self.output = output

        def runTest(self):
            self.assertEqual(fn(*self.input), self.output, f"Should be {self.output}")

    suite = unittest.TestSuite()
    for _ in range(100):
        a, b = random.randint(-1000, 1000), random.randint(-1000, 1000)
        suite.addTest(TestKnown([a, b], max(a, b)))
    unittest.TextTestRunner().run(suite)


def test_greatest(fn):
    class TestKnown(unittest.TestCase):
        def __init__(self, input, output):
            super(TestKnown, self).__init__()
            self.input = input
            self.output = output

        def runTest(self):
            self.assertEqual(fn(self.input), self.output, f"Should be {self.output}")

    suite = unittest.TestSuite()
    for _ in range(100):
        arr = []
        for _ in range(random.randint(10, 100)):
            arr.append(random.randint(-1000, 1000))
        suite.addTest(TestKnown(arr, max(arr)))
    unittest.TextTestRunner().run(suite)


def test_sum(fn):
    class TestKnown(unittest.TestCase):
        def __init__(self, input, output):
            super(TestKnown, self).__init__()
            self.input = input
            self.output = output

        def runTest(self):
            self.assertEqual(fn(self.input), self.output, f"Should be {self.output}")

    suite = unittest.TestSuite()
    for _ in range(100):
        arr = []
        for _ in range(random.randint(10, 100)):
            arr.append(random.randint(-1000, 1000))
        suite.addTest(TestKnown(arr, sum(arr)))
    unittest.TextTestRunner().run(suite)


def test_mult(fn):
    class TestKnown(unittest.TestCase):
        def __init__(self, input, output):
            super(TestKnown, self).__init__()
            self.input = input
            self.output = output

        def runTest(self):
            self.assertEqual(fn(self.input), self.output, f"Should be {self.output}")

    suite = unittest.TestSuite()
    for _ in range(100):
        arr = []
        for _ in range(random.randint(10, 100)):
            arr.append(random.randint(-10, 10))
        suite.addTest(TestKnown(arr, reduce(lambda a, b: a * b, arr, 1)))
    unittest.TextTestRunner().run(suite)


def test_operations(fn):
    class TestKnown(unittest.TestCase):
        def __init__(self, input, output):
            super(TestKnown, self).__init__()
            self.input = input
            self.output = output

        def runTest(self):
            self.assertEqual(fn(*self.input), self.output, f"Should be {self.output}")

    def ans(arr, op):
        if op == "+":
            return sum(arr)
        else:
            return reduce(lambda a, b: a * b, arr, 1)

    suite = unittest.TestSuite()
    for _ in range(100):
        arr = []
        for _ in range(random.randint(10, 100)):
            arr.append(random.randint(-10, 10))
        op = random.choice(["+", "*"])
        suite.addTest(TestKnown((arr, op), ans(arr, op)))

    unittest.TextTestRunner().run(suite)


def test_factorial(fn):
    class TestKnown(unittest.TestCase):
        def __init__(self, input, output):
            super(TestKnown, self).__init__()
            self.input = input
            self.output = output

        def runTest(self):
            self.assertEqual(fn(self.input), self.output, f"Should be {self.output}")

    suite = unittest.TestSuite()
    for _ in range(100):
        n = random.randint(1, 100)
        suite.addTest(TestKnown(n, factorial(n)))
    unittest.TextTestRunner().run(suite)


def test_unique(fn):
    class TestKnown(unittest.TestCase):
        def __init__(self, input, output):
            super(TestKnown, self).__init__()
            self.input = input
            self.output = output

        def runTest(self):
            self.assertEqual(set(fn(self.input)), self.output, f"Should be {self.output}")

    suite = unittest.TestSuite()
    for _ in range(100):
        arr = []
        for _ in range(random.randint(10, 1000)):
            arr.append(random.randint(-100, 100))
        suite.addTest(TestKnown(arr, set(arr)))
    unittest.TextTestRunner().run(suite)


def test_mode(fn):
    class TestKnown(unittest.TestCase):
        def __init__(self, input, output):
            super(TestKnown, self).__init__()
            self.input = input
            self.output = output

        def runTest(self):
            self.assertEqual(fn(self.input), self.output, f"Should be {self.output}")

    suite = unittest.TestSuite()
    for _ in range(100):
        arr = []
        for _ in range(random.randint(100, 125)):
            arr.append(random.randint(1, 25))
        arr += [random.randint(1, 25)] * 50
        suite.addTest(TestKnown(arr, mode(arr)))
    unittest.TextTestRunner().run(suite)


def test_stdev(fn):
    class TestKnown(unittest.TestCase):
        def __init__(self, input, output):
            super(TestKnown, self).__init__()
            self.input = input
            self.output = output

        def runTest(self):
            self.assertAlmostEqual(fn(self.input), self.output, delta=5, msg=f"Should be {self.output}")

    suite = unittest.TestSuite()
    for _ in range(100):
        arr = []
        for _ in range(random.randint(10, 100)):
            arr.append(random.randint(-1000, 1000))
        suite.addTest(TestKnown(arr, stdev(arr)))
    unittest.TextTestRunner().run(suite)


pangrams = [
    "Waltz, nymph, for quick jigs vex Bud.",
    "Sphinx of black quartz, judge my vow.",
    "Pack my box with five dozen liquor jugs.",
    "Glib jocks quiz nymph to vex dwarf.",
    "Jackdaws love my big sphinx of quartz.",
    "The five boxing wizards jump quickly.",
    "How vexingly quick daft zebras jump!",
    "Quick zephyrs blow, vexing daft Jim.",
    "Two driven jocks help fax my big quiz.",
    "The jay, pig, fox, zebra and my wolves quack!",
    "Sympathizing would fix Quaker objectives.",
    "A wizard's job is to vex chumps quickly in fog.",
    "Watch 'Jeopardy!', Alex Trebek's fun TV quiz game.",
    "By Jove, my quick study of lexicography won a prize!",
    "Waxy and quivering, jocks fumble the pizza."
]

def test_pangram(fn):
    class TestKnown(unittest.TestCase):
        def __init__(self, input, output):
            super(TestKnown, self).__init__()
            self.input = input
            self.output = output

        def runTest(self):
            self.assertEqual(fn(self.input), self.output, f"Should be {self.output}")

    suite = unittest.TestSuite()
    tests = pangrams + ["".join([random.choice(ascii_lowercase) for _ in range(random.randint(25, 100))]) for _ in range(15)]
    
    for test in tests:
        suite.addTest(TestKnown(test, set(ascii_lowercase).issubset(set(test.lower()))))
    
    unittest.TextTestRunner().run(suite)


def test_alpha(fn):
    class TestKnown(unittest.TestCase):
        def __init__(self, input, output):
            super(TestKnown, self).__init__()
            self.input = input
            self.output = output

        def runTest(self):
            self.assertEqual(fn(self.input), self.output, f"Should be {self.output}")

    suite = unittest.TestSuite()
    tests = []
    
    for _ in range(100):
        group = []
        for _ in range(random.randint(4, 25)):
            word = ''
            for _ in range(random.randint(4, 10)):
                word += random.choice(ascii_lowercase)
            group.append(word)
        tests.append(",".join(group))
    
    for test in tests:
        suite.addTest(TestKnown(test, ",".join(sorted(test.split(",")))))
    unittest.TextTestRunner().run(suite)


def test_pass(fn):
    class TestKnown(unittest.TestCase):
        def __init__(self, input, output):
            super(TestKnown, self).__init__()
            self.input = input
            self.output = output

        def runTest(self):
            self.assertEqual(fn(self.input), self.output, f"Should be {self.output}")

    suite = unittest.TestSuite()
    check_p = lambda string: sum([len(set(string) & set(c)) > 0 for c in [ascii_lowercase, ascii_uppercase, digits, "#@!$%&()^*[]{}"]] + [len(string) >= 8]) >= 5
    
    tests = []
    for _ in range(100):
        password = ''.join([random.choice(ascii_lowercase * 3 + ascii_uppercase + digits + "#@!$%&()^*[]{}") for _ in range(random.randint(2, 16))])
        tests.append(password)

    for test in tests:
        suite.addTest(TestKnown(test, check_p(test)))
    unittest.TextTestRunner().run(suite)
