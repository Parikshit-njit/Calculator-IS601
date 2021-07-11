import unittest
from CsvReader.CSVReader import CsvReader
from Statistics.Statistics import Statistics
import statistics as stats
from RandomGenerator import RandomsList


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.statistics = Statistics()
        self.data = []

    def getUp(self) -> None:
        return self.data

    def test_instance(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_data_property(self):
        self.assertEqual(self.data, [])

    def test_mean_result(self):
        test_cases = CsvReader("TestFiles/Unit Test Mean.csv").data
        data = RandomsList.generate_randoms(0, 30, 0, 10, False)
        self.assertEqual(self.statistics.get_mean(data), stats.mean(data))
        print("Mean test cases passed!")

    def test_median_result(self):
        test_cases = CsvReader("TestFiles/Unit Test Median.csv").data
        data = RandomsList.generate_randoms(0, 30, 0, 10, False)
        self.assertEqual(self.statistics.get_median(data), stats.median(data))
        print("Median test cases passed!")

    def test_mode_result(self):
        test_cases = CsvReader("TestFiles/Unit Test Mode.csv").data
        data = RandomsList.generate_randoms(0, 30, 2, 10, True)
        self.assertTrue(stats.mode(data.tolist()) in self.statistics.get_mode(data.tolist()))
        print("Mode test cases passed!")

    def test_variance_result(self):
        test_cases = CsvReader("TestFiles/Unit Test Variance.csv").data
        data = RandomsList.generate_randoms(0, 30, 0, 10, False)
        self.assertEqual(self.statistics.get_variance(data), stats.variance(data))
        print("Variance test cases passed!")

    def test_stdev_result(self):
        test_cases = CsvReader("TestFiles/Unit Test StandardDeviation.csv").data
        data = RandomsList.generate_randoms(0, 30, 0, 10, False)
        self.assertEqual(self.statistics.get_stdev(data), stats.stdev(data))
        print("Standard Deviation test cases passed!")


if __name__ == '__main__':
    unittest.main()
