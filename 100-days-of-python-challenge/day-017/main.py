from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


def quiz():
    question_bank = []
    for item in question_data:
        new_question = Question(item['text'], item['answer'])
        question_bank.append(new_question)

    quiz_brain = QuizBrain(question_bank)
    while quiz_brain.still_has_questions():
        quiz_brain.next_question()

    quiz_brain.end_game_message()


quiz()
