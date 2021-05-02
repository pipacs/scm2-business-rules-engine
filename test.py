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
                [DoGeneratePackingSlip("shipping")]
        )
        testCase(
                "No packing slip for Shipping", 
                Payment(Membership("joe")), 
                [GeneratePackingSlipForShipping()],
                []
        )        
        testCase(
                "Packing slip for Royalty", 
                Payment(Book()), 
                [GeneratePackingSlipForRoyalty()],
                [DoGeneratePackingSlip("royalty")]
        )
        testCase(
                "No packing slip for Royalty", 
                Payment(Video("barryLyndon")), 
                [GeneratePackingSlipForRoyalty()],
                []
        )
        testCase(
                "Activate membership",
                Payment(Membership("owner@me.com")),
                [ActivateMembership()],
                [DoActivateMembership()]
        )
        testCase(
                "Don't activate membership",
                Payment(Upgrade("owner@me.com")),
                [ActivateMembership()],
                []
        )
        testCase(
                "Apply upgrade",
                Payment(Upgrade("owner@me.com")),
                [ApplyUpgrade()],
                [DoApplyUpgrade()]
        )
        testCase(
                "Don't apply upgrade",
                Payment(Membership("owner@me.com")),
                [ApplyUpgrade()],
                []
        )
        testCase(
                "Inform owner of upgrade",
                Payment(Upgrade("upgradeowner@me.com")),
                [InformOwner()],
                [DoInformOwner("upgradeowner@me.com")]
        )
        testCase(
                "Don't inform owner of upgrade or membership",
                Payment(Book()),
                [InformOwner()],
                []
        )
        testCase(
                "Inform owner of membership",
                Payment(Membership("member@me.com")),
                [InformOwner()],
                [DoInformOwner("member@me.com")]
        )
        testCase(
                "Add video 'First Aid'",
                Payment(Video("learningToSki")),
                [AddFirstAidVideo()],
                [DoAddFirstAidToPackingSlip]
        )
        testCase(
                "Don't add 'First Aid' to wrong video",
                Payment(Video("theOrchestra")),
                [AddFirstAidVideo()],
                []
        )
        testCase(
                "Don't add 'First Aid' to book",
                Payment(Book()),
                [AddFirstAidVideo()],
                []
        )
        testCase(
                "Commission payment to agent",
                Payment(Video("learningToSki")),
                [GenerateCommissionPaymentToAgent()],
                [DoGenerateCommissionPaymentToAgent()]
        )
        testCase(
                "No commission payment to agent",
                Payment(Upgrade("upgradeowner@me.com")),
                [GenerateCommissionPaymentToAgent()],
                []
        )
        