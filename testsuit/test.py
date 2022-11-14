import unittest
from unitestpack.rcmethod import Test
from payment.pay import TestStringMethods
tc1=unittest.TestLoader().loadTestsFromTestCase(Test)
tc2=unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
sanitytestsuit=unittest.TestSuite(tc1)
functionaltestsuit=unittest.TestSuite(tc2)
mastertestsuit=unittest.TestSuite([tc1,tc2])
unittest.TextTestRunner().run(sanitytestsuit)
unittest.TextTestRunner().run(functionaltestsuit)
unittest.TextTestRunner(verbosity=2).run(mastertestsuit)