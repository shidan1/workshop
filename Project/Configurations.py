from Project.features import *
import os
from Project.features.Feature1 import numberEval

def featureConfigure():   
    path = 'features/.'
    """
    Feature counter for later use
    """
    # featureCounter = (len([feature for feature in os.listdir(path)]))
    
    featureConfig = dict()
    for feature in os.listdir(path):
        featureConfig[feature] = False
    
    """
    Allowing ONLY the following features: 
    """
    featureConfig['Feature1.py'] = True
    featureConfig['Feature21.py'] = True
    featureConfig['Ngram.py'] = True
    
    return featureConfig
