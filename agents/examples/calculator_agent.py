from typing import Any, Dict
import operator
from ..base.base_agent import BaseAgent, AgentConfig

class CalculatorAgent(BaseAgent):
    """A simple calculator agent that performs basic arithmetic operations."""
    
    def __init__(self):
        """Initialize the calculator agent."""
        config = AgentConfig(
            name="Calculator Agent",
            description="A simple calculator agent for basic arithmetic operations",
            version="1.0.0",
            author="AutoGPT",
            license="MIT",
            tags=["calculator", "math", "arithmetic"],
            parameters={
                "supported_operations": ["+", "-", "*", "/", "**"]
            }
        )
        super().__init__(config)
        self.operations = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
            "**": operator.pow
        }
    
    async def initialize(self) -> bool:
        """Initialize the calculator agent."""
        return True
    
    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process arithmetic operation and return result."""
        try:
            # Extract operation and numbers
            operation = input_data.get("operation", "")
            num1 = input_data.get("num1")
            num2 = input_data.get("num2")
            
            # Validate input
            if not operation or operation not in self.operations:
                return {
                    "error": f"Invalid operation. Supported operations: {self.config.parameters['supported_operations']}"
                }
            
            if num1 is None or num2 is None:
                return {"error": "Both numbers are required"}
            
            # Convert to float for calculations
            try:
                num1 = float(num1)
                num2 = float(num2)
            except ValueError:
                return {"error": "Invalid number format"}
            
            # Check for division by zero
            if operation == "/" and num2 == 0:
                return {"error": "Division by zero is not allowed"}
            
            # Perform calculation
            result = self.operations[operation](num1, num2)
            
            return {
                "result": result,
                "operation": operation,
                "num1": num1,
                "num2": num2
            }
            
        except Exception as e:
            return {"error": f"Calculation error: {str(e)}"}
    
    async def cleanup(self) -> bool:
        """Clean up resources."""
        return True 