positive_words = ('good', 'excellent', 'super', 'great', 'fantastic')
negative_words = ('bad', 'worse', 'worst', 'pathetic', 'poor')

def analyze_feedback(feedback):
    feedback = feedback.lower()
    for word in positive_words:
        if word in feedback:
            return "Positive Feedback"
    for word in negative_words:
        if word in feedback:
            return "Negative Feedback"
    return "Neutral Feedback"

feedback = input("Enter a feedback sentence: ")
feedback_type = analyze_feedback(feedback)

print("The feedback type is:", feedback_type)
