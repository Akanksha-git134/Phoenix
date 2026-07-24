# Model Training

Six classical machine learning models were trained and compared using TF-IDF features (10,000 max features, unigrams, English stop-words removed). A seventh, calibrated version of the best-performing model was then built for deployment.

Evaluation Metrics:

- Accuracy
- Precision
- Recall
- F1 Score

Precision, Recall, and F1-score were prioritized over raw Accuracy, since the dataset is highly imbalanced (~95% genuine / ~5% fraudulent).

---

## Model 1: Logistic Regression

### Why was this model selected?

- Simple, interpretable baseline for binary text classification.
- Fast to train on high-dimensional TF-IDF features.
- Commonly used as a first benchmark before trying more complex models.

### Objective

Establish a baseline score to compare all subsequent models against.

### Results

- Accuracy: 97.34%
- Precision: 100.00%
- Recall: 45.09%
- F1 Score: 62.15%

### Observation

Despite perfect precision, the model missed more than half of all fraudulent postings (very low recall). On an imbalanced dataset like this, high accuracy alone is misleading — this model is not suitable for deployment on its own.

---

## Model 2: Balanced Logistic Regression

### Why was this model selected?

- Same algorithm as Model 1, but with `class_weight="balanced"` to address class imbalance.
- Tests whether reweighting the minority (fraud) class improves detection without changing the underlying algorithm.

### Objective

Evaluate whether class balancing alone can meaningfully improve recall over plain Logistic Regression.

### Results

- Accuracy: 97.73%
- Precision: 71.10%
- Recall: 89.60%
- F1 Score: 79.28%

### Observation

Balancing dramatically improved recall (45.09% → 89.60%) at the cost of precision (100.00% → 71.10%), i.e., more false alarms. A clear illustration of the precision/recall trade-off that guided the rest of model selection.

---

## Model 3: Multinomial Naive Bayes

### Why was this model selected?

- Common, computationally efficient algorithm for text classification.
- Works efficiently with TF-IDF features.
- Frequently used for spam detection and document classification, a closely related problem.

### Objective

Evaluate whether Naive Bayes can outperform Logistic Regression on fake job detection while maintaining good precision and recall.

### Results

- Accuracy: 96.45%
- Precision: 91.07%
- Recall: 29.48%
- F1 Score: 44.54%

### Observation

Although the model achieved high precision, it failed to detect most fraudulent job postings. Due to its low recall, it is the weakest-performing model overall and is not suitable for the final fake job detection system.

---

## Model 4: Linear Support Vector Machine (Linear SVM)

### Why was this model selected?

- Highly effective for text classification.
- Performs exceptionally well on sparse, high-dimensional TF-IDF vectors.
- Commonly used in spam filtering and document classification.
- Robust to overfitting in text classification problems.

### Objective

Evaluate whether Linear SVM can outperform Logistic Regression while maintaining high recall and precision.

### Results

- Accuracy: 98.60%
- Precision: 98.43%
- Recall: 72.25%
- F1 Score: 83.33%

### Observation

Linear SVM achieved the highest overall accuracy among all models evaluated so far, with excellent precision. However, recall remained moderate — meaning a meaningful share of fraudulent postings were still missed.

---

## Model 5: Balanced Linear SVM

### Why was this model selected?

The dataset is highly imbalanced (95% genuine jobs vs. 5% fraudulent jobs). By assigning higher importance to the minority class (`class_weight="balanced"`), the model is encouraged to detect more fraudulent postings while maintaining strong overall performance.

### Objective

Evaluate whether class balancing can improve recall over the unbalanced Linear SVM without significantly sacrificing precision or accuracy.

### Results

- Accuracy: 98.52%
- Precision: 86.14%
- Recall: 82.66%
- F1 Score: 84.37%

### Observation

Balancing improved recall substantially (72.25% → 82.66%) while giving up some precision (98.43% → 86.14%). This produced the best F1-score among the six compared models, making it the strongest candidate before calibration.

---

## Model 6: Random Forest

### Why was this model selected?

Random Forest is a widely used ensemble learning algorithm that combines multiple decision trees to improve robustness and reduce overfitting. Although it is primarily designed for structured tabular data, it was included to provide a comprehensive comparison against the linear classifiers above.

### Objective

Evaluate how a tree-based ensemble performs on high-dimensional TF-IDF text features and compare its performance against linear classifiers.

### Results

- Accuracy: 98.32%
- Precision: 100.00%
- Recall: 65.32%
- F1 Score: 79.02%

### Observation

Random Forest achieved perfect precision but noticeably weaker recall than both SVM variants, missing a larger share of fraudulent postings. It performed well but did not surpass Balanced Linear SVM overall.

---

## Comparison Summary

| Model | Accuracy | Precision | Recall | F1 Score |
|---|---|---|---|---|
| Logistic Regression | 97.34% | 100.00% | 45.09% | 62.15% |
| Balanced Logistic Regression | 97.73% | 71.10% | 89.60% | 79.28% |
| Multinomial Naive Bayes | 96.45% | 91.07% | 29.48% | 44.54% |
| Linear SVM | 98.60% | 98.43% | 72.25% | 83.33% |
| Balanced Linear SVM | 98.52% | 86.14% | 82.66% | 84.37% |
| Random Forest | 98.32% | 100.00% | 65.32% | 79.02% |

**Balanced Linear SVM** was selected as the best of the six compared models, achieving the highest F1-score while maintaining a strong balance between precision and recall. Although Balanced Logistic Regression achieved a higher recall, it produced significantly more false positives due to lower precision. Linear SVM achieved higher accuracy but missed a larger proportion of fraudulent job postings.

---

## Final Step: Probability Calibration

`LinearSVC` does not natively support `predict_proba()` — it only outputs a raw decision score. Since the web application needs a genuine probability/confidence score (for the risk-level bucketing and confidence label shown to users), the selected Balanced Linear SVM was wrapped in **`CalibratedClassifierCV`**, which calibrates the decision function into reliable class probabilities.

### Final Deployed Model: Balanced Linear SVM (Calibrated)

- Accuracy: **98.66%**
- Precision: **94.96%**
- Recall: **76.30%**
- F1 Score: **84.62%**

### Observation

Calibration shifted the precision/recall balance further toward precision (86.14% → 94.96%) at some cost to recall (82.66% → 76.30%), with F1-score staying essentially unchanged (84.37% → 84.62%). This trade-off was accepted because reliable probability outputs were required for the application's confidence scoring and risk-level system — not to chase a marginally higher F1-score.

### Reason for Final Selection

- Only model providing well-calibrated, reliable confidence scores.
- Highest overall F1-score among all seven models evaluated.
- Strong precision, keeping false alarms low.
- Best-suited for real-world deployment where users see and rely on the confidence percentage shown.

The trained model was saved as:

```
trained_models/fake_job_detector.pkl
```

The TF-IDF vectorizer was saved as:

```
trained_models/tfidf_vectorizer.pkl
```