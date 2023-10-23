0x05. Python - Exceptions


#WHAT I LEARNED:
Events that take place during the execution of a program in Python are referred to as exceptions since they obstruct the program's usual logic. The Python interpreter raises an exception whenever an exception happens, and try and except blocks may be used to manage these exceptions.


The ZeroDivisionError is a built-in exception that occurs when you try to divide by zero.
The else block is executed if no exceptions occur in the try block.
The final block is always executed, regardless of whether an exception occurred or not. This is useful for cleanup operations.


You can catch more general exceptions by using the Exception class, which is the base class for all built-in exceptions. It's important to be specific in handling exceptions whenever possible so that you can respond appropriately to different types of errors in your code.
