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

@app.get("/integrations/pos")
async def get_pos_integrations():
    return {
        "integrations": [
            {"name": "NCR", "status": "Connected", "last_sync": "2023-10-27 10:30:00", "type": "POS"},
            {"name": "Revel Systems", "status": "Active", "last_sync": "2023-10-27 10:45:00", "type": "POS"},
            {"name": "Lightspeed", "status": "Online", "last_sync": "2023-10-27 09:15:00", "type": "Retail/POS"},
            {"name": "Square", "status": "Connected", "last_sync": "2023-10-27 11:00:00", "type": "POS/Payment"},
            {"name": "Toast", "status": "Active", "last_sync": "2023-10-27 10:50:00", "type": "Restaurant/POS"},
            {"name": "Shopline", "status": "Connected", "last_sync": "2023-10-27 11:10:00", "type": "E-commerce"}
        ]
    }

@app.get("/integrations/github")
async def get_github_info():
    # In a real app, this would use PyGithub
    return {
        "repositories": [
            {"name": "it-ops-suite", "stars": 125, "forks": 34, "open_issues": 5},
            {"name": "ai-service-api", "stars": 89, "forks": 12, "open_issues": 2}
        ],
        "status": "Connected to GitHub API"
    }

@app.get("/integrations/google")
async def get_google_info():
    # In a real app, this would use google-api-python-client
    return {
        "services": [
            {"name": "Google Drive", "status": "Linked", "storage_used": "1.2 GB"},
            {"name": "Google Calendar", "status": "Synced", "events_today": 4}
        ],
        "status": "Connected to Google Cloud API"
    }

@app.get("/integrations/itsm")
async def get_itsm_integrations():
    return {
        "integrations": [
            {"name": "Jira Service Management", "status": "Active", "last_sync": "2023-10-27 12:00:00", "type": "ITSM"},
            {"name": "Zendesk", "status": "Connected", "last_sync": "2023-10-27 11:45:00", "type": "Help Desk"},
            {"name": "ServiceNow", "status": "Syncing", "last_sync": "2023-10-27 12:15:00", "type": "ITSM/Enterprise"},
            {"name": "Slack IT Workflows", "status": "Active", "last_sync": "2023-10-27 12:30:00", "type": "Collaboration"}
        ]
    }

@app.get("/services/premium")
async def get_premium_services():
    return {
        "services": [
            {
                "id": "ai-opt-01",
                "name": "AI Workflow Optimization",
                "description": "Custom LangChain orchestration tailored for your specific business logic and token efficiency.",
                "price": "$499",
                "period": "one-time",
                "category": "AI Development"
            },
            {
                "id": "sec-audit-01",
                "name": "Managed Security Audit",
                "description": "Comprehensive vulnerability assessment, penetration testing, and compliance report (SOC2/GDPR).",
                "price": "$1,200",
                "period": "per audit",
                "category": "Cybersecurity"
            },
            {
                "id": "infra-auto-01",
                "name": "Cloud Infrastructure Automation",
                "description": "Full Terraform/Ansible setup for multi-cloud environments with auto-scaling and CI/CD.",
                "price": "$250",
                "period": "per month",
                "category": "IT Operations"
            },
            {
                "id": "247-support-01",
                "name": "Elite 24/7 IT Support",
                "description": "Dedicated response team with < 15 minute SLA for critical incidents and proactive monitoring.",
                "price": "$800",
                "period": "per month",
                "category": "IT Support"
            }
        ]
    }

@app.get("/freelance/opportunities")
async def get_freelance_opportunities():
    return {
        "opportunities": [
            {
                "id": "opp-01",
                "title": "React Frontend Developer",
                "description": "Build a responsive dashboard for a fintech client using Tailwind CSS and Chart.js.",
                "budget": "$3,000 - $5,000",
                "duration": "1 month",
                "skills": ["React", "Tailwind", "Chart.js"]
            },
            {
                "id": "opp-02",
                "title": "Python Backend Engineer",
                "description": "Develop FastAPI microservices for an AI-powered document processing platform.",
                "budget": "$50 - $80 / hour",
                "duration": "3 months",
                "skills": ["Python", "FastAPI", "PostgreSQL", "Docker"]
            },
            {
                "id": "opp-03",
                "title": "Cybersecurity Consultant",
                "description": "Perform security audits and penetration testing for a series of web applications.",
                "budget": "$2,500 / audit",
                "duration": "Ongoing",
                "skills": ["Penetration Testing", "OWASP", "Security Auditing"]
            },
            {
                "id": "opp-04",
                "title": "DevOps Architect",
                "description": "Setup CI/CD pipelines and Kubernetes clusters on AWS for a high-traffic e-commerce site.",
                "budget": "$8,000 - $12,000",
                "duration": "2 months",
                "skills": ["AWS", "Kubernetes", "Terraform", "GitHub Actions"]
            }
        ]
    }

@app.get("/freelance/tools")
async def get_freelance_tools():
    return {
        "tools": [
            {
                "name": "Global Time Tracker",
                "description": "Track your billable hours across multiple time zones with automated reporting.",
                "status": "Available",
                "icon": "⏱️"
            },
            {
                "name": "Smart Invoicing",
                "description": "Generate professional invoices and track payments in multiple currencies.",
                "status": "Beta",
                "icon": "📄"
            },
            {
                "name": "Collaboration Hub",
                "description": "Secure workspace for project discussions, file sharing, and code reviews.",
                "status": "Active",
                "icon": "💬"
            },
            {
                "name": "Skill Verification",
                "description": "Get certified in key technologies and showcase your expertise to clients.",
                "status": "Join Waitlist",
                "icon": "✅"
            }
        ]
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
