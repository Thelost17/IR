#AIM : use a evaluation toolkit to measure a precison and otherer metrices

from sklearn.metrics import average_precision_score 
# Binary ground truth labels and model scores 
y_true = [0, 1, 1, 0, 1, 1]  # True labels (binary) 
y_scores = [0.1, 0.4, 0.35, 0.8, 0.65, 0.9]  # Predicted scores from the model 
# Calculate and print the average precision-recall score 
avg_precision = average_precision_score(y_true, y_scores) 
print(f'Average Precision-Recall Score: {avg_precision}')
