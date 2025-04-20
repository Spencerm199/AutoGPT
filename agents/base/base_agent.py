from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

from pydantic import BaseModel

class AgentConfig(BaseModel):
    """Configuration for an agent."""
    name: str
    description: str
    version: str
    author: str
    license: str
    tags: List[str] = []
    parameters: Dict[str, Any] = {}

class BaseAgent(ABC):
    """Base class for all agents."""
    
    def __init__(self, config: AgentConfig):
        """Initialize the agent with configuration."""
        self.config = config
        self.is_running = False
    
    @abstractmethod
    async def initialize(self) -> bool:
        """Initialize the agent and its resources."""
        pass
    
    @abstractmethod
    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process input data and return results."""
        pass
    
    @abstractmethod
    async def cleanup(self) -> bool:
        """Clean up resources used by the agent."""
        pass
    
    async def start(self) -> bool:
        """Start the agent."""
        if self.is_running:
            return False
        
        success = await self.initialize()
        if success:
            self.is_running = True
        return success
    
    async def stop(self) -> bool:
        """Stop the agent."""
        if not self.is_running:
            return False
        
        success = await self.cleanup()
        if success:
            self.is_running = False
        return success
    
    def get_config(self) -> AgentConfig:
        """Get the agent's configuration."""
        return self.config
    
    def is_active(self) -> bool:
        """Check if the agent is currently running."""
        return self.is_running 