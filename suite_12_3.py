import unittest
import test_12_2
import module_12_1

total_test = unittest.TestSuite()
total_test.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_1.RunnerTest))
total_test.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(total_test)
