# Business rules

from products import *
from actions import *

class Rule:
        """Base rule"""

        def apply(self, payment):
                return []


class GeneratePackingSlipForShipping(Rule):
        """If the payment is for a physical product, generate a packing slip for shipping"""

        def apply(self, payment):
                actions = []
                if isinstance(payment.product, PhysicalProduct):
                        actions.append(DoGeneratePackingSlip("shipping"))
                return actions


class GeneratePackingSlipForRoyalty(Rule):
        """If the payment is for a book, create a duplicate packing slip for the royalty department"""

        def apply(self, payment):
                actions = []
                if isinstance(payment.product, Book):
                        actions.append(DoGeneratePackingSlip("royalty"))
                return actions


class ActivateMembership(Rule):
        """If the payment is for a membership, activate that membership"""

        def apply(self, payment):
                actions = []
                if isinstance(payment.product, Membership):
                        actions.append(DoActivateMembership())
                return actions


class ApplyUpgrade(Rule):
        """If the payment is an upgrade to a membership, apply the upgrade"""

        def apply(self, payment):
                actions = []
                if isinstance(payment.product, Upgrade):
                        actions.append(DoApplyUpgrade())
                return actions


class InformOwner(Rule):
        """If the payment is for a membership or upgrade, e-mail the owner and inform them of the activation/upgrade"""

        def apply(self, payment):
                actions = []
                if isinstance(payment.product, Upgrade) or isinstance(payment.product, Membership):
                        actions.append(DoInformOwner(payment.product.owner))
                return actions
                