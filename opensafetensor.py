import safetensors.torch as st
from pathlib import Path

# .safetensors 파일의 경로
file_path = Path('C:/skt/project/code/skt_project/model.safetensors')
# 파일을 바이너리 모드로 열고 내용을 바이트로 읽음
with file_path.open('rb') as f:
    model_weights = st.load(f.read())

# 로드된 내용 확인
print(model_weights.keys())  # 파일 내에 있는 키들을 확인
