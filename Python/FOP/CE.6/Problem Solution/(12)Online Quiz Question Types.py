class OnlineQuiz:
    def check_answer(self, user_input):
        raise NotImplementedError("Subclasses must override this method")
class MultipleChoice(OnlineQuiz):
    def __init__(self, correct_option):
        self._correct_option = correct_option
    def check_answer(self, user_input):
        return user_input == self._correct_option

class TrueFalse(OnlineQuiz):
    def __init__(self, correct_answer):
        self._correct_answer = correct_answer
    def check_answer(self, user_input):
        return user_input == self._correct_answer

class FillInBlank(OnlineQuiz):
    def __init__(self, correct_word):
        self._correct_word =  correct_word.lower()
    def check_answer(self, user_input):
        return user_input == self._correct_word.lower()
question = [MultipleChoice('B'), TrueFalse('F'), FillInBlank('jepeto')]
answer = ['A', 'T', 'jepeto']  # user answers

for q, a in zip(question, answer):
    print(q.check_answer(a))






