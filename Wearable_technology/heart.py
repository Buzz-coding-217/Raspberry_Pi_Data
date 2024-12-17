import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, classification_report


data = pd.read_csv('data.csv')

X = data[['Heart', 'Temp', 'RR']]
y = data['Condition']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(penalty='l2', C=0.1, max_iter=1000, verbose=1)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)

print(f'Model Accuracy: {accuracy}')
print(f'Model Precision: {precision}')

user_input = {
    'Heart': float(input('Heart rate: ')),
    'Temp': float(input('Temperature: ')),
    'RR': float(input('RR: '))
}


user_df = pd.DataFrame([user_input])
user_pred = model.predict(user_df)

print(f'Prediction: {user_pred[0]}')
