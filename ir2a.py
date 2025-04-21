# AIM : 2A BOOLEAN RETIEVAL MODEL 
# Documents
documents = {
    1: "apple banana orange",
    2: "apple banana",
    3: "banana orange",
    4: "apple"
}


# Function to build an inverted index
def build_index(docs):
    index = {}
    for doc_id, text in docs.items():
        for term in set(text.split()):
            index.setdefault(term, set()).add(doc_id)
    return index


# Boolean AND operation
def boolean_and(operands, index):
    if not operands:
        return list(range(1, len(documents) + 1))
    result = index.get(operands[0], set())
    for term in operands[1:]:
        result &= index.get(term, set())
    return list(result)


# Boolean OR operation
def boolean_or(operands, index):
    result = set()
    for term in operands:
        result |= index.get(term, set())
    return list(result)


# Boolean NOT operation
def boolean_not(operand, index, total_docs):
    all_docs_set = set(range(1, total_docs + 1))
    return list(all_docs_set - index.get(operand, set()))


# Build the inverted index
inverted_index = build_index(documents)


# Example queries
query1 = ["apple", "banana"]  # AND query
query2 = ["apple", "orange"]  # OR query
query3 = "orange"             # NOT query


# Perform queries
result1 = boolean_and(query1, inverted_index)
result2 = boolean_or(query2, inverted_index)
result3 = boolean_not(query3, inverted_index, len(documents))


# Output results
print("Documents containing 'apple' AND 'banana':", result1)
print("Documents containing 'apple' OR 'orange':", result2)
print("Documents NOT containing 'orange':", result3)
print("Performed by The Lost Warrior")
