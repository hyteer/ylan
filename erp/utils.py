# -*- coding: utf-8 -*-
'''
Utilities for handling views
'''
import re

def test_password(password):
    p = re.compile(r'^[A-Za-z\d]{6,}$')
    if p.match(password) is not None:
        return True
    else:
        return False
