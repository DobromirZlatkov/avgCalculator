import unittest
from sys import getsizeof
from decimal import Decimal
from avg_calculator import avgCalculate



class TestAvgCalculator(unittest.TestCase):

    def test_if_space_complexity_is_O_1(self):
        curr_avg_calculator = avgCalculate()

        size_of_class_before_updating = getsizeof(curr_avg_calculator)
        size_of_class_variable_divider_before_updating = getsizeof(curr_avg_calculator.divider)
        size_of_class_variable_numbers_sum_before_updating = getsizeof(curr_avg_calculator.numbers_sum)

        for x in range(1, 42):
            curr_avg_calculator.update(x)

        average = curr_avg_calculator.getAvg()

        size_of_class_after_updating = getsizeof(curr_avg_calculator)
        size_of_class_variable_divider_after_updating = getsizeof(curr_avg_calculator.divider)
        size_of_class_variable_numbers_sum_after_updating = getsizeof(curr_avg_calculator.numbers_sum)

        self.assertEqual(size_of_class_before_updating, size_of_class_after_updating)
        self.assertEqual(size_of_class_variable_divider_before_updating, size_of_class_variable_divider_after_updating)
        self.assertEqual(size_of_class_variable_numbers_sum_after_updating, size_of_class_variable_numbers_sum_after_updating)

    def test_if_divider_parameter_is_correctly_increased(self):
        curr_avg_calculator = avgCalculate()

        curr_avg_calculator.update(0)
        self.assertEqual(curr_avg_calculator.divider, 1)

        # when wrong parameter is passed divider is not increased
        try:
            curr_avg_calculator.update(None)
        except Exception:
            pass

        self.assertEqual(curr_avg_calculator.divider, 1)

        curr_avg_calculator.update(2)
        self.assertEqual(curr_avg_calculator.divider, 2)



    def test_update_method_raise_value_exception_when_wrong_type_of_parameter(self):
        curr_avg_calculator = avgCalculate()

        with self.assertRaises(ValueError):
            curr_avg_calculator.update("wrong param type")

        with self.assertRaises(ValueError):
            curr_avg_calculator.update(4j)

        with self.assertRaises(ValueError):
            curr_avg_calculator.update([])

        with self.assertRaises(ValueError):
            curr_avg_calculator.update(None)

    def test_getAvg_method_returns_correct_value_with_valid_parameters(self):
        curr_avg_calculator = avgCalculate()

        # validate if when no update is applied value is 0 and no division by 0 error
        curr_avg = curr_avg_calculator.getAvg()
        self.assertEqual(curr_avg_calculator.getAvg(), 0)


        list_of_numbers = [0, 0, 15, 18, 2, 36, 12, 78, 5, 6, 9, -12, -124, Decimal(2.3), Decimal(12.534523523), 3123132132131231231231231231231231231232131231231231231]
        average_of_list = sum(list_of_numbers) / len(list_of_numbers)

        for num in list_of_numbers:
            curr_avg_calculator.update(num)

        self.assertEqual(curr_avg_calculator.getAvg(), average_of_list)


if __name__ == '__main__':
    unittest.main()