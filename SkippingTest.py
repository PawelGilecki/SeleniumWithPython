import unittest

class Apptesting(unittest.TestCase):

    @unittest.SkipTest #decorator
    def test_search(self):
        print("This is search test")

    @unittest.skip("I am skipping this test method because it is not yet ready")
    def test_advancedSearch(self):
        print("This is advanced search test")

    @unittest.skipIf(1==1, "Numbers are not equal")
    def test_prepaidRecharge(self):
        print("This is pre-paid recharge test")

    def test_postpaidRecharge(self):
        print("This is post-paid recharge test")

    def test_loginbygmail(self):
        print("This is login by email")

    def test_loginbytwitter(self):
        print("This is loggin by twitter")

if __name__ == "__main__":
    unittest.main()