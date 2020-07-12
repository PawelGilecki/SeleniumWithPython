import unittest

def setUpModule(): #will be executed before executing any class or any method present in the class test
    print("setUpModule")

def tearDownModule(): #will be executed after executing any class or any method present in the class test
    print("tearDownModule")

class AppTesting(unittest.TestCase):

    @classmethod
    def setUp(self): #Execute before all test methods
        print("This is login test")

    @classmethod
    def tearDown(self): #Execute afer all test methods
        print("This is logout test")

    @classmethod
    def setUpClass(cls): #Execute once when the class started
        print("Open Application")

    @classmethod
    def tearDownClass(cls): #Execute once when the class completed
        print("Close Application")

    def test_search(self):
        print("This is search test")

    def test_advancedSearch(self):
        print("This is advanced search test")

    def test_prepaidRecharge(self):
        print("This is prepaid recharge test")

    def test_postpaidRecharge(self):
        print("This is postpaid recharge test")

if __name__=="__main__":
    unittest.main()