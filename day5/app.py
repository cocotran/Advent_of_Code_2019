import sys
import os
sys.path.append(os.path.abspath("/Users/anhtran/codeventure"))
from intcode import *

input = [int(i) for i in open('input.txt', 'r').read().split(',')]

computer = Computer(input, input_=(1,))
computer.run()