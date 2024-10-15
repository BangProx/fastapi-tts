from fastapi import FastAPI, WebSocket, File, UploadFile, Form
from fastapi.responses import JSONResponse
import asyncio
import json
import os
import uvicorn
import shutil
from externals.tortoise.api_fast import TextToSpeech
from externals.audio_processor import split_text, generate_audio_stream

app = FastAPI()

#tts = TextToSpeech()


@app.post("/audio")
async def upload_audio(user_id: str = Form(...), audio_file: UploadFile = File(...)):
    save_directory = f"tortoise/tortoise/voices/{user_id}"
    os.makedirs(save_directory, exist_ok=True)
    
    file_path = os.path.join(save_directory, audio_file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(audio_file.file, buffer)
    
    return JSONResponse(content={
        "message": f"사용자 {user_id}의 오디오 파일이 성공적으로 업로드되었습니다.",
        "file_name": audio_file.filename,
        "user_id": user_id
    })

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            try:
                data = json.loads(data)
                
                sender_id = data.get('senderId')
                message = data.get('message')
                
                if sender_id is not None:
                    print(f"연결된 사용자: {sender_id}")
                    print(f"메시지: {message}")
                
                if '|' in message:
                    character_name, text = message.split('|', 1)
                else:
                    character_name = str(sender_id)
                    text = message

                text_chunks = split_text(text, max_length=200)
                for chunk in text_chunks:
                    audio_stream = generate_audio_stream(chunk, tts, character_name)

                    for audio_chunk in audio_stream:
                        audio_data = audio_chunk.cpu().numpy().flatten()
                        await websocket.send_bytes(audio_data.tobytes())

                await websocket.send_text("END_OF_AUDIO")
            except json.JSONDecodeError:
                print("잘못된 JSON 형식입니다.")
            except KeyError as e:
                print(f"필수 키가 누락되었습니다: {e}")
    finally:
        print(f"사용자 {sender_id} 연결 해제.")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)