# Checkpoint 2.4 — Feature Engineering

6 questions · untimed · covers Unit 2.4. Choose one answer per question.

**1. Which creates a 0/1 column for orders over 100?**  _(Multiple choice)_

- A) np.where(df.total > 100, 1, 0)
- B) `df.total.apply(100)`
- C) `pd.get_dummies(100)`
- D) `df.where(100)`

**2. `pd.get_dummies()` performs…**  _(Multiple choice)_

- A) label encoding
- B) one-hot encoding
- C) scaling
- D) imputation

**3. Label encoding can make a linear model think 'Red=2' is twice 'Blue=1'.**  _(True/False)_

- A) True
- B) False

**4. Best encoding for 'Small / Medium / Large'?**  _(Multiple choice)_

- A) One-hot
- B) Ordinal encoding
- C) Drop the column
- D) Z-score

**5. `df['bmi'] = df.weight / df.height ** 2` is an example of…**  _(Multiple choice)_

- A) encoding
- B) an arithmetic feature
- C) imputation
- D) deduplication

**6. Can `apply()` run a custom function on every value of a column?**  _(Yes/No)_

- A) Yes
- B) No

---

Answers and feedback are in the instructor answer key. If you are self-studying, ask your facilitator, or use the Google Forms / Moodle version for instant feedback.
