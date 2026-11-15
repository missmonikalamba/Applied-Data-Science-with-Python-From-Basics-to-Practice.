# Final Project — End-to-End Data Science

**Due:** end of Week 10 · **Weight:** 30% of the final grade (notebook 15% + report 10% + presentation 5%)

The Final Project is the capstone of the course. You choose (or are assigned) an open dataset and complete a small, end-to-end data science project that uses every module.

Slides introducing the project: [`Final_Project_Brief.pptx`](Final_Project_Brief.pptx)

## The task

Choose one of the course datasets (Titanic, Iris, California housing, retail sales) **with a new question**, or another public-domain / openly licensed dataset. Then:

1. **Clean and preprocess** the dataset (Module 2 techniques): data types, missing values, duplicates, outliers, feature engineering and encoding.
2. **Explore and visualize** the data, choosing appropriate chart types and explaining why (Module 3 techniques).
3. **Perform descriptive and inferential statistical analysis**, including **at least one hypothesis test or regression** (Module 4 techniques).
4. **Build and evaluate one supervised or unsupervised machine learning model** (Module 5 techniques), with a train/test split and a baseline for supervised models.

## Deliverables

| Deliverable | Details | Weight | Template |
|---|---|---|---|
| Jupyter notebook | Commented code and markdown explanations of each step; runs top to bottom | 15% | [`project-notebook-template.ipynb`](project-notebook-template.ipynb) |
| Written report | 2–3 pages: problem, method, findings, limitations | 10% | [`report-template.md`](report-template.md) |
| Presentation | 5–8 minutes, slides or recorded walkthrough, for a non-technical audience | 5% | [`presentation-guide.md`](presentation-guide.md) |

Before you start, submit a one-paragraph proposal in Week 8 using [`proposal-template.md`](proposal-template.md).

## How to submit

Create a **public GitHub repository** containing:

```
my-final-project/
├── README.md            # question, dataset source + license, how to run
├── project.ipynb        # your notebook (run it fully before submitting)
├── report.pdf           # or report.md
├── slides.pdf           # or a link to your recording in README.md
└── data/                # the dataset, if its license allows redistribution
```

Submit the repository link through your course platform (Google Classroom, Moodle, etc.).

## Grading

See the full rubric in [`RUBRIC.md`](RUBRIC.md).

## Choosing a dataset

- **License:** public domain, CC0 or CC BY (cite the source).
- **Size and shape:** at least ~500 rows, a mix of numeric and categorical columns, and a column worth predicting or grouping.
- **Sources:** UCI Machine Learning Repository, national open-data portals, the World Bank Open Data catalogue, public-domain Kaggle datasets.

## Academic integrity

You may discuss ideas with classmates and use documentation, but your code, analysis and writing must be your own. If you use AI assistants, say how in your README.

---
© Licensed under [CC BY 4.0](../LICENSE.md).
