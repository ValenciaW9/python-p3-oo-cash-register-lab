# Cash Register Lab

## Learning Goals

- Build a class with instance methods.
- Call instance methods inside of other instance methods.
- Use instance methods to track information pertinent to an instance of a class.

***

## Key Vocab

- **Class**: a bundle of data and functionality. Can be copied and modified to
accomplish a wide variety of programming tasks.
- **Initialize**: create a working copy of a class using its `__init__`
method.
- **Instance**: one specific working copy of a class. It is created when a
class's `__init__` method is called.
- **Object**: the more common name for an instance. The two can usually be used
interchangeably.
- **Object-Oriented Programming**: programming that is oriented around data
(made mobile and changeable in **objects**) rather than functionality. Python
is an object-oriented programming language.
- **Function**: a series of steps that create, transform, and move data.
- **Method**: a function that is defined inside of a class.
- **Magic Method**: a special type of method in Python that starts and ends
with double underscores. These methods are called on objects under certain
conditions without needing to use their names explicitly. Also called **dunder
methods** (for **d**ouble **under**score).
- **Attribute**: variables that belong to an object.
- **Property**: attributes that are controlled by methods.

***

## Introduction

We're going to create an Object-Oriented Cash Register that can:

- Add items of varying quantities and prices
- Calculate discounts
- Keep track of what's been added to it
- Void the last transaction

***

## Instructions

**This is a test-driven lab!** You will need to read the spec file and the test
output very carefully to solve this one.

Note that a **discount** is calculated as a percentage off of the total cash
register price (e.g. a discount of 20 means the customer receives 20% off of
their total price).

**Hint #1:** Keep in mind that to access an attribute or call an instance method
_inside_ another instance method, we use the `self` keyword to refer to the
instance on which we are operating. For example:

```py
class Person:

  def __init__(self, age=0):
    self.age = age

  def birthday(self):
    self.age += 1
```

Follow along with the tests in `lib/testing/cash_register_test.py`. Reading
along with what the tests are looking for can be really helpful!

Take it one step at a time!

**Hint #2:** The `apply_discount()` method requires some knowledge about working
with integers versus floats in Python. When you get to that method, take a look
at what return value the tests are expecting and keep in mind that Python
provides methods for changing an Integer to a Float and vice versa.

**Hint #3:** The `void_last_transaction()` method will remove the last
transaction from the total. You'll need to make an additional attribute and keep
track of that last transaction amount somehow. In what method of the class are
you working with an individual item?

**Hint #4:** Python handles mutable default values for arguments differently
than it handles immutable default values. This means that you should usually not
set default values for lists, dictionaries, and instances of classes. You can
learn more on this quirk in Python's documentation on [More Control Flow Tools
](https://docs.python.org/3/tutorial/controlflow.html#default-argument-values).