# Module 2: Data Cleaning and Preprocessing

**Duration:** Weeks 2–3 · **Theory:** 4 hrs · **Practical:** 6 hrs · **Total:** 10 hrs  
**Prerequisites:** Module 1 completed

Raw data is rarely analysis-ready. This module builds a repeatable cleaning pipeline: fixing data types, handling missing values, removing duplicates, taming outliers, and engineering and encoding features for modelling.

## Learning outcomes

By the end of this module, learners will be able to:

- Identify and handle missing data using `dropna()` and `fillna()`
- Detect and filter outliers using Z-scores and the IQR method
- Remove duplicates and replace/rename values in DataFrames
- Create new features through feature engineering techniques
- Encode categorical variables using one-hot and label encoding

## Units

| Unit | Title | Theory | Practical | Checkpoint |
|---|---|---|---|---|
| 2.1 | Introduction to Data Preprocessing | 1 hr | 1.5 hr | [5 MCQs](quizzes/checkpoint-2.1.md) |
| 2.2 | Handling Missing Data | 1 hr | 1.5 hr | [6 MCQs](quizzes/checkpoint-2.2.md) |
| 2.3 | Data Transformation | 1 hr | 1.5 hr | [8 MCQs](quizzes/checkpoint-2.3.md) |
| 2.4 | Feature Engineering | 1 hr | 1.5 hr | [6 MCQs](quizzes/checkpoint-2.4.md) |

### Sub-units

**Unit 2.1 — Introduction to Data Preprocessing**

- 2.1.1 Importance of data preprocessing
- 2.1.2 Understanding data types and formats

**Unit 2.2 — Handling Missing Data**

- 2.2.1 Filtering out missing data
- 2.2.2 Filling in missing data

**Unit 2.3 — Data Transformation**

- 2.3.1 Removing duplicates
- 2.3.2 Replacing values
- 2.3.3 Renaming axis indexes
- 2.3.4 Detecting and filtering outliers

**Unit 2.4 — Feature Engineering**

- 2.4.1 Creating new features
- 2.4.2 Encoding categorical variables

## Materials in this folder

| Assessment layer | File | Format |
|---|---|---|
| Presentation | [`slides/Module02_Data_Cleaning_and_Preprocessing.pptx`](slides/Module02_Data_Cleaning_and_Preprocessing.pptx) | 18 slides (PPTX) |
| Hands-on lab | [`notebooks/Module02_Data_Cleaning_Lab.ipynb`](notebooks/Module02_Data_Cleaning_Lab.ipynb) | Jupyter .ipynb (Colab-ready) |
| Checkpoint quiz | [`quizzes/checkpoint-2.1.md`](quizzes/checkpoint-2.1.md) | 5 MCQs |
| Checkpoint quiz | [`quizzes/checkpoint-2.2.md`](quizzes/checkpoint-2.2.md) | 6 MCQs |
| Checkpoint quiz | [`quizzes/checkpoint-2.3.md`](quizzes/checkpoint-2.3.md) | 8 MCQs |
| Checkpoint quiz | [`quizzes/checkpoint-2.4.md`](quizzes/checkpoint-2.4.md) | 6 MCQs |
| Module quiz | [`quizzes/module-02-quiz.md`](quizzes/module-02-quiz.md) | 25 MCQs, timed 35 min |

Datasets used: [`retail_sales_raw.csv`](../datasets/retail_sales_raw.csv), [`titanic.csv`](../datasets/titanic.csv).

Instructors: the lab answer key, quiz answer keys and LMS import files are in [`instructor/`](../instructor/).

---

© Licensed under [CC BY 4.0](../LICENSE.md).
