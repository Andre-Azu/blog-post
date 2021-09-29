import unittest
from user_model import Quote
#Quote = quote.Quote

class QuoteTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Quote class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_quote = Quote(16,"Yogi Berra","In theory, theory and practice are the same. In practice, they’re not.","http://quotes.stormconsultancy.co.uk/quotes/16")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_quote,Quote))


if __name__ == '__main__':
    unittest.main()