# Module 2 Quiz — Data Cleaning and Preprocessing

25 questions · timed, 35 minutes · covers every unit in Module 2.

Difficulty mix: Recall 10 · Application 10 · Analysis 5.

**1. Which method counts missing values per column when chained with `sum()`?**  _(Multiple choice · Recall)_

- A) `df.isna()`
- B) `df.count()`
- C) `df.size()`
- D) `df.info()`

**2. What does `fillna(method)`'s modern replacement for forward fill look like?**  _(Multiple choice · Recall)_

- A) `df.ffill()`
- B) `df.forward()`
- C) `df.fill(1)`
- D) `df.pad(0)`

**3. `drop_duplicates()` keeps the first occurrence by default.**  _(True/False · Recall)_

- A) True
- B) False

**4. Which function parses strings into datetimes?**  _(Multiple choice · Recall)_

- A) `pd.to_datetime`
- B) `pd.parse`
- C) `pd.Timestamp.now`
- D) `astype('time')`

**5. The IQR is…**  _(Multiple choice · Recall)_

- A) max − min
- B) Q3 − Q1
- C) mean − median
- D) Q2 − Q1

**6. Which scikit-learn class assigns an integer to each category?**  _(Multiple choice · Recall)_

- A) StandardScaler
- B) LabelEncoder
- C) OneHotScaler
- D) KMeans

**7. Is 'timeliness' a data quality dimension?**  _(Yes/No · Recall)_

- A) Yes
- B) No

**8. Which renames the index axis itself?**  _(Multiple choice · Recall)_

- A) `rename_axis()`
- B) `set_index()`
- C) `reset_index()`
- D) `reindex()`

**9. A common Z-score threshold for outliers is |z| >…**  _(Multiple choice · Recall)_

- A) `0.5`
- B) 1
- C) 3
- D) 10

**10. One-hot encoding creates one new column per category.**  _(True/False · Recall)_

- A) True
- B) False

**11. A sensor log has gaps between ordered readings. Best fill?**  _(Multiple choice · Application)_

- A) Mode
- B) `interpolate()`
- C) Drop the column
- D) Fill with 0

**12. 'payment' has 4% missing values (Card/Cash/Mobile). Sensible fill?**  _(Multiple choice · Application)_

- A) Mean
- B) Mode
- C) Interpolate
- D) 0

**13. Which keeps rows with at least 10 non-null values?**  _(Multiple choice · Application)_

- A) `dropna(how='any')`
- B) `dropna(thresh=10)`
- C) `dropna(axis=10)`
- D) `fillna(10)`

**14. Q1 = 4 and Q3 = 8. Which value lies outside the IQR fences?**  _(Multiple choice · Application)_

- A) 15
- B) 13
- C) 9
- D) −1

**15. Region values include 'north', 'North' and 'NORTH'. Best fix?**  _(Multiple choice · Application)_

- A) `df.region.str.title()`
- B) `drop_duplicates()`
- C) `get_dummies()`
- D) `dropna()`

**16. Ages include 999 as a code for 'unknown'. First step?**  _(Multiple choice · Application)_

- A) Keep it
- B) Replace 999 with NaN
- C) Take the mean
- D) One-hot encode it

**17. Which creates `is_child` = 1 when age < 12?**  _(Multiple choice · Application)_

- A) np.where(df.age < 12, 1, 0)
- B) `df.age.where(12)`
- C) df.replace(12, 1)
- D) `pd.cut(12)`

**18. `pd.get_dummies(df['color'])` on Red/Green/Blue returns how many columns?**  _(Multiple choice · Application)_

- A) 1
- B) 2
- C) 3
- D) 4

**19. Which turns 'Low/Med/High' into 0/1/2 in that order?**  _(Multiple choice · Application)_

- A) `LabelEncoder()`
- B) df.map({'Low': 0, 'Med': 1, 'High': 2})
- C) `get_dummies()`
- D) `astype(int)`

**20. You want one row per customer_id, keeping the latest. Use…**  _(Multiple choice · Application)_

- A) drop_duplicates(subset='customer_id', keep='last') after sorting by date
- B) `dropna()`
- C) `duplicated()`
- D) `rename()`

**21. Filling income with the mean in a heavily right-skewed dataset will tend to…**  _(Multiple choice · Analysis)_

- A) Underestimate typical income
- B) Overestimate typical income
- C) Have no effect
- D) Remove outliers

**22. After dropna(), a dataset shrinks from 10,000 to 3,000 rows. Best next step?**  _(Multiple choice · Analysis)_

- A) Accept it
- B) Check which columns cause it and fill or drop those columns instead
- C) Drop more rows
- D) Encode everything

**23. Why is label encoding risky for a 'city' feature in linear regression?**  _(Multiple choice · Analysis)_

- A) It is slow
- B) It imposes a fake order and spacing between cities
- C) It creates too many columns
- D) It removes NaN

**24. IQR flags 5% of 'units' as outliers, but they are genuine bulk orders. Best action?**  _(Multiple choice · Analysis)_

- A) Delete them
- B) Keep them and note it, or analyse separately
- C) Replace with mean
- D) Set to 0

**25. Which order of steps is most sensible?**  _(Multiple choice · Analysis)_

- A) Encode → fix types → fill missing
- B) Fix types → handle missing/duplicates → outliers → features/encoding
- C) Outliers → load → encode
- D) Features → load → clean

---

Answers and feedback are in the instructor answer key. If you are self-studying, ask your facilitator, or use the Google Forms / Moodle version for instant feedback.
