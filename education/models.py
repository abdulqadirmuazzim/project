# from django.db import models
import sys
import random as r
import string as s

some = s.ascii_letters + s.digits + s.punctuation
# Create your models here.


sim = r.choices(some, k=20)


if sys.argv[1] == "come_function":
    passo = sys.argv[1]
    print("password is: ", *sim)

else:
    print('Usage: python app.py [params] eg. funct...', sys.argv[0])
