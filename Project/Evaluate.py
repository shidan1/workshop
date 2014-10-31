from svmutil import svm_predict
from Project.ScriptVector import scriptVectorize
from Project.TrainData import createModel

def evaluate(s):
    values = scriptVectorize(s)
    m = createModel()
    p_label, p_acc, p_val = svm_predict([0], values, m, '-q')
    return p_label


s = r'''
//Random password generator- by javascriptkit.com
//Visit JavaScript Kit (http://javascriptkit.com) for script
//Credit must stay intact for use

var keyList="abcdefghijklmnopqrstuvwxyz123456789"
var temp=''

function generatePass(pLength){
temp=''
for (i=0;i<pLength;i++)
temp+=keyList.charAt(Math.floor(Math.random()*keyList.length))
return temp
}

function populateForm(enterLength){
document.pGenerate.output.value=generatePass(enterLength)
}
'''
print(evaluate(s))
