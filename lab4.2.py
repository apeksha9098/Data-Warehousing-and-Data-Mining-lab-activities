import pyfpgrowth

# Creating sample transactions
transactions = [
    ['Milk', 'Bread', 'Saffron'],
    ['Milk', 'Saffron'],
    ['Bread', 'Saffron', 'Wafer'],
    ['Bread', 'Wafer'],
]

# Convert support fraction to absolute count
support_threshold = int(0.5 * len(transactions))

# Call the function properly
FrequentPatterns = pyfpgrowth.find_frequent_patterns(transactions, support_threshold)

print("Frequent Patterns:")
print(FrequentPatterns)

# Generate association rules
Rules = pyfpgrowth.generate_association_rules(FrequentPatterns, 0.5)

print("\nGenerating rules with min confidence threshold = 0.5")
print(Rules)
