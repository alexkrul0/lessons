
import runner
import unittest


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        self.run1 = runner.Runner('Mike')
        for i in range(0, 10):
            self.run1.walk()
        self.assertEqual(self.run1.distance, 50)

    def test_run(self):
        self.run2 = runner.Runner('Tom')
        for i in range(0, 10):
            self.run2.run()
        self.assertEqual(self.run2.distance, 100)

    def test_challenge(self):
        self.run3 = runner.Runner('Runner 3')
        self.run4 = runner.Runner('Runner 4')
        for i in range(0, 10):
            self.run3.run()
            self.run4.walk()
        self.assertNotEqual(self.run3.distance, self.run4.distance)


if __name__ == '__main__':
    unittest.main()