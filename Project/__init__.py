'''from svmutil import *


y, x = svm_read_problem('heart_scale')

m = svm_train(y[:200], x[:200], '-c 4 -q')


new_y = [0]
new_x = [{1:0.583333, 2:1, 3:1, 4:0.245283, 5:-0.269406, 6:-1, 7:1, 8:-0.435115, 9:1, 10:-0.516129, 12:1, 13:-1}]
new_x_2 = [{1:0.166667, 2:1, 3:1, 4:-0.132075, 5:-0.69863, 6:-1, 7:-1, 8:0.175573, 9:-1, 10:-0.870968, 12:-1, 13:0.5}]


p_label, p_acc, p_val = svm_predict(new_y, new_x_2, m, '-q')

print(p_label)
print(p_acc)
print(p_val)
'''
