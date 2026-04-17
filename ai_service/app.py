import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from langchain.schema import HumanMessage
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="AI Capacity Enhancement Service")

class Query(BaseModel):
    prompt: str
    provider: str = "ollama"  # or "google"

@app.get("/")
async def root():
    return {"message": "AI Service is running"}

@app.post("/ask")
async def ask(query: Query):
    try:
        if query.provider == "google":
            api_key = os.getenv("GOOGLE_API_KEY")
            if not api_key:
                raise HTTPException(status_code=400, detail="Google API Key not configured")
            llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)
            response = llm.invoke([HumanMessage(content=query.prompt)])
            return {"response": response.content}

        elif query.provider == "ollama":
            ollama_base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
            llm = ChatOllama(base_url=ollama_base_url, model="llama3")
            response = llm.invoke([HumanMessage(content=query.prompt)])
            return {"response": response.content}

        else:
            raise HTTPException(status_code=400, detail="Unsupported provider")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
