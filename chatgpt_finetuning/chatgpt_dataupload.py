import openai
import os

# OpenAI API 키 설정
openai.api_key = os.getenv('openai_api_key')  # 환경 변수명 확인 필요

# 파일 업로드
response = openai.File.create(
  file=open("C:/skt/project/code/skt_project/front_function/finetuningdata.jsonl", "rb"),
  purpose="fine-tune"
) 

print(f"Uploaded file ID: {response.id}")

