import os
import uvicorn
from fastapi import FastAPI, HTTPException
from typing import Dict, Any
from dotenv import load_dotenv

from examples.qa_agent import QAAgent
from examples.calculator_agent import CalculatorAgent

# Load environment variables
load_dotenv()

app = FastAPI(title="AutoGPT Agent Server")

# Store active agents
agents: Dict[str, Any] = {
    "qa": QAAgent(),
    "calculator": CalculatorAgent()
}

@app.on_event("startup")
async def startup_event():
    """Initialize agents on startup."""
    for agent_id, agent in agents.items():
        success = await agent.start()
        if not success:
            print(f"Failed to initialize agent: {agent_id}")

@app.on_event("shutdown")
async def shutdown_event():
    """Clean up agents on shutdown."""
    for agent in agents.values():
        await agent.stop()

@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "AutoGPT Agent Server is running"}

@app.get("/agents")
async def list_agents():
    """List all available agents."""
    return {
        agent_id: agent.get_config().dict() 
        for agent_id, agent in agents.items()
    }

@app.post("/agents/{agent_id}/process")
async def process_agent(agent_id: str, input_data: Dict[str, Any]):
    """Process input with specified agent."""
    if agent_id not in agents:
        raise HTTPException(status_code=404, detail="Agent not found")
    
    agent = agents[agent_id]
    if not agent.is_active():
        raise HTTPException(status_code=400, detail="Agent is not running")
    
    result = await agent.process(input_data)
    return result

def main():
    """Run the server."""
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8000"))
    
    uvicorn.run(
        "agents.server:app",
        host=host,
        port=port,
        reload=True if os.getenv("DEBUG", "False").lower() == "true" else False
    )

if __name__ == "__main__":
    main() 