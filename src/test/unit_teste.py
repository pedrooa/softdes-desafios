import unittest
from softdes import lambda_handler

class Test(unittest.TestCase):
    def test_answer(self):
        res = lambda_handler("errado", '')
        self.assertEqual(res, "Função inválida.")


        filename = r'./upload/admin-2020-03-25 193208.py'
        with open(filename,'r') as fp:
            answer = fp.read()
            # print(answer)
        quiz = [1, '2018-08-01', '2020-12-31 23:59:59', 'Exemplo de problema', '[[1],[2],[3]]', '[0, 0, 0]', '["a","b","c"]', 1]
        args = {"ndes": id, "code": answer, "args": eval(quiz[4]), "resp": eval(quiz[5]), "diag": eval(quiz[6]) }
        res = lambda_handler(args, '')
        self.assertEqual(res, "")