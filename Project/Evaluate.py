from svmutil import svm_predict
from Project.ScriptVector import scriptVectorize
from Project.TrainData import createModel

def evaluate(s):
    values = scriptVectorize(s)
    m = createModel()
    p_label, p_acc, p_val = svm_predict([0], values, m, '-q')
    return p_label


s = r'''function hello() {
alert("cruel world");
}'''
print(evaluate(s))