import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    # Test each quote and verify the output of getDataPoint
    for quote in quotes:
      stock, bid_price, ask_price, price = getDataPoint(quote)
      self.assertEqual(price, (bid_price + ask_price) / 2)
      self.assertEqual(stock, quote['stock'])

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    # Test each quote and verify the output of getDataPoint
    for quote in quotes:
      stock, bid_price, ask_price, price = getDataPoint(quote)
      self.assertEqual(price, (bid_price + ask_price) / 2)
      self.assertEqual(stock, quote['stock'])

  """ ------------ Add more unit tests ------------ """

  def test_getRatio_validInput(self):
    # Test the getRatio function with valid inputs
    price_a = 120.0
    price_b = 60.0
    ratio = getRatio(price_a, price_b)
    self.assertEqual(ratio, 2.0)

  def test_getRatio_priceBZero(self):
    # Test getRatio function when price_b is zero
    price_a = 120.0
    price_b = 0.0
    ratio = getRatio(price_a, price_b)
    self.assertEqual(ratio, 0)


  def test_getRatio_priceAZero(self):
    # Test getRatio function when price_a is zero
    price_a = 0.0
    price_b = 120.0
    ratio = getRatio(price_a, price_b)
    self.assertEqual(ratio, 0.0)

  def test_getRatio_bothPricesZero(self):
    # Edge case where both prices are zero, this should raise ZeroDivisionError as dividing zero by zero is undefined
    price_a = 0.0
    price_b = 0.0
    ratio = getRatio(price_a, price_b)
    self.assertEqual(ratio, 0.0)

  def test_getDataPoint_withNegativePrices(self):
    # Edge case with negative prices, should handle correctly as per current implementation
    quote = {'top_ask': {'price': -121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': -120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'XYZ'}
    stock, bid_price, ask_price, price = getDataPoint(quote)
    self.assertEqual(price, (bid_price + ask_price) / 2)
    self.assertEqual(stock, 'XYZ')

  def test_getDataPoint_withLargeNumbers(self):
    # Test with large numbers to see if the function can handle them without overflow
    quote = {'top_ask': {'price': 1e9, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 1e9, 'size': 109}, 'id': '0.109974697771', 'stock': 'BIG'}
    stock, bid_price, ask_price, price = getDataPoint(quote)
    self.assertEqual(price, (bid_price + ask_price) / 2)
    self.assertEqual(stock, 'BIG')


if __name__ == '__main__':
    unittest.main()
