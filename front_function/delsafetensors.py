import safetensors.torch as st

# .safetensors 파일의 경로
file_path = 'C:/skt/project/code/model.safetensors'
 
with open(file_path, 'rb') as f:
    binary_data = f.read()

# Unusual Line Terminators로 의심되는 바이트 시퀀스를 정의
# 예를 들어, Line Separator (U+2028)는 EF BB BF, Paragraph Separator (U+2029)는 EF BF BD입니다.
# 이 값들은 실제 발견된 바이트와 다를 수 있으며, 실제 바이트 값에 맞춰 변경해야 합니다.
line_separator = b'\xef\xbb\xbf'
paragraph_separator = b'\xef\xbf\xbd'

# 바이트 시퀀스를 제거
binary_data_cleaned = binary_data.replace(line_separator, b'').replace(paragraph_separator, b'')

# 변경된 내용을 새 .safetensors 파일로 저장
with open('C:/skt/project/code/model_cleaned.safetensors', 'wb') as f:
    f.write(binary_data_cleaned)
