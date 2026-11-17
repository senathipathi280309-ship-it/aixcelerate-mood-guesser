# aixcelerate-mood-guesser
My beginner Python Mood Guesser project for AIXcelerate.
Mood Guesser
A small beginner Python project for the AIXcelerate selection task. It counts Happy and Sad examples and predicts a mood by checking for clue words.
How to run
Download main.py.
Open it with Python 3, or upload it to Google Colab.
Run the program to see the mood count, predictions, and accuracy.
Level 1: Counting moods
The count_moods(data) function counts how many examples are labelled Happy and how many are labelled Sad.
For the supplied training data, it returns (8, 7).
Level 2: Guessing the mood
The guess_mood(sentence) function converts the sentence to lowercase, removes punctuation, and checks its words against two clue-word lists.
My happy_words list has exactly 8 words, and my sad_words list has exactly 8 words, as required by my roll number ending in 8.
If the two counts are tied, the program chooses Sad. I chose this simple tie rule because a tie does not provide stronger Happy evidence. This is only a basic rule-based guesser, so it can make mistakes.
Level 3: Testing
Accuracy on the 5 practice sentences: 100%
All five practice sentences were classified correctly by this version of the program. This result is only for the small practice set; it does not mean the program will always be correct on new sentences.
Which sentence went wrong (or was closest to going wrong), and why?
None of the five practice sentences was classified incorrectly. The sentence “Today was a great day” was a useful check because it depends on the single clue word “great”. If a new sentence used “great” in a different context, the program might still label it Happy without understanding the full meaning.
One change that would make my program better:
I could improve it by handling negation and context. For example, the words in “not happy” should not automatically give the same result as “happy”. I could also test it with more varied sentences.
Learning questions
Total score of “good party today” and its mood:
good has a score of +2, party has +1, and today has 0 because it was not in the example data. Total = +3, so the mood is Happy.
Total score of “bad exam day” and its mood:
bad has -2, exam has 0, and day has -1. Total = -3, so the mood is Sad.
Why did “exam” get a score of 0, and is that good or bad?
“Exam” appears once in a Happy sentence and once in a Sad sentence, so the counts cancel out. This is useful because the word alone does not favour either mood, although it may also mean the word is not helpful for making a prediction.
Why is “not good” labelled Happy by this method, and how could it be fixed?
“Good” has a positive score, while “not” has no score, so the total stays positive. The method does not understand that “not” changes the meaning. One improvement would be to detect negation words such as “not” and adjust the score of the following word.
AI declaration
I used ChatGPT as an AI tool while preparing this project. I asked it to explain the AIXcelerate instructions, help me understand the Python task, and help prepare and review the starter code and this README. I will review the code and make sure I can explain what each function and line does.
Reflection
The hardest part for me was understanding how to turn the task instructions into a working Python program, especially how the clue-word lists and the mood-counting function work. I learned how to use a list, a for loop, counters, functions, and simple word matching. I also learned that a program can get all the practice examples right and still make mistakes on sentences it has not seen.