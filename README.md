# py_OOP
Labs, exercises, and topics from:
PCPP1: Advanced Perspective of Classes and Object-Oriented Programming
 
- OOP_bases: Classes, instances, attributes, methods, class and instance data (vars);
    - Classes, Instances, Attributes, Methods - Intro (1.1...)
    - Class and Instance data (instance & class variables - attribs) (1.2...)
- shallow and deep 'copy' operations;
- abstract classes, method overriding, static and class methods, special methods;
    - core_syntax, special purpose methods or magic methods (2.1...)
- inheritance, polymorphism, subclasses, and encapsulation;
    - Single vs Multiple Inheritance - MRO, diamond problem (2.2...)
	- Polymorphism, subclass overriding, duck typing 
	- Extended funct. arg. syntax, \*args \*\*kwargs, (2.3...)
	- Decorators, funct. & class decorators, stacking (2.4...)
	- specialized methods: static and class methods (2.5...)
	- Abstract classes, @abc.abstractmethod, meth. overriding, mult. inher. (2.6...)
	- Encapsulation, composition, inheritance from built-in classes
- advanced exception handling techniques;
- the pickle and shelve modules;
- metaclasses.

## OOP Bases: type (what is a type?)
A type is one of the most fundamental and abstract terms of Python:
- it is the foremost type that any class can be inherited from;
- as a result, if you’re looking for the type of class, then type is returned;
- in all other cases, it refers to the class that was used to instantiate the object; 
it’s a general term describing the type/kind of any object;
- it’s the name of a very handy Python function that returns the class information about 
the objects passed as arguments to that function;
- it returns a new type object when type() is called with three arguments; we'll talk 
about this in the 'metaclass' section.
Python comes with a number of built-in types, like numbers, strings, lists, etc., that are
used to build more complex types. Creating a new class creates a new type of object,
allowing new instances of that type to be made.
> Information about an object’s class is contained in __class__.

## Python Core Syntax
What are some real life cases which could be implemented using special methods?
Think of any complex problems that we solve every day like:
- adding time intervals, like: add 21 hours 58 minutes 50 seconds to 1hr 45 minutes
22 seconds;
- adding length measurements expressed in the imperial measurement system, like: add 
2 feet 8 inches to 1 yard 1 foot 4 inches.
With classes equipped with custom special methods, the tasks may start to look simpler.
Of course, don’t forget to check the type of the objects passed as arguments to special 
methods. If someone uses your classes, they might use them incorrectly, so a good __add__ 
method should check whether it’s possible to perform the addition before doing it, or 
else raise an exception

