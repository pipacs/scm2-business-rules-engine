# Actions: results of applying business rules

class Action:
        """Base action type"""

        def __init__(self):
                pass

        def __eq__(self, other):
                return false  # Can't compare abstract Actions

        def __ne__(self, other):
                return not self.__eq__(other)


class DoGeneratePackingSlip(Action):
        """Generate a packing slip for a department"""

        def __init__(self, department):
             Action.__init__(self)
             self.department = department   

        def __eq__(self, other):
                return isinstance(other, DoGeneratePackingSlip) and self.department == other.department


class DoActivateMembership(Action):
        """Activate a membership"""

        def __eq__(self, other):
                return isinstance(other, DoActivateMembership)


class DoApplyUpgrade(Action):
        """Apply an upgrade to a membership"""

        def __eq__(self, other):
                return isinstance(other, DoApplyUpgrade)
