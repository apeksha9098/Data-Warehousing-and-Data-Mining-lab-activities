import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
dataset = pd.read_csv(r'C:\Users\DELL\python\Diabetes.csv')
print("Columns in CSV:", dataset.columns)
split = int(len(dataset) * 0.7)
train = dataset[:split]
test = dataset[split:]
feature_cols = ['Pragnency', 'Glucose', 'Blod Pressure', 'Skin Thikness', 
                'Insulin', 'BMI', 'DFP', 'Age']
target_col = 'Diabetes'
X_train = train[feature_cols].values
y_train = train[target_col].values

X_test = test[feature_cols].values
y_test = test[target_col].values
model = GaussianNB()
model.fit(X_train, y_train)
predicted = model.predict(X_test)
print("\nActual Class: ", y_test[:20])
print("Predicted Class:", predicted[:20])
print("\nConfusion Matrix:")
print(metrics.confusion_matrix(y_test, predicted))
print("\n******** Classification Measures *********")
print("Accuracy:", metrics.accuracy_score(y_test, predicted))
print("Recall:", metrics.recall_score(y_test, predicted))
print("Precision:", metrics.precision_score(y_test, predicted))
print("F1-Score:", metrics.f1_score(y_test, predicted))
