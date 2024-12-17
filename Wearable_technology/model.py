import pandas as pd
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import StandardScaler

file_path = 'Stress-Lysis.csv'
data = pd.read_csv(file_path)

X = data[['Humidity', 'Temperature', 'Step_count']]
y = data['Stress_Level']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

learning_rate = 0.01
epochs = 10

model = SGDRegressor(learning_rate='constant', eta0=learning_rate, max_iter=epochs, random_state=42)
model.fit(X_scaled, y)

user_input_humidity = float(input("Humidity: "))
user_input_temperature = float(input("Temperature: "))
user_input_step_count = float(input("Step Count: "))

user_input_scaled = scaler.transform([[user_input_humidity, user_input_temperature, user_input_step_count]])

predicted_stress_level = model.predict(user_input_scaled)

print(f"\nPredicted Stress Level: {predicted_stress_level[0]:.2f}")
