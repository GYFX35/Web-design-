import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import httpx

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

class ForumQuery(BaseModel):
    prompt: str
    context: str = "general"

class ClientSubmission(BaseModel):
    client_name: str
    project_type: str
    description: str
    budget: str
    email: str

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

@app.get("/integrations/un-agencies")
async def get_un_agencies_data():
    agencies = [
        {
            "name": "World Bank",
            "status": "Online",
            "indicator": "Internet Users (% of pop)",
            "last_value": "63.5%",
            "link": "https://data.worldbank.org/indicator/IT.NET.USER.ZS"
        },
        {
            "name": "WHO",
            "status": "Connected",
            "indicator": "National eHealth Strategy",
            "last_value": "Global Priority",
            "link": "https://www.who.int/health-topics/digital-health"
        },
        {
            "name": "UNESCO",
            "status": "Online",
            "indicator": "ICT in Education",
            "last_value": "Global Framework",
            "link": "https://en.unesco.org/themes/ict-education"
        },
        {
            "name": "UNDP",
            "status": "Active",
            "indicator": "Digital Transformation",
            "last_value": "500+ Active Projects",
            "link": "https://open.undp.org"
        }
    ]

    # Try to get live data for World Bank
    async with httpx.AsyncClient() as client:
        try:
            wb_resp = await client.get("https://api.worldbank.org/v2/indicator/IT.NET.USER.ZS?format=json&per_page=1", timeout=5.0)
            if wb_resp.status_code == 200:
                data = wb_resp.json()
                if len(data) > 1 and len(data[1]) > 0:
                    val = data[1][0].get('value')
                    if val:
                        agencies[0]["last_value"] = f"{round(val, 1)}%"
        except Exception:
            pass

        try:
            # Check WHO eHealth indicators
            who_resp = await client.get("https://ghoapi.azureedge.net/api/Indicator?$filter=contains(IndicatorName,'eHealth')", timeout=5.0)
            if who_resp.status_code == 200:
                agencies[1]["status"] = "Online"
        except Exception:
            pass

    return {"agencies": agencies}

@app.get("/global/opportunities")
async def get_global_opportunities():
    programs = []

    # Try to fetch actual projects from World Bank
    async with httpx.AsyncClient() as client:
        try:
            wb_proj_resp = await client.get("https://search.worldbank.org/api/v2/projects?format=json&qterm=digital&rows=5", timeout=5.0)
            if wb_proj_resp.status_code == 200:
                data = wb_proj_resp.json()
                projects = data.get('projects', {})
                for p_id, p_data in projects.items():
                    programs.append({
                        "id": p_id,
                        "organization": "World Bank",
                        "title": p_data.get('project_name', 'Digital Project'),
                        "region": p_data.get('regionname', 'Global'),
                        "focus": p_data.get('lendinginstr', 'Infrastructure'),
                        "budget": f"${p_data.get('totalamt', 'N/A')}",
                        "status": p_data.get('status', 'Active'),
                        "link": p_data.get('url', 'https://projects.worldbank.org')
                    })
        except Exception:
            pass

    # Fallback/Additional hardcoded items if API fails or to provide variety
    if len(programs) < 2:
        programs.extend([
            {
                "id": "who-dh-02",
                "organization": "WHO",
                "title": "Global Initiative on Digital Health",
                "region": "Global",
                "focus": "Health-Tech Standards",
                "budget": "Multi-donor funded",
                "status": "New",
                "link": "https://www.who.int/initiatives/global-initiative-on-digital-health"
            },
            {
                "id": "undp-digi-04",
                "organization": "UNDP",
                "title": "Digital Governance Accelerator",
                "region": "Latin America",
                "focus": "e-Government Services",
                "budget": "$45M",
                "status": "Active",
                "link": "https://open.undp.org"
            }
        ])

    return {"programs": programs}

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

@app.get("/forum/topics")
async def get_forum_topics():
    return {
        "topics": [
            {"id": 1, "title": "Global Tech Partnerships in Africa", "author": "Dr. Aris", "replies": 24, "category": "Partnerships"},
            {"id": 2, "title": "Scaling Open Source for UN SDGs", "author": "OpenTech Lead", "replies": 15, "category": "Global Development"},
            {"id": 3, "title": "Cybersecurity Standards for International Collab", "author": "SecurityExpert", "replies": 42, "category": "Cybersecurity"},
            {"id": 4, "title": "IT Workforce development in SE Asia", "author": "GlobalDev", "replies": 10, "category": "Development"}
        ]
    }

@app.post("/forum/ask")
async def forum_ask(query: ForumQuery):
    try:
        system_prompt = (
            "You are the Global Tech Forum Bot. Your goal is to facilitate discussions between IT professionals, "
            "encourage global tech collaborations, and provide insights into international tech development projects. "
            "Focus on partnerships, digital inclusion, and professional growth in the tech sector."
        )

        full_prompt = f"{system_prompt}\n\nContext: {query.context}\nUser: {query.prompt}"

        # Defaulting to Ollama for the forum bot
        ollama_base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        try:
            llm = ChatOllama(base_url=ollama_base_url, model="llama3")
            response = llm.invoke([HumanMessage(content=full_prompt)])
            return {"response": response.content}
        except Exception:
            # Fallback mock response if Ollama is not available
            return {
                "response": f"I've analyzed your query about '{query.prompt}'. In the context of {query.context}, "
                            f"this is a critical area for global tech collaboration. Many international organizations "
                            f"are looking for partnerships in this space."
            }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/forum/submit")
async def forum_submit(submission: ClientSubmission):
    # In a real app, this would save to a database
    return {
        "status": "success",
        "message": f"Submission received from {submission.client_name}. Our partnership team will review your {submission.project_type} project shortly.",
        "submission_id": "SUB-12345"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
