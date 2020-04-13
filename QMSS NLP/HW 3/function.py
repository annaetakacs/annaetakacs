#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 17:05:13 2020

@author: annatakacs
"""

def gen_senti(cwd_in, arbitrary_text):
    from nltk import word_tokenize
    cwd = cwd_in
    with open(cwd + "/" + "positive-words.txt", "rb") as file:
       pw = file.read().decode('utf-8').split( )
       pw = set(pw)
    with open(cwd + "/" + "negative-words.txt", "rb") as file:
        nw = file.read().decode('latin-1').split( )
        nw = set(nw)
    pc = 0
    nc = 0
    if len(arbitrary_text) != 0:
        regexp = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        arbitrary_text = arbitrary_text.replace(regexp, '')
        tmp_stem = [word for word in word_tokenize(arbitrary_text)]
        print(tmp_stem)
        for i in tmp_stem: 
            if i in pw:
                pc += 1
            elif i in nw: 
                nc -= 1
            elif i not in pw and i not in nw:
                continue  
        X_std =  (0 - nc) % (pc - nc);
        X_scaled = X_std * ((-1) - 1) + 1;
            
        return pc, nc, X_scaled