from svmutil import svm_predict
from Project.ScriptVector import scriptVectorize
from Project.TrainData import createModel

def evaluate(s):
    values = scriptVectorize(s)
    m = createModel()
    p_label, p_acc, p_val = svm_predict([0], values, m, '-q')
    return p_label


s = r'''
setTimeout("document.bgColor='white'", 1000);
setTimeout("document.bgColor='lightpink'", 1500);
setTimeout("document.bgColor = 'pink'", 2000);
setTimeout("document.bgColor =  'deeppink'", 2500);
setTimeout("document.bgColor = 'red'", 3000);
setTimeout("document.bgColor = 'tomato'", 3500);

'''
print(evaluate(s))
