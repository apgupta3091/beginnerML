from sklearn import tree

#features = [[140, "smooth"], [130, "smooth"], [150, "bumpy"], [170, "bumpy"]]
#labels = [ "apple", "apple", "orange", "orange" ]

#[weight, 2 = sharp, 1 = smooth, 0 = bumpy]
features = [[140, 1], [130, 1], [150, 0], [170, 0], [250, 2], [275, 2]]
# 0 = apple, 1 = orange, 2 = pineapple
labels = [0, 0, 1, 1, 2, 2]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

#guessFruit = prediction value 1/0, 1 is an orange, 0 is an apple
guessFruit = (clf.predict([[260, 0]]))

#if guessFruit == [1] then print fruit is an Orange
if guessFruit == [1]:
    print ("The Program predicts that the fruit is an Orange!")
# else if print fruit is an Apple
elif guessFruit == [0]:
    print ("The Program predicts that the fruit is an Apple!")
# else preint the fruit is a pineapple
else:
    print("The Program predicts that the fruit as a Pineapple!")
