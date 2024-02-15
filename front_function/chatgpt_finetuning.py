import openai
import os

# OpenAI API 키 설정
openai.api_key = os.getenv('openai_api_key')

# JSONL 파일 업로드
upload_response = openai.File.create(
  file=open("C:/skt/project/code/skt_project/front_function/finetuningdata.jsonl", "rb"),
  purpose="fine-tune"
)

print(f"Uploaded file ID: {upload_response['id']}")

# Fine-tuning 모델 만들기
training_response = openai.FineTune.create(
  training_file=upload_response['id'],
  model="gpt-3.5-turbo",
  n_epochs=100  # 100 에포크 설정, 필요에 따라 조정 가능
)

print(f"Fine-tuning job ID: {training_response['id']}")

# Fine-tuning 진행 상태 확인
# training_job_id를 위에서 생성된 fine-tuning job의 ID로 설정
training_job_id = training_response['id']
job_status = openai.FineTune.retrieve(training_job_id)

print(f"Job status: {job_status['status']}")
