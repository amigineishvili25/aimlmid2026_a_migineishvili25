import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score

# 1. მონაცემების ჩატვირთვა
# თუ ფაილი home-შია, სახელი ზუსტად ასე უნდა ეწეროს:
try:
    df = pd.read_csv('a_migineishvili25_93254.csv')
except FileNotFoundError:
    print("შეცდომა: ფაილი ვერ მოიძებნა. დარწმუნდი, რომ კოდი და CSV ერთ საქაღალდეშია.")
    exit()

# 2. მონაცემების მომზადება (70% Train, 30% Test)
X = df[['words', 'links', 'capital_words', 'spam_word_count']]
y = df['is_spam']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

# 3. ლოგისტიკური რეგრესიის მოდელი
model = LogisticRegression()
model.fit(X_train, y_train)

# შედეგების გამოტანა ტერმინალში README-სთვის
print("\n--- Model Results for Assignment 2 ---")
print(f"Accuracy Score: {accuracy_score(y_test, model.predict(X_test)):.4f}")
print(f"Intercept: {model.intercept_[0]:.4f}")
print(f"Coefficients (words, links, caps, spam_words): {model.coef_[0]}")

# 4. ვალიდაცია (Confusion Matrix)
y_pred = model.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)

# 5. ვიზუალიზაციები
# A: Class Distribution
plt.figure(figsize=(6, 6))
df['is_spam'].value_counts().plot(kind='pie', autopct='%1.1f%%', labels=['Legit', 'Spam'], colors=['#66b3ff','#ff9999'])
plt.title('Email Class Distribution')
plt.savefig('distribution.png')

# B: Confusion Matrix Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Predicted Legit', 'Predicted Spam'], yticklabels=['Actual Legit', 'Actual Spam'])
plt.title('Confusion Matrix Heatmap')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.savefig('confusion_matrix.png')

print("\nვიზუალიზაციები შენახულია: distribution.png და confusion_matrix.png")
