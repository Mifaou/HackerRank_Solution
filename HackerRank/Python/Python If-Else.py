#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(raw_input().strip())

    if not n%2==0 or 6<n<21 :
        print ('Weird')
    else :
        print('Not Weird')