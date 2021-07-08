import unittest
from CsvReader.CSVReader import CsvReader
from Statistics.Statistics import Statistics


class MyTestCase(unittest.TestCase):

    def test_mean_result(self):
        data = []
        statistics = Statistics();
        test_cases = CsvReader("TestFiles/Unit Test Statistics.csv").data
        for test_case in test_cases:
            data.append(int(test_case['Value']))
        self.assertEqual(statistics.get_mean(data), statistics.result)
        print("Mean test cases passed!")


if __name__ == '__main__':
    unittest.main()
