# Module 1 Quiz — Foundations of Data Manipulation

20 questions · timed, 30 minutes · covers every unit in Module 1.

Difficulty mix: Recall 8 · Application 8 · Analysis 4.

**1. NumPy's core data structure is the…**  _(Multiple choice · Recall)_

- A) DataFrame
- B) ndarray
- C) Series
- D) list

**2. Which function creates an array filled with zeros?**  _(Multiple choice · Recall)_

- A) `np.empty`
- B) `np.zeros`
- C) `np.null`
- D) `np.blank`

**3. Which attribute returns the total number of elements?**  _(Multiple choice · Recall)_

- A) shape
- B) ndim
- C) size
- D) len

**4. `arr.T` returns the transpose of a 2D array.**  _(True/False · Recall)_

- A) True
- B) False

**5. A DataFrame's `describe()` method returns…**  _(Multiple choice · Recall)_

- A) column dtypes
- B) summary statistics
- C) the first rows
- D) missing values only

**6. Which writes a DataFrame to JSON?**  _(Multiple choice · Recall)_

- A) `df.to_json()`
- B) `df.write_json()`
- C) `pd.to_json(df)`
- D) `df.save('json')`

**7. Is Pandas built on top of NumPy?**  _(Yes/No · Recall)_

- A) Yes
- B) No

**8. `pd.read_csv(f, index_col='id')` does what with 'id'?**  _(Multiple choice · Recall)_

- A) Drops it
- B) Uses it as the row index
- C) Sorts by it
- D) Renames it

**9. What does `np.arange(12).reshape(3, 4)[1]` return?**  _(Multiple choice · Application)_

- A) [1, 5, 9]
- B) [4, 5, 6, 7]
- C) [0, 1, 2, 3]
- D) 4

**10. `a = np.array([1, 2, 3])`. What is `a * a`?**  _(Multiple choice · Application)_

- A) [1, 4, 9]
- B) 14
- C) [2, 4, 6]
- D) Error

**11. `m = np.array([[1, 2], [3, 4]])`. What is `m.mean(axis=1)`?**  _(Multiple choice · Application)_

- A) [2., 3.]
- B) [1.5, 3.5]
- C) `2.5`
- D) [4., 6.]

**12. `v = np.array([10, 20, 30, 40, 50])`. What is `v[::-2]`?**  _(Multiple choice · Application)_

- A) [50, 30, 10]
- B) [10, 30, 50]
- C) [40, 20]
- D) [50, 40]

**13. Which keeps Titanic rows for first-class women?**  _(Multiple choice · Application)_

- A) df[df.pclass == 1 and df.sex == 'female']
- B) df[(df.pclass == 1) & (df.sex == 'female')]
- C) df[df.pclass == 1 & df.sex == 'female']
- D) df.loc[1, 'female']

**14. You need only the first 1,000 rows of a huge CSV. Use…**  _(Multiple choice · Application)_

- A) `usecols=1000`
- B) `nrows=1000`
- C) `head=1000`
- D) `skiprows=1000`

**15. `s = pd.Series([5, 6], index=['x', 'y'])`. What is `s['y']`?**  _(Multiple choice · Application)_

- A) 5
- B) 6
- C) 'y'
- D) KeyError

**16. Which creates a new column 'total' = price × qty?**  _(Multiple choice · Application)_

- A) df.total = price * qty
- B) df['total'] = df['price'] * df['qty']
- C) `df.add('total')`
- D) df['price' * 'qty']

**17. `a` is (4, 3) and `b` is (4,). Why does `a + b` fail?**  _(Multiple choice · Analysis)_

- A) dtypes differ
- B) Trailing dimensions 3 and 4 do not match
- C) b is 1D
- D) Addition needs equal sizes always

**18. A colleague's CSV reloads with an extra 'Unnamed: 0' column. Most likely cause?**  _(Multiple choice · Analysis)_

- A) Wrong encoding
- B) It was saved without index=False
- C) sep was wrong
- D) nrows was set

**19. `s1 = pd.Series({'a': 1, 'b': 2})`, `s2 = pd.Series({'b': 10, 'c': 20})`. What is `(s1 + s2)['a']`?**  _(Multiple choice · Analysis)_

- A) 1
- B) NaN
- C) 11
- D) Error

**20. Which is the best reason to vectorise rather than loop over a NumPy array?**  _(Multiple choice · Analysis)_

- A) Loops are not allowed
- B) Vectorised code runs in compiled C and is much faster
- C) It uses more memory
- D) It changes the dtype

---

