import pickle

# Load Model
with open('models/spam_classifier.pkl', 'rb') as f:
    model = pickle.load(f)

# Load Vectorizer
with open('models/vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# User Input
msg = input("Enter Message: ")

# Transform Input
data = vectorizer.transform([msg])

# Predict
result = model.predict(data)

if result[0] == 1:
    print("Spam Email")
else:
    print("Not Spam")