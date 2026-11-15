# Checkpoint 2.3 — Data Transformation

8 questions · untimed · covers Unit 2.3. Choose one answer per question.

**1. Which method returns a boolean Series marking repeated rows?**  _(Multiple choice)_

- A) `drop_duplicates()`
- B) `duplicated()`
- C) `unique()`
- D) `nunique()`

**2. To deduplicate on the ID column only, pass…**  _(Multiple choice)_

- A) `axis='id'`
- B) `subset=['id']`
- C) `keep='id'`
- D) `on='id'`

**3. `df.replace('N/A', np.nan)` replaces every 'N/A' cell with NaN.**  _(True/False)_

- A) True
- B) False

**4. `s.where(s > 0, 0)` does what?**  _(Multiple choice)_

- A) Keeps positives, sets the rest to 0
- B) Drops negatives
- C) Counts positives
- D) Sets positives to 0

**5. Which renames column 'qty' to 'units'?**  _(Multiple choice)_

- A) df.rename({'qty': 'units'})
- B) df.rename(columns={'qty': 'units'})
- C) `df.columns('units')`
- D) `df.rename_axis('units')`

**6. A Z-score of −3.5 means the value is…**  _(Multiple choice)_

- A) 3.5 units below the mean
- B) 3.5 std devs below the mean
- C) in the bottom 3.5%
- D) an error for sure

**7. With Q1 = 10 and Q3 = 20, the upper IQR fence is…**  _(Multiple choice)_

- A) 25
- B) 30
- C) 35
- D) 40

**8. Should every value outside the IQR fences be deleted automatically?**  _(Yes/No)_

- A) Yes
- B) No

---

Answers and feedback are in the instructor answer key. If you are self-studying, ask your facilitator, or use the Google Forms / Moodle version for instant feedback.
