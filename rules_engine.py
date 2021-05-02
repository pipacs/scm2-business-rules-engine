# Business rules engine

class RulesEngine:
        def __init__(self, rules):
                """Intialize with a list of business rules"""
                self.rules = rules 

        def applyRules(self, payment):
                """
                Return a list of Actions after applying the business rules to the given Payment

                Parameters:
                - payment: Payment to process

                Returns: List of Actions
                """
                actions = []
                for rule in self.rules:
                        actions += rule.apply(payment)
                return actions
