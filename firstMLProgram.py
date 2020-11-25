from sklearn import tree

#features = [[140, "smooth"], [130, "smooth"], [150, "bumpy"], [170, "bumpy"]]

#labels = [ "apple", "apple", "orange", "orange", "pineapple", "pineapple", "Grape", "Grape"]

#labels = [ "apple", "apple", "orange", "orange", "pineapple", "pineapple" ]


#[weight, 2 = sharp, 1 = smooth, 0 = bumpy]
features = [[140, 1], [130, 1], [150, 0], [170, 0], [250, 2], [275, 2], [60, 1], [50, 1]]
# 0 = apple, 1 = orange, 2 = pineapple, 3 = Grape
labels = [0, 0, 1, 1, 2, 2, 3, 3]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
#guessFruit = prediction value 1/0, 1 is an orange, 0 is an apple
guessFruit = (clf.predict([[60, 1]]))

#if guessFruit == [1] then print fruit is an Orange
if guessFruit == [1]:
    print ("The Program predicts that the fruit is an Orange!")
# else if print fruit is an Apple
elif guessFruit == [0]:
    print ("The Program predicts that the fruit is an Apple!")
# else preint the fruit is a pineapple
elif guessFruit == [2]:
    print("The Program predicts that the fruit as a Pineapple!")
else:
    print("The Program predicts that the fruit is a Grape!")
