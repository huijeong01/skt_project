import openai
import os

# OpenAI API 키 설정
openai.api_key = os.getenv('openai_api_key')  # 환경 변수명 확인 필요

# 파일 업로드
openai.files.create(
  file=open("chatgpt_finetuning/training_data1.jsonl", "rb"),
  purpose="fine-tune"
) 

# 파일 업로드
openai.files.create(
  file=open("chatgpt_finetuning/validation_data1.jsonl", "rb"),
  purpose="fine-tune"
) 


