#重複した問題がランダムで選択されると上手く反映できない。重複を避ける仕様を考える

import re
import random

sourse = 'english_words01.txt'

with open(sourse) as f:
    data = f.read()

english_words = re.findall('[a-z]+', data)
ja = re.findall('\s.*\n', data)

meanings = []
for word in ja:
    m = re.sub('\t|\n', '', word)
    meanings.append(m)

words_dict = dict(zip(english_words, meanings))

n_tests = 5
n_questions = 10

for test_num in range(n_tests):
    with open('英単語テスト_{:02d}.txt'.format(test_num + 1), 'w') as f:
        f.write('出席番号: \n'
                '名前:\n\n'
                '第{}回 英単語テスト\n\n'.format(test_num + 1))

        for question_num in range(n_questions):
            question_word = random.choice(english_words)
            correct_answer = words_dict[question_word]

            meanings_copy = meanings
            meanings_copy.remove(correct_answer)
            wrong_answers = random.sample(meanings_copy, 3)

            answer_options = [correct_answer] + wrong_answers

            random.shuffle(answer_options)

            f.write('問{}. {}\n\n'.format(question_num + 1, question_word))

            for i in range(4):
                f.write('{}. {}\n'.format(i + 1, answer_options[i]))
            f.write('\n\n')
