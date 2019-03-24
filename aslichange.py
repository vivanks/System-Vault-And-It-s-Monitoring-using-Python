#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 01:48:24 2019

@author: vivanksharma
"""

import os
from addfile import addfile
from removefile import removefile

cd = os.getcwd()

path = cd
early_version = []
files = []
def Diff(li1, li2): 
    return (list(set(li1) - set(li2)))


for root, dirs, filenames in os.walk(path):
	for f in filenames:
		files.append(os.path.relpath(os.path.join(root, f), path))
    
for root, dirs, filenames in os.walk(path):
	for f in filenames:
		early_version.append(os.path.relpath(os.path.join(root, f), path))
            
while 1:
    
    files = []
    for root, dirs, filenames in os.walk(path):
        for f in filenames:
            files.append(os.path.relpath(os.path.join(root, f), path))
    
    if(len(Diff(early_version,files))>0 or len(Diff(files,early_version))>0):
        print(Diff(files,early_version))
        print(Diff(early_version,files))
        
        if(len(Diff(files,early_version))>0):
            addfile()
        if(len(Diff(early_version,files))>0):
            removefile()
        
    early_version=[]
    for root, dirs, filenames in os.walk(path):
        for f in filenames:
            early_version.append(os.path.relpath(os.path.join(root, f), path))
    
    
    
    