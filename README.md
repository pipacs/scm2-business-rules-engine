# SCM Coding Test 2: Business Rules Engine

## Dependencies

* Python

## Running The Unit Test

```sh
cd <repository_root>
python3 test.py
```

## Implementation Notes

* Product class hieratchy is in _products.py_
* Action class hierarchy is in _actions.py_
  * To extend the system with new actions, define them here
* Business rules class hierarchy is in _rules.py_
  * To extend the system with new rules, define them here, and append them to the ```RuleEngine``` initializer parameter list
* Books and videos are treated as physical products
* Actions and products are just symbolic, they are lacking many basic properties
