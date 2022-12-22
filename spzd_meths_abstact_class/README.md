# py_OOP - Specilized methods

## Class methods
Class methods are methods that, like class variables, work on the class itself, and
not on the class objects that are instantiated. You can say that they are methods bound
to the class, not to the object.

When can this be useful? There are several possibilities, here are the two most popular:
- we control access to class variables, e.g., to a class variable containing information 
about the number of created instances or the serial number given to the last produced 
object, or we modify the state of the class variables;
- we need to create a class instance in an alternative way, so the class method can be 
implemented by an alternative constructor.

Convention
To be able to distinguish a class method from an instance method, the programmer signals 
it with the @classmethod decorator preceding the class method definition.
Additionally, the first parameter of the class method is cls, which is used to refer to
the class methods and class attributes.


## Static methods
Static methods are methods that do not require (and do not expect!) a parameter indicating
 the class object or the class itself in order to execute their code.

When can it be useful?
When you need a utility method that comes in a class because it is semantically related, 
but does not require an object of that class to execute its code;
consequently, when the static method does not need to know the state of the objects or classes.

Convention
To be able to distinguish a static method from a class method or instance method, the 
programmer signals it with the @staticmethod decorator preceding the class method definition.
Static methods do not have the ability to modify the state of objects or classes, because 
they lack the parameters that would allow this.


## Using static and class methods - comparison
The time has come to compare the use of class and static methods:
1. a class method requires 'cls' as the first parameter and a static method does not;
2. a class method has the ability to access the state or methods of the class, and a
 static method does not;
3. a class method is decorated by '@classmethod' and a static method by '@staticmethod';
4. a class method can be used as an alternative way to create objects, and a static method
 is only a utility method.

# py_OOP - Abstract Classes

## Abstract Classes - abc module
import abc - class Abstract(abc.ABC): - @abc.abstractmethod
## Method overriding
abstract methods must be subclass overrided
## Multiple Inheritance
When you plan to implement a multiple inheritance from abstract classes, remember that
an effective subclass should override all abstract methods inherited from its super classes.
## Summary:
- Abstract Base Class (ABC) is a class that cannot be instantiated. Such a class is a base
 class for concrete classes;
- ABC can only be inherited from;
- we are forced to override all abstract methods by delivering concrete method 
implementations.



