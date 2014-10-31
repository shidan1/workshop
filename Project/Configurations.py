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
    featureConfig['Feature2.py'] = True
    featureConfig['Feature4.py'] = True
    featureConfig['Feature5.py'] = True
    featureConfig['Feature6.py'] = False
    featureConfig['Feature7.py'] = False
    featureConfig['Feature8.py'] = False
    featureConfig['Feature10.py'] = False
    featureConfig['Feature13.py'] = False
    featureConfig['Feature14.py'] = False
    featureConfig['Feature15.py'] = False
    featureConfig['Feature16.py'] = False
    featureConfig['Feature17.py'] = False
    featureConfig['Feature18.py'] = False
    featureConfig['Feature19.py'] = False
    featureConfig['Feature20.py'] = False
    featureConfig['Feature21.py'] = True
    featureConfig['Feature22.py'] = False
    featureConfig['Feature24.py'] = False
    featureConfig['Feature27.py'] = False
    featureConfig['Ngram.py'] = True
    
    return featureConfig
