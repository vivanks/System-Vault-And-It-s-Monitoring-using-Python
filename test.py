#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 10:15:39 2019

@author: vivanksharma
"""


import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
import pyaudio
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import accuracy_score
from sklearn import tree
import pyrebase

config = {
    "apiKey": "AIzaSyDCvibFIow6J7GMaR1OIRc3yeQxl54SQfE",
    "authDomain": "fir-b73a1.firebaseapp.com",
    "databaseURL": "https://fir-b73a1.firebaseio.com",
    "projectId": "fir-b73a1",
    "storageBucket": "fir-b73a1.appspot.com",
    "messagingSenderId": "652141591985"
  }

firebase = pyrebase.initialize_app(config)

def test():
    
    S = "Press 't' if heard \nPress 'f' if not \n"
    freqs =[250.0,500.0,1000.0,2000.0,4000.0, 8000.0]
    A_f = 1
    
    points = []
    volumes =[]
    points2=[]
    volumes2=[]
    
    p = pyaudio.PyAudio()
    
    stream = p.open(format=pyaudio.paFloat32,channels=1,rate=44100,output=True)
    
    def play_freqs():
        
        volume = 0.1*A_f
        duration = 1.0  # in seconds, may be float
        fs = 44100  # sampling rate, Hz, must be integer
        print("Audiometric test\n")
        
        i=0
        while i<len(freqs):
            if i == 0:
                
                volume = 0.1*A_f
                
                samples = (np.sin(2 * np.pi * np.arange(fs * duration) * freqs[i] / fs)).astype(np.float32)
                
                stream.write(volume * samples)
                
            x = input(S)#it should continue until sounds of all frequencies from the list are played
            print("\n")
                
            if x == 'f':
                    
                volume = volume + 0.1*A_f
                samples = (np.sin(2 * np.pi * np.arange(fs * duration) * freqs[i] / fs)).astype(np.float32)
                stream.write(volume*samples)
                #points.append(freqs[i])
                #volumes.append(float(volume))
                    
                #stream.write(volume*samples)
                #points.append(freqs[i])
                #volumes.append(float(volume))
                    
            if x == 't':
                
                points2.append(freqs[i])
                volumes2.append(float(volume))
                
                if(i<len(freqs)-1):
                    i = i + 1 #it should continue with the next element from list freqs
            
                    volume = 0.1*A_f
                    samples = (np.sin(2 * np.pi * np.arange(fs * duration) * freqs[i] / fs)).astype(np.float32)
                    stream.write(volume * samples)
                
                if(i==len(freqs)-1):
                    break
                
                
    play_freqs()
    
    print(points2)
    print(volumes2)
    
    up = {}
    for i in range(5):
        
        up[int(points2[int(i)])]=volumes2[int(i)]
    
    print(up)
    db = firebase.database()
    db.child("users").child("vivank").set(up)
    F = np.array(points2)
    I = np.array(volumes2)
    plt.plot(np.array(points2),np.array(volumes2),'-o',color="green",markersize=4)
    plt.title("Results of Audiometry: Audiogram")
    plt.xlabel("Frequencies")
    plt.ylabel("Intensities")
    
    S = pd.DataFrame(I, index = F)
    
    return S 


test()
    