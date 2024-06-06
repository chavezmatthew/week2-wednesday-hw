# 1. Product Review Analysis

# Objective: The aim of this assignment is to extract insights from product reviews by using string manipulation to categorize and summarize customer feedback for a SaaS product.

# Task 1: Keyword Highlighter

# Write a program that searches through a series of product reviews for keywords such as "good", "excellent", "bad", "poor", and "average". Print out each review with the keywords in uppercase so they stand out.


reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "This was a poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]

keywords = ["good", "excellent", "bad", "poor", "average"]



def capitalize_keywords (reviews, keywords):
    capitalized_reviews = []
    for review in reviews:
        for keyword in keywords:
            review = review.replace (keyword, keyword.upper())
        capitalized_reviews.append(review)
    return capitalized_reviews

capitalized_reviews = capitalize_keywords(reviews, keywords)
for review in capitalized_reviews:
    print(review)





# Task 2: Sentiment Tally

# Develop a function that tallies the number of positive and negative words in each review. Use a predefined list of positive and negative words to check against. The function should return the count of positive and negative words for each review.


positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"] 
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]


def tally(reviews, positive_words, negative_words):
    positive_tally = []
    negative_tally = []

    for review in reviews:
        positive_count = 0
        negative_count = 0
        review_lower = review.lower()
        for word in positive_words:
            positive_count += review_lower.count(word)
        positive_tally.append(positive_count)
        for word in negative_words:
            negative_count += review_lower.count(word)
        negative_tally.append(negative_count)

    return positive_tally, negative_tally

positive_tally, negative_tally = tally(reviews, positive_words, negative_words)

for i in range(len(reviews)):
    print(f"Review {i+1}: {positive_tally[i]} positive words, {negative_tally[i]} negative words")



