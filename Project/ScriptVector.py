from Project.Configurations import featureConfigure
from Project.features import Feature1, Feature2, Feature4, Feature5, Feature6
from Project.features import Feature7, Feature8, Feature10, Feature13, Feature14
from Project.features import Feature15, Feature16, Feature17, Feature18, Feature19
from Project.features import Feature20, Feature21, Feature22, Feature24, Feature27
from Project.features import Ngram, ForLength, WhileLength


def scriptVectorize(script):
    featureConfig = featureConfigure()
    i = 1
    vector = dict()
    
    for feature in featureConfig:
        if featureConfig[feature] == True:
            vector[i] = eval(feature[:-2]+"run(script)")
            i += 1
    
    return [vector]
            
