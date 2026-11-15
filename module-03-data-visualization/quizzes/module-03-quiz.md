# Module 3 Quiz — Data Visualization with Matplotlib & Seaborn

25 questions · timed, 35 minutes · covers every unit in Module 3.

Difficulty mix: Recall 10 · Application 10 · Analysis 5.

**1. In Matplotlib, the overall canvas is called the…**  _(Multiple choice · Recall)_

- A) Axes
- B) Figure
- C) Plot
- D) Frame

**2. Which function draws vertical bars?**  _(Multiple choice · Recall)_

- A) `plt.barh`
- B) `plt.bar`
- C) `plt.hist`
- D) `plt.col`

**3. Which sets the y-axis label on an Axes object?**  _(Multiple choice · Recall)_

- A) `ax.ylabel()`
- B) `ax.set_ylabel()`
- C) `ax.label_y()`
- D) `ax.y()`

**4. `plt.subplots()` returns a Figure and Axes.**  _(True/False · Recall)_

- A) True
- B) False

**5. Which Seaborn function sets the background style?**  _(Multiple choice · Recall)_

- A) `sns.set_style`
- B) `sns.set_theme_color`
- C) `sns.background`
- D) `sns.style`

**6. Seaborn's `set_context('talk')` mainly changes…**  _(Multiple choice · Recall)_

- A) colours
- B) the scale of fonts and lines
- C) data types
- D) the chart type

**7. Which Matplotlib function draws a violin plot?**  _(Multiple choice · Recall)_

- A) `plt.violinplot`
- B) `plt.violin`
- C) `plt.kde`
- D) `plt.boxplot(violin=True)`

**8. Is Seaborn built on top of Matplotlib?**  _(Yes/No · Recall)_

- A) Yes
- B) No

**9. Which argument sets marker transparency?**  _(Multiple choice · Recall)_

- A) alpha
- B) opacity
- C) transparent
- D) fade

**10. `plt.grid()` adds…**  _(Multiple choice · Recall)_

- A) a legend
- B) grid lines
- C) subplots
- D) a title

**11. You need 3 plots side by side. Which call?**  _(Multiple choice · Application)_

- A) plt.subplots(3, 1)
- B) plt.subplots(1, 3)
- C) `plt.subplot(3)`
- D) `plt.figure(3)`

**12. To compare survival rate (0/1) by passenger class, the clearest Seaborn chart is…**  _(Multiple choice · Application)_

- A) sns.barplot(x='class', y='survived')
- B) `sns.kdeplot(x='survived')`
- C) `sns.heatmap(df)`
- D) `sns.lineplot(x='survived')`

**13. Monthly website visits for 3 years: best chart?**  _(Multiple choice · Application)_

- A) Pie
- B) Line
- C) Box
- D) Scatter

**14. Does advertising spend relate to sales across 200 stores? Best chart?**  _(Multiple choice · Application)_

- A) Scatter
- B) Pie
- C) Count plot
- D) Histogram

**15. Which annotates the max point of series `s` (index = x)?**  _(Multiple choice · Application)_

- A) ax.annotate('max', xy=(s.idxmax(), s.max()))
- B) `ax.text(s.max())`
- C) `ax.title('max')`
- D) `ax.annotate(s)`

**16. Which formats a date axis as 'Jan', 'Feb', …?**  _(Multiple choice · Application)_

- A) `mdates.DateFormatter('%b')`
- B) `mdates.DateFormatter('%Y')`
- C) `ax.dates('month')`
- D) `plt.month()`

**17. Many overlapping scatter points hide density. Quick fix?**  _(Multiple choice · Application)_

- A) Use alpha=0.2 or smaller markers
- B) Use a pie chart
- C) Remove the axis
- D) Use 3D

**18. To colour a Seaborn scatter by 'region', add…**  _(Multiple choice · Application)_

- A) `color='region'`
- B) `hue='region'`
- C) `group='region'`
- D) `by='region'`

**19. Shares of 3 payment methods in total sales: acceptable chart?**  _(Multiple choice · Application)_

- A) Pie chart
- B) Line chart
- C) Heatmap
- D) Histogram

**20. A Seaborn histogram looks blocky and misleading. What should you try?**  _(Multiple choice · Application)_

- A) Change bins
- B) Change hue
- C) Use a pie
- D) Remove labels

**21. A chart's bar axis starts at 95 and makes a 2% difference look like 5×. This is…**  _(Multiple choice · Analysis)_

- A) good practice
- B) a truncated axis that misleads
- C) a log scale
- D) an annotation

**22. Two lines on dual y-axes appear to move together. What should you conclude?**  _(Multiple choice · Analysis)_

- A) They are causally linked
- B) Nothing yet: axis scales were chosen by the designer
- C) They are equal
- D) The data is wrong

**23. A boxplot shows group A with a much wider box than group B. This means…**  _(Multiple choice · Analysis)_

- A) A has more data
- B) A's middle 50% is more spread out
- C) A has a higher mean
- D) A has outliers

**24. Why might a violin plot be preferred over a bar chart of means?**  _(Multiple choice · Analysis)_

- A) It is more colourful
- B) It shows the distribution shape, such as two peaks
- C) It is faster
- D) It needs less data

**25. A heatmap of correlations uses a rainbow colour map from red (−1) to red (+1). The problem?**  _(Multiple choice · Analysis)_

- A) None
- B) Strong positive and negative look alike; use a diverging map
- C) Too few colours
- D) Wrong font

---

Answers and feedback are in the instructor answer key. If you are self-studying, ask your facilitator, or use the Google Forms / Moodle version for instant feedback.
