# Product types

class Product:
        """Base product type"""
        
        def __init__(self):
                """Initialize with a default SKU ID"""
                self.sku = type(self).__name__


class PhysicalProduct(Product):
        """A physical product"""
        pass


class Book(PhysicalProduct):
        """A book"""
        pass 


class Membership(Product):
        """A membeship with an owner"""

        def __init__(self, owner):
                """Initialize with an owner"""
                Product.__init__(self)
                self.owner = owner


class Upgrade(Product):
        """An upgrade to a membership"""

        def __init__(self, owner):
                """Initialize with an owner"""
                Product.__init__(self)
                self.owner = owner


class Video(PhysicalProduct):
        """A (physical) video"""

        def __init__(self, sku):
                """Initialize with a custom SKU ID"""
                Product.__init__(self)
                self.sku = sku 
