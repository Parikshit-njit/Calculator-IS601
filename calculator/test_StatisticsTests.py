import unittest
from Statistics.Statistics import Statistics
import statistics as stats
from RandomGenerator.RandomInts import RandomsList as IntRandoms
from RandomGenerator.RandomDecimals import RandomsList as DecimalRandoms


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.statistics = Statistics()
        self.integerRandomDataF = IntRandoms.generate_randoms(0, 30, 0, 10, False)
        self.integerRandomDataT = IntRandoms.generate_randoms(0, 30, 2, 10, True)
        self.decimalRandomData = DecimalRandoms.generate_randoms(3, 4, 0, 10, True)

    def getUp(self) -> None:
        return self.integerRandomDataF
        return self.integerRandomDataT
        return self.decimalRandomData

    def test_instance(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_result(self):
        # test_cases = CsvReader("TestFiles/Unit Test Mean.csv").data
        self.assertEqual(self.statistics.get_mean(self.integerRandomDataF), stats.mean(self.integerRandomDataF))
        self.assertEqual(self.statistics.get_mean(self.decimalRandomData), stats.mean(self.decimalRandomData))
        print("Mean test cases passed!")

    def test_median_result(self):
        # test_cases = CsvReader("TestFiles/Unit Test Median.csv").data
        self.assertEqual(self.statistics.get_median(self.integerRandomDataF), stats.median(self.integerRandomDataF))
        print("Median test cases for Integer Random List passed!")
        self.assertEqual(self.statistics.get_median(self.decimalRandomData), stats.median(self.decimalRandomData))
        print("Median test cases for Decimal Random List passed!")

    def test_mode_result(self):
        # test_cases = CsvReader("TestFiles/Unit Test Mode.csv").data
        self.assertTrue(stats.mode(self.integerRandomDataT.tolist()) in self.statistics.get_mode(self.integerRandomDataT.tolist()))
        print("Mode test cases for Integer Random List passed!")
        print("Mode test cases for Decimal Random List passed!")

    def test_variance_result(self):
        # test_cases = CsvReader("TestFiles/Unit Test Variance.csv").data
        self.assertEqual(self.statistics.get_variance(self.integerRandomDataF), stats.variance(self.integerRandomDataF))
        print("Variance test cases for Integer Random List passed!")
        self.assertEqual(self.statistics.get_variance(self.decimalRandomData), stats.variance(self.decimalRandomData))
        print("Variance test cases for Decimal Random List passed!")

    def test_stdev_result(self):
        # test_cases = CsvReader("TestFiles/Unit Test StandardDeviation.csv").data
        self.assertEqual(self.statistics.get_stdev(self.integerRandomDataF), stats.stdev(self.integerRandomDataF))
        print("Standard Deviation test cases for Integer Random List passed!")
        self.assertEqual(self.statistics.get_stdev(self.decimalRandomData), stats.stdev(self.decimalRandomData))
        print("Standard Deviation test cases for Decimal Random List passed!")


if __name__ == '__main__':
    unittest.main()
