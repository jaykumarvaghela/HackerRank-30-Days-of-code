#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    meal = meal_cost
    tip = (tip_percent/100)*meal_cost
    tax = (tax_percent/100)*meal_cost
    total_cost = meal+tip+tax
    print(round(total_cost))
    
    
    

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
