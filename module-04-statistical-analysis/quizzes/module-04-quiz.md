# Module 4 Quiz — Statistical Analysis with Python

30 questions · timed, 40 minutes · covers every unit in Module 4.

Difficulty mix: Recall 12 · Application 12 · Analysis 6.

**1. Which Pandas method returns the median?**  _(Multiple choice · Recall)_

- A) `df.mid()`
- B) `df.median()`
- C) `df.mean()`
- D) `df.mode()`

**2. Variance measures…**  _(Multiple choice · Recall)_

- A) the centre
- B) average squared distance from the mean
- C) the most common value
- D) skewness

**3. Which Pandas method returns skewness?**  _(Multiple choice · Recall)_

- A) `df.skew()`
- B) `df.kurt()`
- C) `df.std()`
- D) `df.var()`

**4. Kurtosis describes how heavy a distribution's tails are.**  _(True/False · Recall)_

- A) True
- B) False

**5. The Central Limit Theorem is about the distribution of…**  _(Multiple choice · Recall)_

- A) individual values
- B) sample means
- C) outliers
- D) categories

**6. A 95% confidence level corresponds to α =…**  _(Multiple choice · Recall)_

- A) `0.95`
- B) `0.05`
- C) `0.5`
- D) `0.01`

**7. Which correlation method is rank-based?**  _(Multiple choice · Recall)_

- A) Pearson
- B) Spearman
- C) OLS
- D) ANOVA

**8. Failing to reject a false H₀ is a…**  _(Multiple choice · Recall)_

- A) Type I error
- B) Type II error
- C) p-value
- D) confidence interval

**9. Which SciPy function runs a chi-square test of independence?**  _(Multiple choice · Recall)_

- A) `stats.chi2_contingency`
- B) `stats.chisq_ind`
- C) `stats.chi_test`
- D) `stats.f_oneway`

**10. Does `scipy.stats.ttest_ind` compare two independent groups?**  _(Yes/No · Recall)_

- A) Yes
- B) No

**11. In statsmodels, which attribute holds the fitted coefficients?**  _(Multiple choice · Recall)_

- A) `model.coef`
- B) `model.params`
- C) `model.weights`
- D) `model.beta_`

**12. A two-tailed test checks for…**  _(Multiple choice · Recall)_

- A) an increase only
- B) a decrease only
- C) a difference in either direction
- D) no difference

**13. Data: 2, 3, 3, 4, 100. Best single summary of the typical value?**  _(Multiple choice · Application)_

- A) Mean (22.4)
- B) Median (3)
- C) Max
- D) Range

**14. Q1 = 20, Q3 = 50. The IQR is…**  _(Multiple choice · Application)_

- A) 30
- B) 35
- C) 70
- D) 20

**15. A normal variable has mean 100 and sd 15. About 95% of values lie between…**  _(Multiple choice · Application)_

- A) 85 and 115
- B) 70 and 130
- C) 55 and 145
- D) 95 and 105

**16. Which code gives a 95% CI for the mean of sample `s`?**  _(Multiple choice · Application)_

- A) stats.t.interval(0.95, len(s)-1, s.mean(), stats.sem(s))
- B) stats.ttest_1samp(s, 0.95)
- C) s.quantile([0.025, 0.975])
- D) `stats.norm(s)`

**17. You test whether average delivery time differs from 30 minutes. Use…**  _(Multiple choice · Application)_

- A) ttest_1samp(times, 30)
- B) ttest_ind(times, 30)
- C) `chi2_contingency(times)`
- D) `f_oneway(times)`

**18. Comparing average spend across 4 regions: use…**  _(Multiple choice · Application)_

- A) Paired t-test
- B) One-way ANOVA
- C) Chi-square
- D) Pearson r

**19. A test gives p = 0.21 with α = 0.05. The correct conclusion is…**  _(Multiple choice · Application)_

- A) H₀ is true
- B) Reject H₀
- C) Not enough evidence to reject H₀
- D) H₁ is true

**20. Which builds the contingency table for a chi-square test?**  _(Multiple choice · Application)_

- A) pd.crosstab(df.a, df.b)
- B) `df.corr()`
- C) `df.describe()`
- D) `pd.get_dummies(df)`

**21. Which compares Welch's two-sample t-test (unequal variances)?**  _(Multiple choice · Application)_

- A) ttest_ind(a, b, equal_var=False)
- B) ttest_rel(a, b)
- C) ttest_1samp(a, b)
- D) f_oneway(a, b, welch=True)

**22. Model: price = 50,000 + 120 × size_m2. Predicted price for 100 m²?**  _(Multiple choice · Application)_

- A) 62,000
- B) 50,120
- C) 170,000
- D) 12,000

**23. Which line fits OLS with an intercept?**  _(Multiple choice · Application)_

- A) sm.OLS(y, sm.add_constant(X)).fit()
- B) sm.OLS(X, y)
- C) sm.fit(y, X)
- D) `sm.OLS(y).fit(X)`

**24. Pearson r between hours studied and score is 0.62. r² is about…**  _(Multiple choice · Application)_

- A) `0.38`
- B) `0.62`
- C) `0.79`
- D) `0.24`

**25. A drug trial uses α = 0.01 instead of 0.05. The effect is…**  _(Multiple choice · Analysis)_

- A) more Type I errors
- B) fewer Type I errors but more Type II errors
- C) no change
- D) higher power

**26. A city finds ice-cream sales correlate with drownings (r = 0.8). Best explanation?**  _(Multiple choice · Analysis)_

- A) Ice cream causes drowning
- B) A confounder: hot weather drives both
- C) Drowning causes ice-cream sales
- D) The data is fake

**27. A residual plot shows a funnel that widens as fitted values grow. This suggests…**  _(Multiple choice · Analysis)_

- A) a perfect model
- B) non-constant variance (heteroscedasticity)
- C) no relationship
- D) too few variables only

**28. With 1 million rows, a tiny difference of 0.1% gives p < 0.001. What should you report?**  _(Multiple choice · Analysis)_

- A) Only the p-value
- B) The effect size and whether it matters in practice
- C) That the effect is large
- D) Nothing

**29. ANOVA across 3 teaching methods gives p = 0.002. What can you conclude?**  _(Multiple choice · Analysis)_

- A) All three differ
- B) At least one mean differs; post-hoc tests show which
- C) Method A is best
- D) The means are equal

**30. A 95% CI for mean wait time is 12 to 18 minutes. Which statement is correct?**  _(Multiple choice · Analysis)_

- A) 95% of customers wait 12–18 min
- B) The method captures the true mean in 95% of repeated samples
- C) The true mean is 15
- D) There is a 5% chance the data is wrong

---

Answers and feedback are in the instructor answer key. If you are self-studying, ask your facilitator, or use the Google Forms / Moodle version for instant feedback.
