# AIXcelerate - Mood Guesser

# Training data
train_data = [
    ("I got full marks in the test today!", "Happy"),
    ("We won the college cricket match", "Happy"),
    ("My friends planned a surprise party for me", "Happy"),
    ("The food in the canteen was really tasty", "Happy"),
    ("I am so excited for the weekend trip", "Happy"),
    ("Our project got selected for the exhibition", "Happy"),
    ("I finally learned how to ride a bicycle", "Happy"),
    ("Mom made my favourite sweets today", "Happy"),
    ("I lost my phone on the bus", "Sad"),
    ("I failed in the mathematics exam", "Sad"),
    ("My best friend is moving to another city", "Sad"),
    ("It rained and our picnic was cancelled", "Sad"),
    ("I missed the last bus and felt very upset", "Sad"),
    ("My laptop stopped working before the submission", "Sad"),
    ("I felt lonely during the long holidays", "Sad")
]


# Level 1: Count Happy and Sad sentences
def count_moods(data):
    happy = 0
    sad = 0

    for sentence, mood in data:
        if mood == "Happy":
            happy += 1
        elif mood == "Sad":
            sad += 1

    return happy, sad


# Level 2: Exactly 8 clue words in each list
happy_words = [
    "won", "marks", "surprise", "tasty",
    "excited", "selected", "favourite", "great"
]

sad_words = [
    "lost", "failed", "moving", "cancelled",
    "missed", "upset", "stopped", "lonely"
]


def guess_mood(sentence):
    # Convert to lowercase and remove punctuation
    cleaned_sentence = ""
    for character in sentence.lower():
        if character.isalnum() or character.isspace():
            cleaned_sentence += character

    words = cleaned_sentence.split()

    happy_count = 0
    sad_count = 0

    for word in words:
        if word in happy_words:
            happy_count += 1
        if word in sad_words:
            sad_count += 1

    # Tie rule: choose Sad because there is no stronger Happy evidence.
    if happy_count > sad_count:
        return "Happy"
    else:
        return "Sad"


# Level 3: Test with the five practice sentences
practice_data = [
    ("I won a medal in the sports meet", "Happy"),
    ("I lost my notebook before the exam", "Sad"),
    ("My friends gave me a lovely surprise", "Happy"),
    ("The train was late and I felt upset", "Sad"),
    ("Today was a great day", "Happy")
]


if __name__ == "__main__":
    print("AIXcelerate Mood Guesser")
    print("-----------------------")

    print("Mood count (Happy, Sad):", count_moods(train_data))
    print()

    correct = 0

    for sentence, actual_mood in practice_data:
        predicted_mood = guess_mood(sentence)
        print("Sentence:", sentence)
        print("Predicted mood:", predicted_mood)
        print("Actual mood:", actual_mood)
        print()

        if predicted_mood == actual_mood:
            correct += 1

    accuracy = (correct / len(practice_data)) * 100
    print("Accuracy:", accuracy, "%")
