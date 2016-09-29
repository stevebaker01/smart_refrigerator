import re
import unittest


# 1. Write a Python function called “is_palindrome”
def is_palindrome(string):
    if not isinstance(string, str):
        return False
    string = re.sub('[^0-9a-zA-Z]+', '', string.lower())
    return True if string[::-1] == string else False

"""
1a. Please explain the advantages and disadvantages to your solution.

advantages: compact, simple, easy to read, understand and maintain
disadvantages: assumes to return False for things that aren't strings without
    spec, to avoid exeptions
"""


# Write the unittest class “TestIsPalindrome” that extends unittest.TestCase
# that sufficiently tests the “is_palindrome” function from problem 1.
class IsPalindromeTest(unittest.TestCase):

    def testEmptyString(self):
        self.assertEqual(is_palindrome(''), True)

    def testPalindrome(self):
        self.assertEqual(is_palindrome('redivider'), True)

    def testNotPalindrome(self):
        self.assertEqual(is_palindrome('divider'), False)

    def testNotString(self):
        self.assertEqual(is_palindrome(None), False)
        self.assertEqual(is_palindrome(1), False)
        self.assertEqual(is_palindrome(object()), False)
        self.assertEqual(is_palindrome([]), False)

    def testExamplesFromInstructions(self):

        self.assertEqual(is_palindrome('abba'), True)
        self.assertEqual(is_palindrome('race car'), True)
        self.assertEqual(is_palindrome('A man, a plan, a canal, Panama!'),
                         True)
        self.assertEqual(is_palindrome('Not a palindrome'), False)


# 3. Given the following base class:
class Animal(object):

    legs = 0
    opposing_thumbs = False

    def breath(self):
        print('Breathing')

    def speak(self):
        print('')


# Show what the class hierarchy would be for Man, Woman, Dog, Cat,
# Horse and Zebra.

class Human(Animal):

    legs = 2
    opposing_thumbs = True

    def speak(self):
        print('Hello.')


class Woman(Human):

    def wears_skirt(self):
        print('Sometimes.')


class Man(Human):

    def wears_skirt(self):
        print('Rarely.')


class Quadruped(Animal):

    legs = 4


class Cat(Quadruped):

    def speak(self):
        print('Meow.')


class Dog(Quadruped):

    def speak(self):
        print('Woof.')


class Horse(Quadruped):

    def speak(self):
        print("I'm Mr. Ed.")


class Zebra(Quadruped):

    def speak(self):
        print('<contact publicist>')


class Snake(Animal):

    pass

"""
3a. Explain why you chose your class structure.

There are many ways to build this basic class hierarchy this demonstrates
a simple, reasonable, and rational solution to a simple problem.
"""

"""
4. Describe how to find the middle element of a linked list. What
are the advantages and disadvantages to your solution? Is there a better
solution? Explain.

Either count through each element once and then count (num elements/2).
OR
set two pointers and move one by one element and the other by two on each pass
when the pointer moving by two reaches the last element the pointer moving
by one will reach the center.

The later will be more efficient as only as many computations are as
elements are needed. The former will require 50% more computations (counts).
"""

"""
6. In Python, what is a decorator? Please give an example.

A decorator in python is pattern that allows for modification and/or
introspection of a given method. My favorite example is a profiling function
which will time, or profile, a given function. I use this here and there so it
is the first decorator/function in my personal utils package... :)

https://github.com/stevebaker01/steves-utilities/blob/master/steves_utilities/profiler.py
"""

"""
7. What is the difference between a process and a thread? What are some
advantages and disadvantages of each?

In the broadest sense a process is a programatic task. Processes can often be
broken into sub-tasks called threads which can be understood as smaller parts
of the overall process that can be run separately and usually concurrntly.

Threaded programming is threcherous in any language as concurrency and race
conditions can present programmatic and architectural challenges but they can
dramatically reduce the time it takes to execute many processes or large
processes. "concurrent" is a new standard library in python 3 which can really
help when writting threaded processes and the new exception flow in Python 3
is also an improvement for threaded programs. concurrent is backward compatible
python 2.7 at least, but of course not the exception flow :-/
"""

"""
8. In Python, what is the difference between the “==” operator and the “is”
operator?

"==" tests equality (is one value equal to another)
"is" tests identity (is one object the same object as the one on the other
    side of the "is")
"""

"""
9. In Python, what is a module? What is it used for?

A module is a python file containing a discrete unit of functionality. Python
classes and functions that can be imported by other python code to perform
a set of processes needed by the including program.
Modules are often distributed in packages which contain one or more module.
Modules are esentually modular, portable functionality.
Larger python programs will often generally contain many of their own modules
which offer a natuaral way to separate functionality.
"""

"""
10. Regarding web frameworks, explain what an html template is and how it is
related to a view.

An html templating system is a common component of many web frameworks.
They basicaly allow the (data) model for the application be expressed
(rendered) in the client as the "view", usually in a browser. Most templating
systems allow for html, css, and java coding as usual for web apps but with
special syntax to tell the framework how to assemble the dom for the view.
So basically a single template is a file containing instructions html, css,
and/or javascript on how to render the desired "view" of the apps data model
(described in code elsewhere in the farmework). The framework generally
includes special syntax and conventions for proceduralizing the construction
of the view's document object model to accommodate the data model.
"""