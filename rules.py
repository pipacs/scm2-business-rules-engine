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
                        actions.append(PackingSlip("shipping"))
                return actions


class GeneratePackingSlipForRoyalty(Rule):
        """If the payment is for a book, create a duplicate packing slip for the royalty department"""

        def apply(self, payment):
                actions = []
                if isinstance(payment.product, Book):
                        actions.append(PackingSlip("royalty"))
                return actions