# Syllabus — Applied Data Science with Python

*Open Educational Resource (OER) · 2-month (10-week) curriculum with assessment framework*

## Target audience and context of use

This course is designed primarily for use within a facilitated setting — a university module, bootcamp, or corporate training program — where an instructor reviews the Final Project and provides feedback. The self-paced materials (video-ready slides, notebooks, and checkpoint quizzes) also support independent self-study, but the Final Project rubric assumes some form of feedback loop.

**Recommended for:**
- Beginner-to-intermediate Python users who already know variables, loops, functions, and lists
- Undergraduate or postgraduate students in computer science, data science, economics, engineering, or business analytics
- Professionals reskilling into data analytics or data science roles

## Recommended platforms
- GitHub (code and notebooks) | Jupyter Book
- Google Classroom
- Google Colaboratory

## Required tools and environment
- Python 3.11 or 3.12
- Jupyter Notebook / JupyterLab (local) or Google Colab (recommended — browser-based, zero install)
- Core libraries: NumPy, Pandas, Matplotlib, Seaborn, SciPy, statsmodels, scikit-learn
- A free GitHub account, for accessing lab notebooks and submitting the Final Project repository

## Datasets
All datasets are open and freely redistributable (details and licenses in [`datasets/README.md`](datasets/README.md)):
- Titanic passenger dataset — classification practice (Modules 2, 5)
- Iris dataset — classification and clustering practice (Modules 4, 5)
- California housing dataset — regression practice (Modules 4, 5)
- Retail/sales transactions dataset — exploratory analysis and visualization practice (Modules 2, 3)
- Learner-selected open dataset — used for the Final Project

## Course overview: 10-week roadmap

| Module | Name | Theory (hrs) | Practical (hrs) | Month | Weeks |
|---|---|---|---|---|---|
| 1 | Foundations of Data Manipulation | 2 | 3 | Month 1 | Week 1 |
| 2 | Data Cleaning and Preprocessing | 4 | 6 | Month 1 | Weeks 2–3 |
| 3 | Data Visualization with Matplotlib & Seaborn | 4.5 | 6 | Month 1 | Weeks 3–5 |
| 4 | Statistical Analysis with Python | 6.5 | 9.5 | Month 2 | Weeks 5–7 |
| 5 | Machine Learning | 4 | 8 | Month 2 | Weeks 8–10 |
| **Total** | **5 Modules** | **21 hrs** | **32.5 hrs** | | **10 Weeks · 53.5 total hrs** |

**Month 1 — Foundations & Core Data Skills:** NumPy arrays, Pandas wrangling, cleaning messy datasets, and compelling visualizations, including how to choose the right chart for the data.

**Month 2 — Statistical Analysis & Machine Learning:** descriptive and inferential statistics, hypothesis testing and regression, then supervised and unsupervised machine learning with extra practice time.

## Module learning outcomes

### Module 1: Foundations of Data Manipulation
*Week 1 · Theory 2 h · Practical 3 h · Prerequisites: Basic Python programming (variables, loops, functions, lists)*

- Create and manipulate NumPy arrays using core functions
- Perform arithmetic, aggregation, and comparison operations on arrays
- Use indexing, slicing, boolean indexing, and fancy indexing
- Import, explore, and manipulate data using Pandas Series and DataFrames
- Read and write data in CSV, Excel, and JSON formats

### Module 2: Data Cleaning and Preprocessing
*Weeks 2–3 · Theory 4 h · Practical 6 h · Prerequisites: Module 1 completed*

- Identify and handle missing data using dropna() and fillna()
- Detect and filter outliers using Z-scores and the IQR method
- Remove duplicates and replace/rename values in DataFrames
- Create new features through feature engineering techniques
- Encode categorical variables using one-hot and label encoding

### Module 3: Data Visualization with Matplotlib & Seaborn
*Weeks 3–5 · Theory 4.5 h · Practical 6 h · Prerequisites: Modules 1 & 2 completed*

- Create and customize line, bar, scatter, pie, box, and violin plots using Matplotlib
- Build subplots and annotate visualizations effectively
- Plot time series data with proper date formatting
- Use Seaborn for statistical and aesthetic visualizations
- Choose the appropriate chart type for different data scenarios, and explain why

### Module 4: Statistical Analysis with Python
*Weeks 5–7 · Theory 6.5 h · Practical 9.5 h · Prerequisites: Modules 1–3 completed*

- Calculate and interpret measures of central tendency and variability
- Understand and apply probability distributions
- Perform hypothesis testing with t-tests, chi-square, and ANOVA
- Calculate and interpret correlation and regression coefficients
- Use SciPy and StatsModels for statistical computation

### Module 5: Machine Learning
*Weeks 8–10 · Theory 4 h · Practical 8 h · Prerequisites: Modules 1–4 completed*

