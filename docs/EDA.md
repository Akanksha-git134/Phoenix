## Dataset Overview

- 17,880 job postings
- 18 features
- Target variable: fraudulent
- 13 object columns
- 5 integer columns

## Initial Observations

- description has only one missing value.
- salary_range has approximately 84% missing values.
- company_profile is available for most records.
- Binary features such as has_company_logo and has_questions may provide useful signals.
- job_id appears to be an identifier and is unlikely to be useful for prediction.

## Missing Value Analysis

### Key Findings

- salary_range has the highest missing percentage (83.96%).
- department has 64.58% missing values.
- description is nearly complete (only one missing value).
- Several categorical features contain moderate missing values but may still contribute useful information.

### Initial Decision

No features will be dropped during the EDA phase. Feature selection decisions will be made after evaluating their predictive importance.

## Target Variable Analysis

### Distribution

- Real job postings: 17,014 (95.16%)
- Fraudulent job postings: 866 (4.84%)

### Observation

The dataset is highly imbalanced. A model predicting only legitimate jobs would achieve over 95% accuracy while failing to identify fraudulent postings.

### Decision

Evaluation will prioritize Precision, Recall, F1-score, and ROC-AUC. Class balancing techniques such as class weights and SMOTE will be investigated during model development.

## Duplicate Analysis

### Findings

- No completely duplicated rows were found.
- 3,078 duplicate job descriptions exist, which may represent multiple postings of similar positions rather than duplicated records.
- 6,649 duplicate job titles were observed, which is expected because common job titles are frequently reused.

### Decision

No records will be removed during the EDA phase. Duplicate text fields will be evaluated in the context of feature engineering rather than treated as duplicate observations.

## Text Feature Analysis

### Average Length

- Description: ~1218 characters
- Company Profile: ~762 characters
- Requirements: ~695 characters
- Benefits: ~350 characters
- Title: ~29 characters

### Observations

- The job description contains the richest textual information.
- Company profile and requirements are also substantial and may improve prediction.
- The title is short but provides useful context.
- Multiple text fields may be combined during feature engineering.

## Categorical Feature Analysis

### Employment Type

- Full-time jobs dominate the dataset.
- Contract and Part-time positions are less common.

### Required Experience

- Mid-Senior level is the most frequent category.
- Entry-level and Associate positions are also common.

### Required Education

- Bachelor's Degree is the most common educational requirement.
- Master's Degree and High School follow.

### Initial Observation

The distributions appear realistic. The relationship between these categories and fraudulent postings will be investigated during feature analysis.