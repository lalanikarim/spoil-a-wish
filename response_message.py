import ast
from langchain_core.output_parsers import BaseOutputParser
from pydantic import BaseModel, Field
from typing import List

class Result(BaseModel):
  response: str = Field(..., description="The response content.")

class ResponseMessage(BaseModel):
  success: bool = Field(..., description="Indicates if the operation was successful.")
  errors: List[str] = Field(..., description="A list of errors encountered.")
  messages: List[str] = Field(..., description="A list of informational messages.")
  result: Result = Field(..., description="The result of the operation.")

class CFWAIResponseParser(BaseOutputParser):
    def parse(self, text: str) -> ResponseMessage:
        return ResponseMessage.model_validate(ast.literal_eval(text))