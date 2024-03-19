import unittest
from product import Product


class TestProduct(unittest.TestCase):
    def test_init(self):
        p = Product('apple', 10, 5)
        self.assertEqual(p.name, 'apple')
        self.assertEqual(p.price, 10)
        self.assertEqual(p.quantity, 5)
        
    def test_input_type(self):
        p = Product('apple', 10, 5)
        self.assertIsInstance(p.name, str)
        self.assertIsInstance(p.price, int)
        self.assertIsInstance(p.quantity, int)
    
    def test_calculateTotal(self):
        p = Product('apple', 10, 5)
        self.assertEqual(p.calculateTotal(), 50)
        
    def test_calcualteTotal_with_zero_quantity(self):
        product = Product('apple', 10, 0)
        self.assertEqual(product.calculateTotal(), 0)
        
    def test_negative_values(self):
        with self.assertRaises(ValueError):
            p = Product('apple', 10, -5)
    
if __name__ == "__main__":
    unittest.main()