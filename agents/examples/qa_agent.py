from typing import Any, Dict
import openai
from ..base.base_agent import BaseAgent, AgentConfig

class QAAgent(BaseAgent):
    """A simple question-answering agent using OpenAI's API."""
    
    def __init__(self):
        """Initialize the QA agent."""
        config = AgentConfig(
            name="QA Agent",
            description="A simple question-answering agent using OpenAI's API",
            version="1.0.0",
            author="AutoGPT",
            license="MIT",
            tags=["qa", "openai", "gpt"],
            parameters={
                "model": "gpt-4",
                "temperature": 0.7,
                "max_tokens": 150
            }
        )
        super().__init__(config)
        self.client = None
    
    async def initialize(self) -> bool:
        """Initialize the OpenAI client."""
        try:
            self.client = openai.OpenAI()
            return True
        except Exception as e:
            print(f"Failed to initialize OpenAI client: {e}")
            return False
    
    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process a question and return the answer."""
        if not self.client:
            return {"error": "Agent not initialized"}
        
        try:
            question = input_data.get("question", "")
            if not question:
                return {"error": "No question provided"}
            
            response = await self.client.chat.completions.create(
                model=self.config.parameters["model"],
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": question}
                ],
                temperature=self.config.parameters["temperature"],
                max_tokens=self.config.parameters["max_tokens"]
            )
            
            return {
                "answer": response.choices[0].message.content,
                "model": self.config.parameters["model"]
            }
            
        except Exception as e:
            return {"error": f"Failed to process question: {str(e)}"}
    
    async def cleanup(self) -> bool:
        """Clean up resources."""
        self.client = None
        return True 