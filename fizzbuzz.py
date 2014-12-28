#! /usr/bin/python
# -*- coding: utf-8 -*-

# FizzBuzz関数
def fizzbuzz():
    x = 0
    for num in range(1, 101):
        x += 1
        if x%3 == 0 and x%5 == 0:
            print("FizzBuzz")
        elif x%3 == 0:
            print("Fizz")
        elif x%5 == 0:
            print("Buzz")
        else:
            print x

if __name__ == "__main__":
    fizzbuzz()
