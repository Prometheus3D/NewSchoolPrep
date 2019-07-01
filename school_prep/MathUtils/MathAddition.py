from random import randint


class Addition:
    def __init__(self, problem_amt, min_num=0, max_num=10):
        self.min_num = min_num
        self.max_num = max_num
        self.problem_amt = problem_amt

    def _get_num(self):
        return randint(self.min_num, self.max_num)

    def generate_addition_problems(self):
        prob_list = []

        while True:
            add_problem = (self._get_num(), self._get_num())
            if add_problem not in prob_list:
                answer = sum(add_problem)
                add_problem = add_problem + (answer,)
                prob_list.append(add_problem)

            if len(prob_list) is self.problem_amt:
                break

        return prob_list
