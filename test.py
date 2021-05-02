# Unit test runner for SCM Coding Test 2: Business Rules Engine

from rules_engine import RulesEngine
from rules import *
from products import *
from actions import *


class Payment:
        def __init__(self, product):
                self.product = product


def testCase(name, payment, rules, expectedActions):
        """Test if applying the given rules to a payment results in the expected actions"""
        rulesEngine = RulesEngine(rules)
        actualActions = rulesEngine.applyRules(payment)
        if expectedActions == actualActions:
                print(name, "PASSED")
        else:
                print(name, "FAILED: Expected", expectedActions, "Actual", actualActions)


if __name__ == "__main__":
        # Tests of individual rules
        testCase(
                "Packing slip for Shipping", 
                Payment(PhysicalProduct()), 
                [GeneratePackingSlipForShipping()],
                [PackingSlip("shipping")])        
        testCase(
                "Packing slip for Royalty", 
                Payment(Book()), 
                [GeneratePackingSlipForRoyalty()],
                [PackingSlip("royalty")])