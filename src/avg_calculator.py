from numbers import Number
from decimal import Decimal


class avgCalculate(object):
	def __init__(self):
		self.divider = Decimal(0.0)
		self.numbers_sum = Decimal(0.0)

	def update(self, number):
		if not (isinstance(number, Decimal) or  isinstance(number, float) or isinstance(number, int)):
			raise ValueError("avgCalculate.update 'number' parameter must be type of Decimal, float or int, not {0}".format(type(number)))

		self.divider += 1
		self.numbers_sum += Decimal(number)

	def getAvg(self):
		"""
		Method calculates the average of numbers
		"""
		if self.divider == Decimal(0.0) or self.numbers_sum == Decimal(0.0):
			return Decimal(0)

		return self.numbers_sum / self.divider

