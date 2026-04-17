import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="AI Capacity Enhancement Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    prompt: str
    provider: str = "ollama"  # or "google"

@app.get("/")
async def root():
    return {"message": "AI Service is running"}

@app.get("/metrics")
async def get_metrics():
    return {
        "servers": [
            {"host": "prod-db-01", "status": "Online", "cpu": "12%", "memory": "45%", "security": "Secure"},
            {"host": "web-app-primary", "status": "Online", "cpu": "28%", "memory": "62%", "security": "Warning"},
            {"host": "api-gateway-01", "status": "Online", "cpu": "8%", "memory": "32%", "security": "Secure"},
            {"host": "cache-redis-01", "status": "Online", "cpu": "5%", "memory": "20%", "security": "Secure"}
        ],
        "stats": {
            "health": "99.9%",
            "active_projects": 12,
            "open_incidents": 2,
            "security_alerts": 3
        }
    }

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
