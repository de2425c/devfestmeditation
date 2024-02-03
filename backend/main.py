from fastapi import FastAPI, Response, HTTPException,Request
from fastapi.responses import FileResponse
from api_manager import api_manager
import uvicorn

app = FastAPI()
api_manager = api_manager()

@app.post("/api/generate_text", status_code=200)
async def generate_text(request: Request):
    try:
        data = await request.json()
        if 'prompt' not in data:
            raise HTTPException(status_code=400, detail="Invalid request. Pass in prompt with prompt field.")
        
        prompt = data['prompt']
        return api_manager.generate_text(prompt)
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
        

    
    

@app.post("/api/tts", status_code=200)
async def tts(request: Request):
    try:
        data = await request.json()

        if 'content' not in data:
            raise HTTPException(status_code=400, detail="Invalid request. Pass in content with content field.")
        content = data['content'] 
        output_location = api_manager.tts(content)
        return FileResponse(output_location, media_type='audio/wav')
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)