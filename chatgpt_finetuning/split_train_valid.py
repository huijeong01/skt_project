import json

def split_jsonl_file(original_file, train_file, validation_file, validation_split=0.2):
    # 전체 데이터를 저장할 리스트
    data = []
    
    # 원본 파일을 읽어 데이터 저장
    with open(original_file, 'r', encoding='utf-8') as file:
        for line in file:
            data.append(json.loads(line))
    
    # 데이터를 훈련 및 검증 세트로 분할
    split_index = int(len(data) * (1 - validation_split))
    train_data = data[:split_index]
    validation_data = data[split_index:]
    
    # 훈련 데이터 저장
    with open(train_file, 'w', encoding='utf-8') as file:
        for item in train_data:
            file.write(json.dumps(item) + '\n')
    
    # 검증 데이터 저장
    with open(validation_file, 'w', encoding='utf-8') as file:
        for item in validation_data:
            file.write(json.dumps(item) + '\n')


original_file = 'chatgpt_finetuning/cutdata2.jsonl'
train_file = 'chatgpt_finetuning/training_data2.jsonl'
validation_file = 'chatgpt_finetuning/validation_data2.jsonl'

split_jsonl_file(original_file, train_file, validation_file)