- Define machine learning and describe its types and applications
- Build and evaluate a supervised learning model (classification and regression)
- Apply clustering as an unsupervised learning technique
- Implement Linear Regression and Logistic Regression using scikit-learn
- Evaluate models using appropriate metrics (accuracy, RMSE, confusion matrix)

## 10-week schedule at a glance

| Week | Module / Unit | Theory (hrs) | Practical (hrs) | Assessment |
|---|---|---|---|---|
| 1 | Module 1: All 3 Units (NumPy, Pandas, I/O) | 2 | 3 | 3 Checkpoints + Module Quiz 1 |
| 2 | Module 2: Units 2.1, 2.2 (Preprocessing, Missing Data) | 2 | 3 | 2 Checkpoints |
| 3 | Module 2: Units 2.3, 2.4 + Module 3: Unit 3.1 | 3 | 4.5 | 3 Checkpoints + Module Quiz 2 |
| 4 | Module 3: Units 3.2 (incl. chart selection), 3.3 | 2 | 3 | 1 Checkpoint (3.2; Unit 3.3 is assessed in Checkpoint 3.4) |
| 5 | Module 3: Unit 3.4 + Module 4: Unit 4.1 | 3.5 | 4.5 | 2 Checkpoints + Module Quiz 3 |
| 6 | Module 4: Unit 4.2 (Inferential Statistics) | 2 | 3 | 1 Checkpoint |
| 7 | Module 4: Units 4.3, 4.4 (Hypothesis Testing, Regression) | 2.5 | 3.5 | 2 Checkpoints + Module Quiz 4 |
| 8 | Module 5: Units 5.1, 5.2 (ML Intro + Supervised) | 2.5 | 4 | 2 Checkpoints · Final Project proposal |
| 9 | Module 5: Unit 5.3 (Unsupervised) + guided practice | 1 | 2.5 | 1 Checkpoint |
| 10 | Module 5: Unit 5.4 + Final Project work & submission | 0.5 | 1.5 | 1 Checkpoint + Module Quiz 5 + Final Project |
| **Total** | **10 Weeks** | **21** | **32.5** | **5 Module Quizzes + Final Project** |

## Assessment framework

Every module includes the same assessment layers. All materials are open-licensed and platform-agnostic.

| Layer | What | Where |
|---|---|---|
| 1. Presentation | One deck per module (16–22 slides): video placeholder, overview with icons, unit outcomes, code slides, inline checkpoint MCQs, CC BY footer | `module-*/slides/` |
| 2. Hands-on lab | One notebook per module: Learning Objectives → Concept → Guided Practice → Your Turn; fill-in-the-blank, debugging, mini-project; answer keys for instructors | `module-*/notebooks/`, `instructor/answer-keys/` |
| 3. Unit checkpoint quiz | 5–9 MCQs per unit (MCQ, True/False, Yes/No), immediate feedback when hosted on Google Forms, H5P or Moodle | `module-*/quizzes/checkpoint-*.md` |
| 4. Module quiz | 20–30 MCQs, timed 30–40 minutes, Recall 40% / Application 40% / Analysis 20% | `module-*/quizzes/module-*-quiz.md` |
| 5. Final Project | Capstone in Week 10: notebook + 2–3 page report + 5–8 minute presentation | `final-project/` |

### Quiz inventory

| Module | Checkpoints (MCQs per unit) | Module quiz | Time limit |
|---|---|---|---|
| 1 | 1.1: 6, 1.2: 6, 1.3: 5 | 20 MCQs | 30 min |
| 2 | 2.1: 5, 2.2: 6, 2.3: 8, 2.4: 6 | 25 MCQs | 35 min |
| 3 | 3.1: 6, 3.2: 9, 3.4: 8 | 25 MCQs | 35 min |
| 4 | 4.1: 6, 4.2: 7, 4.3: 6, 4.4: 5 | 30 MCQs | 40 min |
| 5 | 5.1: 6, 5.2: 7, 5.3: 5, 5.4: 5 | 25 MCQs | 35 min |

Unit 3.3 (Introduction to Seaborn) has no separate checkpoint in the course design; its content is assessed in Checkpoint 3.4 and the Module 3 quiz.

## Grading scheme

| Component | Weight | Notes |
|---|---|---|
| Unit Checkpoint Quizzes | 20% | All units combined |
| Module Quizzes | 25% | 5 quizzes across the course |
| Hands-On Lab Notebooks | 25% | One per module, 5 total |
| Final Project | 30% | Notebook 15% + report 10% + presentation 5% |
| **Total** | **100%** | |

Suggested lab grading: completion of all *Your Turn* exercises with passing checks (60%), mini-project quality (30%), code readability (10%).

---
© Licensed under [CC BY 4.0](LICENSE.md).
