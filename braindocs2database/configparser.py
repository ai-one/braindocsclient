#!/usr/bin/env python
""" Copyright (c) 2015 ai-one inc., La Jolla CA. All rights reserved.
"""

from __future__ import print_function
import sys
from ConfigParser import RawConfigParser
from StringIO import StringIO

def promptstring(prompt, default="", endchar=":"):
    r = raw_input("%s [%s]%s " % (prompt, default, endchar))
    if r == "":
        return default
    else:
        return r
        
def promptyesno(prompt, defaultno=True, endchar="?", repeat=True):
    default = "no" if defaultno else "yes"
    while True:
        r = promptstring(prompt, default, endchar).lower()
        if r == "yes" or r == "y":
            ret = True
            break
        elif r == "no" or r == "n":
            ret = False
            break
        else:
            if repeat == False:
                raise ValueError()
            else:
                print("usage: enter 'yes' or 'no'")
    return ret

class PromptingConfigParser(RawConfigParser):
    def __init__(self, initialize=None):
        RawConfigParser.__init__(self)
        if initialize:
            for section, items in initialize.iteritems():
                self.add_section(section)
                for key, value in items.iteritems():
                    self.set(section, key, value)
    
    def printfile(self, file=sys.stdout):
        for section in self.sections():
            print(section.upper(), file=file)
            for item in self.items(section):
                print("   %s: %s" % item, file=file)
    
    def __str__(self):
        s = StringIO()
        self.printfile(s)
        return s.getvalue()
    
    def prompt(self):
        for section in self.sections():
            print(section.upper())
            for k,v in self.items(section):
                v = promptstring("   Specify %s" % k, v)
                self.set(section, k, v)