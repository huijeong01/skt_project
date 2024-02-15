# 괄호, *, & 없는 경우의 dialect form만 남기고 audio 파일을 생성하되 30초 근방에서 잘리고 그에 맞춰 json 파일 생성하기

from pydub import AudioSegment
import json
import os

def filter_and_split_audio(json_path, audio_path, output_directory, segment_length=30000):
    with open(json_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    audio = AudioSegment.from_file(audio_path)

    # 조건을 만족하는 발화와 해당 오디오 세그먼트를 필터링
    filtered_utterances = []
    segments = []
    current_segment = []
    current_length = 0

    for utterance in data['utterance']:
        dialect_form = utterance['dialect_form']
        # 괄호, '&', '*' 중 하나라도 포함되지 않는 발화만 필터링
        if not any(char in dialect_form for char in ['[', ']', '(', ')', '{', '}', '&', '*']):
            start_ms = int(utterance['start'] * 1000)
            end_ms = int(utterance['end'] * 1000)
            segment_duration = end_ms - start_ms

            # 현재 세그먼트 길이 확인 및 30초 근방에서 새 세그먼트 시작
            if current_length + segment_duration > segment_length:
                segments.append((current_segment, current_length))
                current_segment = []
                current_length = 0

            current_segment.append(utterance)
            current_length += segment_duration

    # 마지막 세그먼트 추가
    if current_segment:
        segments.append((current_segment, current_length))

    # 각 세그먼트에 대한 오디오 및 JSON 파일 생성
    for index, (segment_utterances, _) in enumerate(segments, start=1):
        segment_audio = sum(audio[int(u['start'] * 1000):int(u['end'] * 1000)] for u in segment_utterances)
        segment_audio_path = os.path.join(output_directory, f"{os.path.splitext(os.path.basename(json_path))[0]}_segment_{index}.wav")
        segment_audio.export(segment_audio_path, format='wav')

        segment_json_path = os.path.join(output_directory, f"{os.path.splitext(os.path.basename(json_path))[0]}_segment_{index}.json")
        with open(segment_json_path, 'w', encoding='utf-8') as segment_json_file:
            json.dump({
                'id': f"{data['id']}_segment_{index}",
                'metadata': data['metadata'],
                'speaker': data['speaker'],
                'setting': data['setting'],
                'utterance': segment_utterances
            }, segment_json_file, ensure_ascii=False, indent=4)

# 경로 설정
json_directory = 'path/to/json/files'
audio_directory = 'path/to/audio/files'
output_directory = 'path/to/output'
os.makedirs(output_directory, exist_ok=True)

# 파일 처리
for json_file in os.listdir(json_directory):
    if json_file.endswith('.json'):
        json_path = os.path.join(json_directory, json_file)
        audio_path = os.path.join(audio_directory, os.path.splitext(json_file)[0] + '.wav')
        if os.path.exists(audio_path):
            filter_and_split_audio(json_path, audio_path, output_directory)
