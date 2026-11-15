# Module 5 Quiz — Machine Learning

25 questions · timed, 35 minutes · covers every unit in Module 5.

Difficulty mix: Recall 10 · Application 10 · Analysis 5.

**1. Which library provides LogisticRegression, KMeans and train_test_split?**  _(Multiple choice · Recall)_

- A) pandas
- B) scikit-learn
- C) seaborn
- D) statsmodels

**2. In supervised learning, the training data includes…**  _(Multiple choice · Recall)_

- A) only features
- B) features and labels
- C) only labels
- D) no data

**3. `test_size=0.25` keeps what share for testing?**  _(Multiple choice · Recall)_

- A) `2.5%`
- B) 25%
- C) 75%
- D) 0.25 rows

**4. Regression predicts a continuous value.**  _(True/False · Recall)_

- A) True
- B) False

**5. Which metric is the square root of MSE?**  _(Multiple choice · Recall)_

- A) R²
- B) RMSE
- C) MAE
- D) Accuracy

**6. Which attribute holds K-Means cluster centres?**  _(Multiple choice · Recall)_

- A) centers
- B) `cluster_centers_`
- C) `means_`
- D) `centroids()`

**7. Which step comes immediately after training in the ML pipeline?**  _(Multiple choice · Recall)_

- A) Collection
- B) Evaluation
- C) Preprocessing
- D) Feature engineering

**8. Is dimensionality reduction a type of unsupervised learning?**  _(Yes/No · Recall)_

- A) Yes
- B) No

**9. `classification_report()` includes…**  _(Multiple choice · Recall)_

- A) RMSE
- B) precision, recall and F1
- C) inertia
- D) coefficients

**10. Which module contains Pipeline?**  _(Multiple choice · Recall)_

- A) `sklearn.pipeline`
- B) `sklearn.chain`
- C) `sklearn.tools`
- D) `pandas.pipeline`

**11. Predicting next month's electricity demand (kWh) is…**  _(Multiple choice · Application)_

- A) classification
- B) regression
- C) clustering
- D) reinforcement

**12. Which line trains a classifier correctly?**  _(Multiple choice · Application)_

- A) clf.fit(X_test, y_test)
- B) clf.fit(X_train, y_train)
- C) clf.predict(X_train, y_train)
- D) clf.fit(y_train, X_train)

**13. Confusion matrix [[90, 10], [20, 30]] (rows actual 0/1). Accuracy?**  _(Multiple choice · Application)_

- A) `0.80`
- B) `0.60`
- C) `0.90`
- D) `0.75`

**14. Same matrix: recall for class 1 is…**  _(Multiple choice · Application)_

- A) 30/50 = 0.60
- B) 30/40 = 0.75
- C) 90/100 = 0.90
- D) 30/150 = 0.20

**15. A house-price model has RMSE = 50,000. This means…**  _(Multiple choice · Application)_

- A) predictions are typically off by about $50k
- B) R² = 0.5
- C) 50,000 houses were wrong
- D) the model is perfect

**16. To keep the same class balance in train and test sets, pass…**  _(Multiple choice · Application)_

- A) `shuffle=False`
- B) `stratify=y`
- C) `random_state=0`
- D) `test_size=0.5`

**17. The elbow curve flattens after k = 4. You should try…**  _(Multiple choice · Application)_

- A) k = 1
- B) k = 4
- C) k = 10
- D) the largest k

**18. Features are age (0–100) and income (0–200,000). Before K-Means you should…**  _(Multiple choice · Application)_

- A) drop age
- B) scale both features
- C) one-hot encode income
- D) nothing

**19. Which builds a scaled logistic regression in one object?**  _(Multiple choice · Application)_

- A) Pipeline([('s', StandardScaler()), ('m', LogisticRegression())])
- B) `StandardScaler(LogisticRegression())`
- C) `LogisticRegression(scale=True)`
- D) `Pipeline(LogisticRegression)`

**20. To get the probability that each test passenger survived, use…**  _(Multiple choice · Application)_

- A) clf.predict_proba(X_test)[:, 1]
- B) `clf.predict(X_test)`
- C) `clf.score(X_test)`
- D) `clf.coef_`

**21. A model scores 99% on training data and 70% on test data. Most likely?**  _(Multiple choice · Analysis)_

- A) Underfitting
- B) Overfitting
- C) Data leakage in test
- D) Perfect model

**22. A fraud model has 99.5% accuracy, but only 0.5% of transactions are fraud. What should you check?**  _(Multiple choice · Analysis)_

- A) Nothing, it is great
- B) Recall for the fraud class and the confusion matrix
- C) R²
- D) Inertia

**23. Scaling the whole dataset before train_test_split causes…**  _(Multiple choice · Analysis)_

- A) faster training only
- B) data leakage: test information influences training
- C) better generalisation
- D) no difference ever

**24. Why use logistic rather than linear regression to predict pass/fail?**  _(Multiple choice · Analysis)_

- A) Linear is too slow
- B) Logistic outputs probabilities between 0 and 1 for classes
- C) Logistic needs no data
- D) Linear cannot use two features

**25. K-Means gives 3 clusters, but one contains 95% of customers. Best next step?**  _(Multiple choice · Analysis)_

- A) Ship it
- B) Try scaling features, a different k, and check what each cluster means
- C) Use accuracy to evaluate
- D) Switch to linear regression

---

Answers and feedback are in the instructor answer key. If you are self-studying, ask your facilitator, or use the Google Forms / Moodle version for instant feedback.
