#업로된 파일(이미 전처리가 되어 있는 상태) -> whisper -> chatgpt

from fastapi import FastAPI, HTTPException, UploadFile, File
import httpx
from starlette.responses import JSONResponse
import os
from whisper import load_model

app = FastAPI()

# OpenAI API 설정
OPENAI_API_KEY = os.getenv('openai_api_key')

def generate_prompt(standard_korean: str) -> str:
    prompt_template = f"""
    너는 표준 한국어를 제주도 사투리로 바꾸는 번역기이다. 표준 한국어 문장을 제주도 사투리로 바꿔줘.
    
    표준 한국어: "{standard_korean}"
    제주도 사투리로 번역:
    """
    return prompt_template

async def transcribe_audio(file_path: str):
    print(f"Transcribing file: {file_path}")  # 파일 처리 시작 로깅
    model = load_model("large") # 모델 사이즈에 따라 'base', 'small', 'medium', 'large', 'tiny' 등을 선택
    result = model.transcribe(file_path)
    print(f"Transcription completed for: {file_path}")  # 파일 처리 완료 로깅
    print(f"whisper 추출 text: {result['text']}")
    return result["text"]



@app.post("/translate_audio/")
async def translate_audio(file: UploadFile = File(...)):
    # 파일 저장
    file_location = f"C:/skt/project/code/skt_project/chatgpt_json/fastapi_test/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())

    try:
        # 음성 파일에서 텍스트 추출
        text = await transcribe_audio(file_location)
        # 추출된 텍스트를 제주도 사투리로 번역
        prompt = generate_prompt(text)
        
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": "다음 문장을 제주도 사투리로 번역해."},
                {"role": "user", "content": prompt}
            ]
        }
        #     "messages": [
        #         {"role": "system", "content": "You translate standard Korean to Jeju dialect"},
        #         {"role": "user", "content":f"Translate from Korean to Jeju dialect the following text: {prompt}"},
        #     ]
        # }

        headers = {
            "Authorization": f"Bearer {OPENAI_API_KEY}"
        }

        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post("https://api.openai.com/v1/chat/completions", json=data, headers=headers)
            if response.status_code == 200:
                translation = response.json()['choices'][0]['message']['content']
                return JSONResponse(content={"translation": translation}, status_code=200)
            else:
                return JSONResponse(content={"error": "ChatGPT API 호출에 실패했습니다.", "details": response.text}, status_code=response.status_code)
    except Exception as e:
        error_detail = f"{type(e).__name__}: {e}"
        print(error_detail)  # 콘솔에 에러 출력
        return JSONResponse(content={"error": "서버 내부 오류가 발생했습니다.", "details": error_detail}, status_code=500)

    finally:
        # 임시 파일 삭제
        os.remove(file_location)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

#uvicorn main:app --reload