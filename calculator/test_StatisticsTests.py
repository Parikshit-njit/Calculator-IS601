import unittest
from CsvReader.CSVReader import CsvReader
from Statistics.Statistics import Statistics
import statistics as stats
from RandomGenerator import RandomsList


class MyTestCase(unittest.TestCase):

    def test_mean_result(self):
        data = []
        statistics = Statistics()
        test_cases = CsvReader("TestFiles/Unit Test Mean.csv").data
        # for test_case in test_cases:
        #     data.append(int(test_case['Value']))
        data = RandomsList.generate_randoms(0, 30, 0, 10)
        print(data)
        self.assertEqual(statistics.get_mean(data), stats.mean(data))
        print("Mean test cases passed!")

    def test_median_result(self):
        data = []
        statistics = Statistics()
        test_cases = CsvReader("TestFiles/Unit Test Median.csv").data
        # for test_case in test_cases:
        #     data.append(int(test_case['Value']))
        data = RandomsList.generate_randoms(0, 30, 0, 10)
        print(data)
        self.assertEqual(statistics.get_median(data), stats.median(data))
        print("Median test cases passed!")

    def test_mode_result(self):
        data = []
        statistics = Statistics()
        test_cases = CsvReader("TestFiles/Unit Test Mode.csv").data
        for test_case in test_cases:
            data.append(int(test_case['Value']))
        self.assertEqual(statistics.get_mode(data), stats.mode(data))
        print("Mode test cases passed!")

    def test_variance_result(self):
        data = []
        statistics = Statistics()
        test_cases = CsvReader("TestFiles/Unit Test Variance.csv").data
        for test_case in test_cases:
            data.append(int(test_case['Value']))
        self.assertEqual(statistics.get_variance(data), statistics.result)
        print("Variance test cases passed!")

    def test_stdev_result(self):
        data = []
        statistics = Statistics()
        test_cases = CsvReader("TestFiles/Unit Test StandardDeviation.csv").data
        for test_case in test_cases:
            data.append(int(test_case['Value']))
        self.assertEqual(statistics.get_stdev(data), statistics.result)
        print("Standard Deviation test cases passed!")


if __name__ == '__main__':
    unittest.main()
