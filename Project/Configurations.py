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
    featureConfig['Feature7.py'] = True
    featureConfig['Feature8.py'] = False
    featureConfig['Feature10.py'] = True
    featureConfig['Feature13.py'] = True
    featureConfig['Feature14.py'] = True
    featureConfig['Feature15.py'] = True
    featureConfig['Feature16.py'] = True
    featureConfig['Feature17.py'] = True
    featureConfig['Feature18.py'] = False
    featureConfig['Feature19.py'] = True
    featureConfig['Feature20.py'] = True
    featureConfig['Feature21.py'] = False
    featureConfig['Feature22.py'] = True
    featureConfig['Feature24.py'] = True
    featureConfig['Feature27.py'] = True
    featureConfig['Ngram.py'] = True
    featureConfig['ForLength.py'] = True
    featureConfig['WhileLength.py'] = False
    
    return featureConfig
