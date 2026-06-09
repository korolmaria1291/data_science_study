# A/B Testing: Analysis of Two Landing Page Variants

## Table of Contents

1. [Statement of the Problem](#1-statement-of-the-problem)
2. [Data Analysis and Preprocessing](#2-data-analysis-and-preprocessing)
3. [Initial Analysis of A/B Testing Results](#3-initial-analysis-of-ab-testing-results)
4. [Metric Stabilization Analysis](#4-metric-stabilization-analysis)
5. [Statistical Analysis of A/B Testing Results](#5-statistical-analysis-of-ab-testing-results)
6. [Final Conclusion](#6-final-conclusion)

---

## 1. Statement of the Problem

### Business Problem

A travel agency plans to launch a new promotional campaign to increase tour sales. Two landing page variants were developed and tested using an A/B experiment.

### Objective

Analyze the effectiveness of both landing page variants using two key business metrics:

- Purchase Conversion Rate
- Average Order Value (AOV)

The goal is to verify that the experiment was conducted correctly, evaluate metric stabilization over time, and determine which landing page variant performs better.

### Tour Packages

- Thailand — 100,000 RUB
- Turkey — 60,000 RUB
- Maldives — 200,000 RUB
- St. Petersburg — 10,000 RUB
- Kamchatka — 150,000 RUB

---

## 2. Data Analysis and Preprocessing

### Dataset Exploration

- Review dataset structure and data types
- Check data quality and consistency

### Experiment Validation

- Verify balanced user distribution between Groups A and B
- Identify users appearing in both experimental groups
- Ensure the correctness of the experiment setup

---

## 3. Initial Analysis of A/B Testing Results

### Business Metrics Analysis

- Calculate conversion rates for both groups
- Calculate Average Order Value (AOV) for both groups
- Compare customer purchasing behavior across available tour packages

### Data Visualization

- Visualize key performance metrics
- Compare the performance of Groups A and B

### Findings

- Summarize initial observations and business insights

---

## 4. Metric Stabilization Analysis

### Daily Metrics Calculation

- Calculate daily conversion rates
- Calculate daily Average Order Value (AOV)

### Cumulative Metrics Analysis

- Compute cumulative conversion rates
- Compute cumulative Average Order Value (AOV)

### Visualization

- Cumulative conversion rate trends by day
- Cumulative AOV trends by day

### Findings

- Evaluate metric stabilization throughout the experiment

---

## 5. Statistical Analysis of A/B Testing Results

### Hypothesis Testing

- Test for statistically significant differences in conversion rates between Groups A and B
- Test for statistically significant differences in Average Order Value (AOV) between Groups A and B

### Confidence Intervals

Construct 95% confidence intervals for:

- Conversion rate in Group A
- Conversion rate in Group B
- Difference in conversion rates between groups
- Average Order Value (AOV) in Group A
- Average Order Value (AOV) in Group B

### Findings

- Interpret statistical test results
- Evaluate practical business significance

---

## 6. Final Conclusion

The A/B test revealed no statistically significant difference in conversion rates between Groups A and B. Confidence intervals overlap, and the statistical test results provide insufficient evidence to reject the null hypothesis.

However, the Average Order Value (AOV) in Group B was statistically significantly higher than in Group A. The confidence intervals do not overlap, and the t-test confirms the observed difference.

Therefore, Landing Page B is recommended for deployment, as it generates significantly higher revenue per user while maintaining a conversion rate comparable to Landing Page A.

---

## Notebook

The complete analysis can be found in the project notebook.

[PROJECT-9 A B Testing.ipynb](https://github.com/korolmaria1291/data_science_study/blob/main/project_9_ab_testing/A%20B%20testing.ipynb)

---

## Dataset

The original dataset used in this project is available in the repository.

[ab_data_tourist.csv](https://github.com/korolmaria1291/data_science_study/blob/main/project_9_ab_testing/ab_data_tourist.csv)

---

## Tools and Technologies

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy

---

## Skills Demonstrated

- A/B Testing
- Statistical Hypothesis Testing
- Confidence Intervals
- Conversion Rate Analysis
- Average Order Value (AOV) Analysis
- Experimental Design Validation
- Business Metrics Evaluation
- Data Visualization
- Data Preprocessing
- Exploratory Data Analysis (EDA)