# Checkpoint 2.2 — Handling Missing Data

6 questions · untimed · covers Unit 2.2. Choose one answer per question.

**1. Which returns True where a value is missing?**  _(Multiple choice)_

- A) `df.notna()`
- B) `df.isna()`
- C) `df.fillna()`
- D) `df.dropna()`

**2. `df.dropna(axis=1)` removes…**  _(Multiple choice)_

- A) rows with any NaN
- B) columns with any NaN
- C) all NaN values in place
- D) duplicate columns

**3. `df.dropna(thresh=5)` keeps rows that have…**  _(Multiple choice)_

- A) at most 5 NaN
- B) at least 5 non-missing values
- C) exactly 5 columns
- D) 5 NaN

**4. The median is less affected by extreme values than the mean.**  _(True/False)_

- A) True
- B) False

**5. Forward fill copies…**  _(Multiple choice)_

- A) the next valid value backwards
- B) the previous valid value forwards
- C) the column mean
- D) zeros

**6. `pd.Series([2, None, 6]).interpolate()` gives…**  _(Multiple choice)_

- A) [2, 2, 6]
- B) [2, 4, 6]
- C) [2, 6, 6]
- D) [2, 0, 6]

---

Answers and feedback are in the instructor answer key. If you are self-studying, ask your facilitator, or use the Google Forms / Moodle version for instant feedback.
