import openai
import os

# OpenAI API 키 설정
openai.api_key = os.getenv('openai_api_key')

# 파일 업로드를 위한 파일 경로 설정
file_path = "C:/skt/project/code/skt_project/front_function/finetuningdata.jsonl"

# 파일 업로드
with open(file_path, "rb") as file:
    upload_response = openai.File.create(
        file=file,
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
job_status = openai.FineTune.retrieve(id=training_job_id)

print(f"Job status: {job_status['status']}")
