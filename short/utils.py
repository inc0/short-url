# -*- coding: utf-8 -*-
import random
import string
import os
import time


def generate_suffix():
    suffix = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(4))
    return suffix