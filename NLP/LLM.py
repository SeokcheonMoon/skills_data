from transformers import pipeline

# 모델 로드
generator = pipeline('text-generation', model='gpt-2')

# 텍스트 생성
response = generator("이제부터 LLM에 대해 이야기해볼까요?", max_length=50)
print(response)