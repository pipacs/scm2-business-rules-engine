# Actions: results of applying business rules

class Action:
        """Base action type"""

        def __eq__(self, other):
                return false  # Can't compare abstract Actions

        def __ne__(self, other):
                return not self.__eq__(other)


class PackingSlipForShipping(Action):
        """Generate a packing slip for Shipping"""

        def __eq__(self, other):
                return isinstance(other, PackingSlipForShipping)


