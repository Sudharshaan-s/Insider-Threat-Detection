import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from collections import Counter

threat_actors = [
	"AAM0658",
	"AJR0932",
	"BDV0168",
	"MSO0222"
]

start_date = joint["date"].iloc[0]
end_date = joint["date"].iloc[-1]
time_horizon = (end_date - start_date).days + 1

def date_to_index(date):
	return (date - start_date).days

def extract_time_series_by_user(user_name, df):
	return df[df["user"] == user_name]

def vectorize_user_time_series(user_name, df):
	user_time_series = extract_time_series_by_user(user_name, df)
	x = np.zeros((len(feature_map), time_horizon))
	event_date_indicates = user_time_series["date"].apply(date_to_index).to_numpy()
	event_features = user_time_series["feature"].to_numpy()
	for i in range(len(event_date_indicates)):
		x[event_features[i], event_date_indices[i]] += 1
	return x

def vectorize_dataset(df):
	users = set(df["user"].values)
	X = np.zeros((len(users), len(feature_map), time_horizon))
	y = np.zeros((len(users)))
	for index, user in enumerate(users):
		x = vectorize_user_time_series(user, df)
		X[index, :, :] = x
		y[index] = int(user in threat_actors)

X, y = vectorize_dataset(joint)

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y)

X_train_reshaped = X_train.reshape([X_train.shape[0], X_train.shape[1] * X_train.shape[2]])
X_test_reshaped = X_test.reshape([X_test.shape[0], X_test.shape[1] * X_test.shape[2]])

x_train_normal = X_train_reshaped[y_train == 0, :]
x_train_threat = X_train_reshaped[y_train == 1, :]
x_test_normal = X_test_reshaped[y_test == 0, :]
x_test_threat = X_test_reshaped[y_test == 1, :]

contamination_parameter = 0.035
IF = IsolationForest(n_estimators=100, max_samples=256, contamination=contamination_parameter)

IF.fit(X_train_reshaped)

normal_scores = IF.decision_function(X_train_normal)
fig = plt.figure(figsize=(8, 4), dpi=600, facecolor="w", edgecolor="k")
normal = plt.hist(normal_scores, 50, density=True)

plt.xlim((-0.2, 0.2))
plt.xlabel("Anomaly score")
plt.ylabel("Percentage")
plt.title("Anomaly score for normal")

anomaly_scores = IF.decision_function(X_train_threat)
fit = plt.figure(figsize=(8, 4), dpi=600, facecolor="w")
anomaly = plt.hist(anomaly_scores, 50, density=True)

plt.xlim((-0.2, 0.2))
plt.xlabel("Anomaly score")
plt.ylabel("Percentage")
plt.title("Anomaly score for threat")

cutoff = 0.12

s = IF.decision_function(X_train_reshaped)
print(Counter(y_train[cutoff > s]))



s = IF.decision_function(X_test_reshaped)
print(Counter(y_test[cutoff > s]))
