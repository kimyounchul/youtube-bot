import openai
import os

API_KEY = os.getenv("OPENAI_API_KEY")  # 환경 변수에서 API 키 불러오기

def generate_script(recipe_name):
    prompt = f"시바견이 {recipe_name}을 만드는 스토리를 재미있게 써줘."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

recipe = "오믈렛"
script = generate_script(recipe)
print(script)
