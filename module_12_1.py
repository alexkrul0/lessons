
import runner
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        self.run1 = runner.Runner('Runner 1')
        for i in range(0, 10):
            self.run1.walk()
        self.assertEqual(self.run1.distance, 50)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        self.run2 = runner.Runner('Runner 2')
        for i in range(0, 10):
            self.run2.run()
        self.assertEqual(self.run2.distance, 100)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        self.run3 = runner.Runner('Runner 3')
        self.run4 = runner.Runner('Runner 4')
        for i in range(0, 10):
            self.run3.run()
            self.run4.walk()
        self.assertNotEqual(self.run3.distance, self.run4.distance)


if __name__ == '__main__':
    unittest.main()