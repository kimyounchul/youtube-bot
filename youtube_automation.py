import openai
import os

# OpenAI API 키 설정
API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = API_KEY  # ✅ 최신 방식 적용

def generate_script(recipe_name):
    prompt = f"시바견이 {recipe_name}을 만드는 스토리를 재미있게 써줘."

    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",  # ✅ 최신 모델 적용
        messages=[
            {"role": "system", "content": "너는 유능한 요리사 시바견이야."},
            {"role": "user", "content": prompt}
        ]
    )
    return response["choices"][0]["message"]["content"]

recipe = "오믈렛"
script = generate_script(recipe)
print(script)
