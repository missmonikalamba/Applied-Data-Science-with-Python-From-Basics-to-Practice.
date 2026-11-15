# Applied Data Science with Python

**An Open Educational Resource (OER) · 10 weeks · 5 modules · 53.5 hours · CC BY 4.0**

A complete, ready-to-teach course that takes learners who already know basic Python (variables, loops, functions, lists) from NumPy and Pandas through data cleaning, visualization and statistics to machine learning with scikit-learn, ending in an end-to-end Final Project.

Designed for facilitated settings (university modules, bootcamps, corporate training) and usable for self-study. Recommended platforms: **GitHub** (code and notebooks) / Jupyter Book, **Google Classroom**, and **Google Colab** (zero install).

## What's inside

| Module | Title | Weeks | Theory (h) | Practical (h) | Slides | Lab notebook | Quizzes |
|---|---|---|---|---|---|---|---|
| 1 | [Foundations of Data Manipulation](module-01-foundations-of-data-manipulation/) | Week 1 | 2 | 3 | [16-slide deck](module-01-foundations-of-data-manipulation/slides/Module01_Foundations_of_Data_Manipulation.pptx) | [Lab](module-01-foundations-of-data-manipulation/notebooks/Module01_NumPy_Pandas_Lab.ipynb) | 3 checkpoints · 20-question quiz |
| 2 | [Data Cleaning and Preprocessing](module-02-data-cleaning-and-preprocessing/) | Weeks 2–3 | 4 | 6 | [18-slide deck](module-02-data-cleaning-and-preprocessing/slides/Module02_Data_Cleaning_and_Preprocessing.pptx) | [Lab](module-02-data-cleaning-and-preprocessing/notebooks/Module02_Data_Cleaning_Lab.ipynb) | 4 checkpoints · 25-question quiz |
| 3 | [Data Visualization with Matplotlib & Seaborn](module-03-data-visualization/) | Weeks 3–5 | 4.5 | 6 | [22-slide deck](module-03-data-visualization/slides/Module03_Data_Visualization.pptx) | [Lab](module-03-data-visualization/notebooks/Module03_Visualization_Gallery_Lab.ipynb) | 3 checkpoints · 25-question quiz |
| 4 | [Statistical Analysis with Python](module-04-statistical-analysis/) | Weeks 5–7 | 6.5 | 9.5 | [22-slide deck](module-04-statistical-analysis/slides/Module04_Statistical_Analysis.pptx) | [Lab](module-04-statistical-analysis/notebooks/Module04_Statistics_Lab.ipynb) | 4 checkpoints · 30-question quiz |
| 5 | [Machine Learning](module-05-machine-learning/) | Weeks 8–10 | 4 | 8 | [20-slide deck](module-05-machine-learning/slides/Module05_Machine_Learning.pptx) | [Lab](module-05-machine-learning/notebooks/Module05_ML_Algorithms_Lab.ipynb) | 4 checkpoints · 25-question quiz |
| — | [Final Project](final-project/) | Week 10 | | | [Brief deck](final-project/Final_Project_Brief.pptx) | [Template](final-project/project-notebook-template.ipynb) | Rubric |
| | **Total** | **10 weeks** | **21** | **32.5** | **98 slides** | **5 labs + 5 answer keys** | **112 checkpoint + 125 module-quiz MCQs** |

Every module folder follows the same layout and the same assessment layers:

1. **Presentation** — one uniform PowerPoint deck per module (intro video placeholder, overview with icons, unit outcomes, code slides with real outputs, inline checkpoint MCQs with answers in the speaker notes, CC BY footer on every slide).
2. **Hands-on lab** — one Jupyter notebook per module: *Learning Objectives → Concept → Guided Practice → Your Turn*, with self-checking `assert` cells, debugging tasks and a mini-project. Tested in a clean Python environment.
3. **Unit checkpoint quizzes** — 5–9 MCQs per unit (MCQ, True/False, Yes/No).
4. **Module quiz** — 20–30 timed MCQs, tagged Recall / Application / Analysis (40/40/20).
5. **Final Project** — capstone notebook + 2–3 page report + 5–8 minute presentation, with a full rubric.

See the [syllabus](SYLLABUS.md) for outcomes, the 10-week schedule and the grading scheme.

## Repository structure

```
applied-data-science-python/
├── README.md                      ← you are here
├── SYLLABUS.md                    ← audience, tools, roadmap, schedule, grading
├── LICENSE.md                     ← CC BY 4.0
├── requirements.txt               ← Python libraries for local use
├── datasets/                      ← all open datasets + data dictionary
├── module-01-foundations-of-data-manipulation/
│   ├── README.md                  ← outcomes, units, materials
│   ├── slides/                    ← PowerPoint deck
│   ├── notebooks/                 ← lab notebook (Colab-ready)
│   └── quizzes/                   ← checkpoint quizzes + module quiz
├── module-02-data-cleaning-and-preprocessing/
├── module-03-data-visualization/
├── module-04-statistical-analysis/
├── module-05-machine-learning/
├── final-project/                 ← brief deck, brief, rubric, templates
├── instructor/                    ← answer keys, quiz keys, LMS import files
└── scripts/set_github_username.py ← one-time setup after you publish
```

## Quick start

**Learners (Google Colab, no install):** open a module's lab notebook on GitHub and click *Open in Colab*. The notebooks load datasets from this repository automatically.

**Learners (local):**
```bash
git clone https://github.com/YOUR-GITHUB-USERNAME/applied-data-science-python.git
cd applied-data-science-python
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

**Instructors:** read [`instructor/README.md`](instructor/README.md) for answer keys, quiz import into Google Forms / Moodle / H5P, and teaching notes.

## Publishing this repository (one-time setup)

1. Create an empty public repository named `applied-data-science-python` on GitHub and upload these files (or `git push`).
2. Replace the placeholder username in all notebooks and READMEs so the Colab badges and dataset links work:
   ```bash
   python scripts/set_github_username.py your-github-username
   ```
   Commit and push the change.
3. **Answer keys:** the `instructor/` folder contains lab solutions and quiz answers. For graded cohorts, move it to a separate **private** repository before publishing.
4. Optional: enable GitHub Pages or build a Jupyter Book from the notebooks.

## 🤖 Virtual Tutor

An AI-powered Virtual Tutor designed to support students in their learning journey through interactive and personalized learning assistance.

Explore the Virtual Tutor using the link below:

<p align="center">
  <a href="https://notebook.google.com/notebook/6fe22ade-ef66-469c-8d1e-5a9d7d13e926?authuser=1">
    <img src="https://img.shields.io/badge/Launch-Virtual%20Tutor-blue?style=for-the-badge&logo=google&logoColor=white" alt="Launch Virtual Tutor"/>
  </a>
</p>

## Requirements

Python 3.11 or 3.12 · NumPy · Pandas · Matplotlib · Seaborn · SciPy · statsmodels · scikit-learn · openpyxl (Excel I/O) · Jupyter or Google Colab · a free GitHub account.

## License

All course materials are released under the [Creative Commons Attribution 4.0 International License (CC BY 4.0)](LICENSE.md). Datasets keep their own open licenses, listed in [`datasets/README.md`](datasets/README.md). Slide icons are from Font Awesome Free (CC BY 4.0).

Suggested attribution: *“Applied Data Science with Python”, Open Educational Resource, licensed under CC BY 4.0.*
