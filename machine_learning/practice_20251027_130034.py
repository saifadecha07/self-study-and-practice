# Session: Morning study session
# Note: Need to memorize this syntax.

from sklearn.tree import DecisionTreeClassifier

# Source: Google Machine Learning Crash Course
# Simple Decision Tree
features = [[140, 1], [130, 1], [150, 0], [170, 0]] # weight, texture (1=smooth, 0=bumpy)
labels = [0, 0, 1, 1] # 0=apple, 1=orange

clf = DecisionTreeClassifier()
clf = clf.fit(features, labels)
print('Prediction:', clf.predict([[160, 0]]))