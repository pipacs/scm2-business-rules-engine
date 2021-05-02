# Unit test runner for SCM Coding Test 2: Business Rules Engine

class RulesEngine:
        def __init__(self, rules):
                self.rules = rules 

        def applyRules(self, payment):
                actions = []
                for rule in self.rules:
                        actions += rule.apply(payment)
                return actions


class Rule:
        def apply(self, payment):
                return []


class GeneratePackingSlipForShipping(Rule):
        def apply(self, payment):
                actions = []
                if isinstance(payment.product, PhysicalProduct):
                        actions.append(PackingSlipForShipping())
                return actions


class Action:
        def __eq__(self, other):
                return false  # Can't compare abstract Actions

        def __ne__(self, other):
                return not self.__eq__(other)


class PackingSlipForShipping(Action):
        def __eq__(self, other):
                return isinstance(other, PackingSlipForShipping)


class Payment:
        def __init__(self, product):
                self.product = product


class Product:
        pass


class PhysicalProduct(Product):
        pass


class Payment:
        def __init__(self, product):
                self.product = product


def testCase(name, payment, rules, expectedActions):
        """Test if applying the given rules to a payment results in the expected actions"""
        rulesEngine = RulesEngine(rules)
        actualActions = rulesEngine.applyRules(payment)
        if expectedActions == actualActions:
                print(name, "passed")
        else:
                print(name, "FAILED: Expected", expectedActions, "Actual", actualActions)


if __name__ == "__main__":
        # Tests of individual rules
        testCase(
                "Packing slip for Shipping", 
                Payment(PhysicalProduct()), 
                [GeneratePackingSlipForShipping()],
                [PackingSlipForShipping()])