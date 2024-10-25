def get_presision(TP,FN,FP,TN):
    precission = TP/(TP+FP)
    return precission

def get_accurasy(TP,FN,FP,TN):
    accurasy = (TP+TN)/(TP+TN+FP+FN)
    return accurasy

def get_recall(TP,FN,FP,TN):
    recall = TP/(TP+FN)
    return recall

def get_f1score(TP,FN,FP,TN):
    presision = get_presision(TP,FN,FP,TN)
    recall = get_recall(TP,FN,FP,TN)
    f1 = 2 * presision * recall / (presision + recall)
    return f1

TP = 18
FN = 2
FP = 8
TN = 72

#titanic
#TP = 585
#FN = 34
#FP = 182
#TN = 245


print("accuracy = ", get_accurasy(TP,FN,FP,TN))
print("presision = ", get_presision(TP,FN,FP,TN))
print("recall = ", get_recall(TP,FN,FP,TN))
print("f1 score = ", get_f1score(TP,FN,FP,TN))

