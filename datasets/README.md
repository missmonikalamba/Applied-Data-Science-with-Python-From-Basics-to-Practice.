# Datasets

All datasets used in this course are open and freely redistributable, keeping the course fully OER-compliant. Notebooks load them with a `load_data("file.csv")` helper that reads the local copy, or this repository on GitHub when run in Colab.

| File | Rows | Main use |
|---|---|---|
| [`titanic.csv`](titanic.csv) | 891 | Modules 1, 2, 3, 4, 5 (classification) |
| [`iris.csv`](iris.csv) | 150 | Modules 3, 4, 5 (classification and clustering) |
| [`california_housing.csv`](california_housing.csv) | 20,640 | Modules 3, 4, 5 (regression) |
| [`retail_sales.csv`](retail_sales.csv) | 2,400 | Modules 1, 3, 4, 5 |
| [`retail_sales_raw.csv`](retail_sales_raw.csv) | 2,440 | Module 2 (cleaning) |

The Final Project uses a **learner-selected open dataset** (see [`../final-project/README.md`](../final-project/README.md)).

## `titanic.csv` — Titanic passengers

**Rows × columns:** 891 × 15 · **Used in:** Modules 1, 2, 3, 4, 5 (classification)

**Source and license:** Passenger records from the RMS Titanic (1912). From the seaborn-data repository (github.com/mwaskom/seaborn-data). Historical public records; freely redistributable.

**Notes:** `survived` (0/1) is the classification target. `age` and `deck` have many missing values, which Module 2 uses for practice.

<details><summary>Data dictionary</summary>

| Column | Type | Example | Missing |
|---|---|---|---|
| `survived` | int64 | 0 | 0 |
| `pclass` | int64 | 3 | 0 |
| `sex` | text | male | 0 |
| `age` | float64 | 22.0 | 177 |
| `sibsp` | int64 | 1 | 0 |
| `parch` | int64 | 0 | 0 |
| `fare` | float64 | 7.25 | 0 |
| `embarked` | text | S | 2 |
| `class` | text | Third | 0 |
| `who` | text | man | 0 |
| `adult_male` | bool | True | 0 |
| `deck` | text | C | 688 |
| `embark_town` | text | Southampton | 2 |
| `alive` | text | no | 0 |
| `alone` | bool | False | 0 |

</details>

## `iris.csv` — Iris flowers

**Rows × columns:** 150 × 5 · **Used in:** Modules 3, 4, 5 (classification and clustering)

**Source and license:** Fisher’s Iris data (1936), 150 flowers of three species. From the seaborn-data repository; public domain.

**Notes:** Clean and small: ideal for distributions, ANOVA and K-Means.

<details><summary>Data dictionary</summary>

| Column | Type | Example | Missing |
|---|---|---|---|
| `sepal_length` | float64 | 5.1 | 0 |
| `sepal_width` | float64 | 3.5 | 0 |
| `petal_length` | float64 | 1.4 | 0 |
| `petal_width` | float64 | 0.2 | 0 |
| `species` | text | setosa | 0 |

</details>

## `california_housing.csv` — California housing (1990 census)

**Rows × columns:** 20,640 × 10 · **Used in:** Modules 3, 4, 5 (regression)

**Source and license:** District-level housing data from the 1990 U.S. Census, published by Pace & Barry (1997) via StatLib; this CSV version (with `ocean_proximity` and missing `total_bedrooms`) is the one popularised by the open “handson-ml2” repository. U.S. government census data; public domain.

**Notes:** `median_house_value` is capped at 500,001 and `median_income` is in tens of thousands of dollars. Both quirks are discussed in Modules 3–5.

<details><summary>Data dictionary</summary>

| Column | Type | Example | Missing |
|---|---|---|---|
| `longitude` | float64 | -122.23 | 0 |
| `latitude` | float64 | 37.88 | 0 |
| `housing_median_age` | float64 | 41.0 | 0 |
| `total_rooms` | float64 | 880.0 | 0 |
| `total_bedrooms` | float64 | 129.0 | 207 |
| `population` | float64 | 322.0 | 0 |
| `households` | float64 | 126.0 | 0 |
| `median_income` | float64 | 8.3252 | 0 |
| `median_house_value` | float64 | 452600.0 | 0 |
| `ocean_proximity` | text | NEAR BAY | 0 |

</details>

## `retail_sales.csv` — Retail sales transactions (tidy)

**Rows × columns:** 2,400 × 14 · **Used in:** Modules 1, 3, 4, 5

**Source and license:** Synthetic 2024 transactions for a five-category retailer, generated for this course with a fixed random seed. Released under CC0 (public domain dedication).

**Notes:** Seasonality (Nov–Dec peak) is built in. Ratings are missing for about 12% of rows.

<details><summary>Data dictionary</summary>

| Column | Type | Example | Missing |
|---|---|---|---|
| `transaction_id` | text | T101487 | 0 |
| `date` | text | 2024-01-01 | 0 |
| `store_id` | text | W01 | 0 |
| `region` | text | West | 0 |
| `category` | text | Grocery | 0 |
| `product` | text | Olive Oil | 0 |
| `unit_price` | float64 | 9.31 | 0 |
| `units` | int64 | 1 | 0 |
| `discount` | float64 | 0.2 | 0 |
| `customer_type` | text | Member | 0 |
| `payment_method` | text | Cash | 0 |
| `customer_age` | int64 | 30 | 0 |
| `rating` | float64 | 3.0 | 296 |
| `revenue` | float64 | 7.45 | 0 |

</details>

## `retail_sales_raw.csv` — Retail sales transactions (raw, messy)

**Rows × columns:** 2,440 × 14 · **Used in:** Module 2 (cleaning)

**Source and license:** The same synthetic data with deliberate problems for cleaning practice. CC0.

**Notes:** Contains 40 duplicate rows, mixed date formats (ISO and day/month/year), inconsistent region case, a padded category label, missing values in several columns, impossible ages of 999, and unit-count outliers (60–150).

<details><summary>Data dictionary</summary>

| Column | Type | Example | Missing |
|---|---|---|---|
| `transaction_id` | text | T100038 | 0 |
| `date` | text | 2024-04-11 | 0 |
| `store_id` | text | S01 | 0 |
| `region` | text | South | 73 |
| `category` | text | Grocery | 0 |
| `product` | text | Olive Oil | 0 |
| `unit_price` | float64 | 9.65 | 49 |
| `units` | int64 | 4 | 0 |
| `discount` | float64 | 0.0 | 0 |
| `customer_type` | text | Member | 0 |
| `payment_method` | text | Mobile | 97 |
| `customer_age` | float64 | 37.0 | 147 |
| `rating` | float64 | 3.0 | 302 |
| `revenue` | float64 | 38.6 | 49 |

</details>

## Regenerating the retail data

The retail files were generated with NumPy (seed 42). The generator is described in the instructor guide; any similar synthetic data works for the exercises, but the lab `assert` checks expect these exact files.
