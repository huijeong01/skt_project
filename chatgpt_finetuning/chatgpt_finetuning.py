import openai
from openai import OpenAI
import os

# OpenAI API 키 설정
openai.api_key = os.getenv('openai_api_key')  # 환경 변수명 확인 필요
client = OpenAI()

# fine tuning 모델 만들기
client.fine_tuning.jobs.create(
  training_file="file-Aqjsshcm1WJgr4lZMKjZ7hvZ",
  validation_file="file-iqZAoKrLWXyGUa5u6JgyP67X",
  model="gpt-3.5-turbo",
  hyperparameters={
    "n_epochs":10  #n_epochs는 50까지만 가능!
  }
)

print('Completed!')
