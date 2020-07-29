import psycopg2
from random import choice

class KkutuGame:
    def __init__(self):
        DB_CONFIG = {
            "database": "main",
            "user": "postgres",
            "password": "password"
        }

        self.conn = psycopg2.connect(**DB_CONFIG)
        self.prev_letter = None
        self.used_word_dict = {}

    def _use_word(self, word):
        #사용자가 컴퓨터가 사용한 단어 기록
        first_letter = word[0]
        if first_letter in self.used_word_dict:
            self.used_word_dict[first_letter] += word
        else:
            self.used_word_dict[first_letter] = [word]

    def _remove_used_word(self, words_list):
        #이전에 사용한 단어들은 선택 불가
        first_letter = words_list[0][0][0]
        try:
            used_dict = dict(map(lambda x: (x, 1), self.used_word_dict[first_letter]))
        except KeyError:
            used_dict = dict()
        
        return [word for word in words_list if word not in used_dict]
    
    def is_valid_word(self, word):
        if word[0] != self.prev_letter and self.prev_letter is not None:
            return '이전 글자와 다름'
        if len(word) < 2:
            return '너무 짧은 단어'

        try:
            if word in self.used_word_dict[word[0]]:
                return '이미 사용됨'
        except KeyError:
            pass

        with self.conn.cursor() as cursor:
            sql = f"select _id from public.kkutu_ko where _id = '{word}'"
            cursor.execute(sql)

            result = cursor.fetchall()

        if not result:
            return '없는 단어'

        self._use_word(word)

        return 'ok'

    def next_word(self, last_letter):
        #다음 단어 검색
        with self.conn.cursor() as cursor:
            sql = f"select _id from public.kkutu_ko where _id like '{last_letter}%' and char_length('_id') >= 2"
            cursor.execute(sql)

            result = cursor.fetchall()
        result = self._remove_used_word(result)
        
        #만약 다음 단어가 없으면 None 반환
        if result is None:
            return None
        
        #단어들 중 하나를 골라서 반환
        word = choice(result)[0]
        self._use_word(word)

        return word

#구현 예시
if __name__ == "__main__":
    game = KkutuGame()

    while True:
        #유저 턴
        word = input('나: ')
        is_ok = game.is_valid_word(word)
        
        #올바른 단어가 아니라면 다시 입력
        while is_ok is not 'ok':
            print(is_ok)
            word = input('나: ')
            is_ok = game.is_valid_word(word)
        
        #컴퓨터 턴
        next_word = game.next_word(word[-1])
        if next_word:
            print(f"컴퓨터: {next_word}")
        #다음 단어가 없다면
        else:
            print('승리!')
            break
