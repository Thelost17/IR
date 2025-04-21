#AIM : EVALUATION METRICS FOR IR SYSTEM

def calculate_metrics(retrieved_set, relevant_set): 
    # Calculate True Positive, False Positive, and False Negative 
    true_positive = len(retrieved_set.intersection(relevant_set)) 
    false_positive = len(retrieved_set.difference(relevant_set)) 
    false_negative = len(relevant_set.difference(retrieved_set)) 
    
    # Print the metrics 
    print("True Positive:", true_positive) 
    print("False Positive:", false_positive) 
    print("False Negative:", false_negative) 
    
    # Calculate Precision, Recall, and F-measure 
    precision = true_positive / (true_positive + false_positive) 
    recall = true_positive / (true_positive + false_negative) 
    f_measure = 2 * precision * recall / (precision + recall) 
    
    return precision, recall, f_measure 
 
# Example sets 
retrieved_set = {"doc1", "doc2", "doc3"}  # Predicted set 
relevant_set = {"doc1", "doc4"}  # Actually needed set (Relevant) 
 
# Calculate and print Precision, Recall, and F-measure 
precision, recall, f_measure = calculate_metrics(retrieved_set, 
relevant_set) 
print(f"Precision: {precision}") 
print(f"Recall: {recall}") 
print(f"F-measure: {f_measure}")
