## Model 2: Multinomial Naive Bayes

### Why was this model selected?

- Common algorithm for text classification.
- Works efficiently with TF-IDF features.
- Computationally fast.
- Frequently used for spam detection and document classification.

### Objective

Evaluate whether Naive Bayes can outperform Logistic Regression on fake job detection while maintaining good precision and recall.

## Model 3: Multinomial Naive Bayes

### Why was this model selected?

- Widely used for text classification tasks.
- Fast to train and computationally efficient.
- Serves as a strong baseline for NLP problems.

### Results

- Accuracy: 96.45%
- Precision: 0.91
- Recall: 0.29
- F1 Score: 0.45

### Observation

Although the model achieved high precision, it failed to detect most fraudulent job postings. Due to its low recall, it is not suitable for the final fake job detection system.

## Model 4: Linear Support Vector Machine (Linear SVM)

### Why was this model selected?

- Highly effective for text classification.
- Performs exceptionally well on sparse TF-IDF vectors.
- Commonly used in spam filtering and document classification.
- Strong baseline for NLP problems.

### Objective

Evaluate whether Linear SVM can outperform Logistic Regression while maintaining high recall and precision.

## Model 4: Linear Support Vector Machine (Linear SVM)

### Why was this model selected?

- Performs exceptionally well on high-dimensional sparse TF-IDF vectors.
- Frequently used for document classification and spam detection.
- Robust to overfitting in text classification problems.

### Results

- Accuracy: 98.60%
- Precision: 0.98
- Recall: 0.72
- F1 Score: 0.83

### Observation

Linear SVM achieved the highest overall accuracy and F1 score among all models evaluated. It maintained excellent precision while detecting a significant proportion of fraudulent job postings, making it one of the strongest candidates for deployment.

## Model 5: Balanced Linear SVM

### Why was this model selected?

The dataset is highly imbalanced (95% genuine jobs vs. 5% fraudulent jobs). By assigning higher importance to the minority class, the model is encouraged to detect more fraudulent postings while maintaining strong overall performance.

### Objective

Evaluate whether class balancing can improve recall without significantly sacrificing precision or accuracy.

## Model 6: Random Forest

### Why was this model selected?

Random Forest is a widely used ensemble learning algorithm that combines multiple decision trees to improve robustness and reduce overfitting. Although it is primarily designed for structured tabular data, it was included to provide a comprehensive comparison with other classical machine learning models.

### Objective

Evaluate how a tree-based ensemble performs on high-dimensional TF-IDF text features and compare its performance against linear classifiers.

# Final Model Selection

Balanced Linear SVM was selected as the final deployed model because it achieved the highest F1 Score while maintaining an excellent balance between precision and recall.

Although Balanced Logistic Regression achieved a higher recall, it produced significantly more false positives due to lower precision.
Highest F1 Score while maintaining high Accuracy and strong Precision.

Linear SVM achieved the highest accuracy but missed a larger proportion of fraudulent job postings.

Balanced Linear SVM provided the best trade-off between correctly identifying fraudulent jobs and minimizing false alarms, making it the most suitable model for real-world deployment.

# Model Training

Six machine learning models were trained using TF-IDF features.

Models evaluated:

- Logistic Regression
- Balanced Logistic Regression
- Multinomial Naive Bayes
- Linear Support Vector Machine
- Balanced Linear Support Vector Machine
- Random Forest

Evaluation Metrics:

- Accuracy
- Precision
- Recall
- F1 Score

## Best Model

Balanced Linear Support Vector Machine

Accuracy : 98.52%

Precision : 86.14%

Recall : 82.66%

F1 Score : 84.37%

Reason for Selection:

- Highest F1 Score
- Strong Recall for fraudulent jobs
- Excellent Precision
- Best balance between false positives and false negatives

The trained model was saved as:

trained_models/fake_job_detector.pkl

The TF-IDF vectorizer was saved as:

trained_models/tfidf_vectorizer.pkl