from selenium.common.exceptions import NoSuchElementException

import browser
import time
import page
import re

A = [[1,2,3], [4,5,6]]
# B = [list(x) for x in zip(*A)]    # without map
# C = list(map(list, zip(*A)))      # with map