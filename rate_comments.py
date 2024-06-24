import json
import os
from openai import OpenAI
from dotenv import load_dotenv

# 환경 변수를 불러옵니다.
load_dotenv()

class CommentRater:
    def __init__(self, comment):
        self.comment = comment
        self.api_key = os.getenv("OPENAI_API_KEY")
        with open("prompt.txt", "r") as file:
            self.prompt = file.read()

    def create_score(self):
        client = OpenAI(api_key=self.api_key)

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": self.prompt.replace("{USER_COMMENT}", self.comment)}]
        )

        result = completion.choices[0].message.content
        scores = json.loads(result)
        print(scores)

        score = int(sum(scores.values()))  # 점수 항목의 수로 나눕니다.

        print(score)
        return score

    

    
    