#whisper sampling data input을 위해 sampling rate change

from pydub import AudioSegment
from pathlib import Path

# 오디오 파일이 저장된 폴더 경로
input_root_folder = 'C:/skt/project/code/skt_project/chatgpt_json/test'

# 변경할 새로운 샘플링 레이트 (Hz 단위)
new_sample_rate = 16000

# 지정된 폴더 안에 있는 모든 오디오 파일 찾기
input_audio_files = list(Path(input_root_folder).rglob('*.mp3'))

# 각 오디오 파일의 샘플링 레이트 변경
for audio_file in input_audio_files:
    # 오디오 파일 로드
    audio = AudioSegment.from_file(audio_file)

    # 새 샘플링 레이트로 오디오 변경
    changed_audio = audio.set_frame_rate(new_sample_rate)

    # 변경된 오디오 파일을 새로운 이름으로 저장 (원본 파일명에 "_modified" 추가)
    new_file_name = audio_file.stem + "_modified" + ".wav"  # 새 파일명 생성
    new_file_path = audio_file.parent / new_file_name  # 새 파일 경로 생성

    # 변경된 오디오 파일 저장
    changed_audio.export(new_file_path, format="wav")
