# Product types

class Product:
        """Base product type"""
        pass


class PhysicalProduct(Product):
        """A physical product"""
        pass


class Book(PhysicalProduct):
        """A book"""
        pass 


class Membership(Product):
        """A membeship with an owner"""

        def __init__(self, owner):
                self.owner = owner


class Upgrade(Product):
        """An uprgade to a membership"""

        def __init__(self, owner):
                self.owner = owner


class Video(PhysicalProduct):
        """A (physical) video"""

        def __init__(self, title):
                self.title = title 


