# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 16:45:54 2021

@author: DELL_04
"""
import pandas as pd
import numpy as np
from scipy import stats

def learning_changed(path):
    data = pd.read_table(path)
    timingdf = periodgenerator(data.iloc[:,5:7])
    redlightON = timingdf['redLED']
    filmOpen = timingdf['greenLED'].dropna()
    trainmixtest = np.arange(10,40)
    train_session = [ j 
                     for i in range(24)
                     for j in range(10,40)
                     if filmOpen[i][0]-redlightON[j][-1] ==1 
                     ]
    test_session = [ i 
                    for i in trainmixtest 
                    if i not in train_session
                    ]
    maximun_position = max(data['fish 1 x'])
    minimun_position = min(data['fish 1 x'])
    roi = (maximun_position+minimun_position)/3
    
    ratioPrered_baseline_1 = [ len([i for i in data['fish 1 x'][redlightON[j][0]-200:redlightON[j][0]]
                              if i < roi]) / 200
                        for j in range(10)
                        ]
    ratioInred_baseline_1 = [ len([i for i in data['fish 1 x'][redlightON[j]]
                              if i < roi]) / len(redlightON[j])
                        for j in range(10)
                        ]
    
    ratioPrered_train_1 = [ len([i for i in data['fish 1 x'][redlightON[train_session[j]][0]-200:redlightON[train_session[j]][0]]
                              if i < roi]) / 200
                        for j in range(24)
                        ]
    ratioInred_train_1 = [ len([i for i in data['fish 1 x'][redlightON[train_session[j]]]
                              if i < roi]) / len(redlightON[train_session[j]])
                        for j in range(24)
                        ]
    
    ratioPrered_test_1 = [ len([i for i in data['fish 1 x'][redlightON[test_session[j]][0]-200:redlightON[test_session[j]][0]]
                              if i < roi]) / 200
                        for j in range(6)
                        ]
    ratioInred_test_1 = [ len([i for i in data['fish 1 x'][redlightON[test_session[j]]]
                              if i < roi]) / len(redlightON[test_session[j]])
                        for j in range(6)
                        ]
    
    ratioInfilm_1 = [ len([i for i in data['fish 1 x'][filmOpen[j]]
                              if i < roi]) / len(filmOpen[j])
                        for j in range(24)
                        ]
    
    fish1_baseline = pd.DataFrame({'redOff':ratioPrered_baseline_1, 'redOn':ratioInred_baseline_1})
    fish1_test = pd.DataFrame({'redOff':ratioPrered_test_1, 'redOn':ratioInred_test_1})
    fish1_train = pd.DataFrame({'redOff':ratioPrered_train_1, 'redOn':ratioInred_train_1, 'filmOpen':ratioInfilm_1})

    ratioPrered_baseline_2 = [ len([i for i in data[' fish 2 x'][redlightON[j][0]-200:redlightON[j][0]]
                              if i < roi]) / 200
                        for j in range(10)
                        ]
    ratioInred_baseline_2 = [ len([i for i in data[' fish 2 x'][redlightON[j]]
                              if i < roi]) / len(redlightON[j])
                        for j in range(10)
                        ]
    
    ratioPrered_train_2 = [ len([i for i in data[' fish 2 x'][redlightON[train_session[j]][0]-200:redlightON[train_session[j]][0]]
                              if i < roi]) / 200
                        for j in range(24)
                        ]
    ratioInred_train_2 = [ len([i for i in data[' fish 2 x'][redlightON[train_session[j]]]
                              if i < roi]) / len(redlightON[train_session[j]])
                        for j in range(24)
                        ]
    
    ratioPrered_test_2 = [ len([i for i in data[' fish 2 x'][redlightON[test_session[j]][0]-200:redlightON[test_session[j]][0]]
                              if i < roi]) / 200
                        for j in range(6)
                        ]
    ratioInred_test_2 = [ len([i for i in data[' fish 2 x'][redlightON[test_session[j]]]
                              if i < roi]) / len(redlightON[test_session[j]])
                        for j in range(6)
                        ]
    
    ratioInfilm_2 = [ len([i for i in data[' fish 2 x'][filmOpen[j]]
                              if i < roi]) / len(filmOpen[j])
                        for j in range(24)
                        ]
    
    fish2_baseline = pd.DataFrame({'redOff':ratioPrered_baseline_2, 'redOn':ratioInred_baseline_2})
    fish2_test = pd.DataFrame({'redOff':ratioPrered_test_2, 'redOn':ratioInred_test_2})
    fish2_train = pd.DataFrame({'redOff':ratioPrered_train_2, 'redOn':ratioInred_train_2, 'filmOpen':ratioInfilm_2})
    
    return fish1_baseline,fish1_train,fish1_test, fish2_baseline,fish2_train,fish2_test