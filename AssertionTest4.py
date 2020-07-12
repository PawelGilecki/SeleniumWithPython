import unittest

class Test(unittest.TestCase):
    def testName(self):
        list={"python", "selenium", "java"}

        #self.assertIn("selenium", list)
        self.assertNotIn("ruby", list)
if __name__ == "__main__":
    unittest.main()