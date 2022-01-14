# Welcome to design-patterns-python

Examples using design patterns with python.


### Prerequisites

* python3 [latest](https://www.python.org/downloads/)
* virtualenv [latest version](https://virtualenv.pypa.io/en/latest/)
* ChromeDriver [Chrome for Selenium](https://chromedriver.chromium.org/)


### Manage environment

* Create a environment
```
pip3 install virtualenv
python3 -m virtualenv env -p python3
```

* Select environment
```
source env/bin/activate
```


### The SOLID concepts

The Single-responsibility principle: "There should never be more than one reason for a class to change."[5] In other words, every class should have only one responsibility.[6]
The Open–closed principle: "Software entities ... should be open for extension, but closed for modification."[7]
The Liskov substitution principle: "Functions that use pointers or references to base classes must be able to use objects of derived classes without knowing it."[8] See also design by contract.[8]
The Interface segregation principle: "Many client-specific interfaces are better than one general-purpose interface."[9][4]
The Dependency inversion principle: "Depend upon abstractions, [not] concretions."[10][4]


### Factory
#### Motivation
* Object creation logic becomes too convoluted/complejo
* Initializer is not descriptive

* Use this when the creation be so complicated.
* Can create hierarchy

#### Teory
 _A component responsible solely for the wholesale (not piecewise) creation of objects_=

 * A factory method is a static method that creates objects