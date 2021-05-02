# SCM Coding Test 2: Business Rules Engine

## Dependencies

* Python 3

## Running The Unit Test

```sh
cd <repository_root>
python3 test.py
```

## Design Notes

### Business Rules Engine

The business rules engine (```RulesEngine```) type is implemented in _rules_engine.py_. 

It has a list of ```Rule```s and an ```apply()``` method which applies all rules to a given payment, and returns zero or more ```Action```s.

### Business Rules

A business rule (```Rule```), when applied to a payment, generates zero or more ```Action```s.

The business rules class hierarchy is in _rules.py_. To extend the system with new rules, define them here and append them to the ```RulesEngine``` initializer parameter list.

### Actions

Actions are the result of applying business rules to a payment.

The ```Action``` class hierarchy is in _actions.py_. To extend the system with new actions, define them here.

For testability, ```Action```s should implement the "==" operator (```__eq__()``` method).

### Other

* Product class hierarchy is in _products.py_
* Books and videos are treated as physical products
* Actions, products and payment are just symbolic implementations, they are lacking many basic properties
