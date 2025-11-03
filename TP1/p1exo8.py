Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> random : int(0,100)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    random : int(0,100)
ValueError: int() base must be >= 2 and <= 36, or 0
>>> import random
>>> nombre = random.randint(0,100)
>>> print(f"le nombre généré est : {nombre}. ")
le nombre généré est : 39. 
