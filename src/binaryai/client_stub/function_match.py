# Generated by ariadne-codegen
# Source: ./src/binaryai/query.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class FunctionMatch(BaseModel):
    file: Optional["FunctionMatchFile"]


class FunctionMatchFile(BaseModel):
    decompile_result: Optional["FunctionMatchFileDecompileResult"] = Field(
        alias="decompileResult"
    )


class FunctionMatchFileDecompileResult(BaseModel):
    function: Optional["FunctionMatchFileDecompileResultFunction"]


class FunctionMatchFileDecompileResultFunction(BaseModel):
    match: Optional[List["FunctionMatchFileDecompileResultFunctionMatch"]]


class FunctionMatchFileDecompileResultFunctionMatch(BaseModel):
    score: float
    algorithm: str
    function: "FunctionMatchFileDecompileResultFunctionMatchFunction"


class FunctionMatchFileDecompileResultFunctionMatchFunction(BaseModel):
    code: str


FunctionMatch.model_rebuild()
FunctionMatchFile.model_rebuild()
FunctionMatchFileDecompileResult.model_rebuild()
FunctionMatchFileDecompileResultFunction.model_rebuild()
FunctionMatchFileDecompileResultFunctionMatch.model_rebuild()
