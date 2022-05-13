# Test data
books_db = {1: 8, 2: 8, 3: 8, 4: 8, 5: 8}
discounts = {1: 0, 2: 0.05, 3: 0.1, 4: 0.2, 5: 0.25}
import unittest
 
class TestDiscounter(unittest.TestCase):
    def _groupifyOrder(self,books):
        groups = {}
        for book in books:
            if book in groups:
                groups[book] += 1
            else:
                groups[book] = 1
        return groups
 
    def _discounter(self,book_groups, total_discount=0):
        discount_tier = len(book_groups)
        # Loop through books, and apply discount to each book based
        # on discount tier
        for book in book_groups:
            total_discount += books_db[book] * discounts[discount_tier]
            book_groups[book] -= 1
        # Note - this style of dict comprehension only works with Python +2.7
        # Cull out dict entries that have a value of zero
        book_groups = {k: v for k, v in book_groups.items() if v}
        # If we have more groups, recurison continues
        if book_groups:
            self._discounter(book_groups, total_discount)
        return total_discount
    
    def calculateBasket(self,books):
        groups = self._groupifyOrder(books)
        total_discount = self._discounter(groups)
        full_price = sum([books_db[i] for i in books])
        total = full_price - total_discount
        return total
    price = 8
 
    def setUp(self):
        pass
 
    def test_noDiscount(self):
        books = [1, 1, 1, 1, 1]
        total = self.calculateBasket(books)
        self.assertEqual(total, self.price*len(books))
 
    def test_fivePercentDiscount(self):
        books = [1, 1, 1, 1, 2]
        total = self.calculateBasket(books)
        self.assertEqual(total, (self.price*5)-((self.price*2)*0.05))
 
    def test_tenPercentDiscount(self):
        books = [1, 1, 1, 2, 3]
        total = self.calculateBasket(books)
        self.assertEqual(total, (self.price*5)-((self.price*3)*0.1))
 
    def test_twentyPercentDiscount(self):
        books = [1, 1, 2, 3, 4]
        total = self.calculateBasket(books)
        self.assertEqual(total, (self.price*5)-((self.price*4)*0.2))
 
    def test_twentyFivePercentDiscount(self):
        books = [1, 2, 3, 4, 5]
        total = self.calculateBasket(books)
        self.assertEqual(total, (self.price*5)-((self.price*5)*0.25))
 
if __name__ == '__main__':
    unittest.main()