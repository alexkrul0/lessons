import runner_and_tournament
import unittest

from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):
    def setUp(self):
        self.run1 = Runner('Усэйн', 10)
        self.run2 = Runner('Андрей', 9)
        self.run3 = Runner('Ник', 3)

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}


    def tearDown(self):
        sort_result = {}
        for time, runner in sorted(self.all_results.items()):
            sort_result[time] = runner.name
        print(sort_result)


    def test1(self):
        tournament = Tournament(90, self.run1, self.run3)
        result = tournament.start()
        self.all_results.update(result)
        self.assertTrue(self.all_results[max(self.all_results)] == 'Ник')


    def test2(self):
        tournament = Tournament(90, self.run2, self.run3)
        result = tournament.start()
        self.all_results.update(result)
        self.assertTrue(self.all_results[max(self.all_results)] == 'Ник')


    def test3(self):
        tournament = Tournament(90, self.run1, self.run2, self.run3)
        result = tournament.start()
        self.all_results.update(result)
        self.assertTrue(self.all_results[max(self.all_results)] == 'Ник')


if __name__ == '__main__':
    unittest.main()