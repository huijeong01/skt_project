import openai
from openai import OpenAI
import os

# OpenAI API 키 설정
openai.api_key = os.getenv('openai_api_key')  # 환경 변수명 확인 필요
client = OpenAI()

# fine tuning 모델 만들기
client.fine_tuning.jobs.create(
  training_file="file-fILpyHnQVLDsRa6n7HmNab4T",
  model="gpt-3.5-turbo",
  hyperparameters={
    "n_epochs":50  #n_epochs는 50까지만 가능!
  }
)

print('Completed!')
