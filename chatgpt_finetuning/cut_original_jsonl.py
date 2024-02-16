import json

def split_and_save_half(original_file, new_file):
    # 데이터를 저장할 리스트
    data = []
    
    # 원본 파일을 읽어 데이터 저장
    with open(original_file, 'r', encoding='utf-8') as file:
        for line in file:
            data.append(json.loads(line))
    
    # 데이터의 절반을 새로운 파일로 저장
    half_index = len(data) // 3
    with open(new_file, 'w', encoding='utf-8') as file:
        for item in data[:half_index]:
            file.write(json.dumps(item) + '\n')

# 사용 예시
original_file = 'chatgpt_finetuning/originaldata.jsonl' # 원본 파일 이름
new_file = 'chatgpt_finetuning/cutdata2.jsonl' # 새 파일 이름

split_and_save_half(original_file, new_file)
