# Generated by ariadne-codegen on 2023-09-18 11:53
# Source: ./src/binaryai/query.graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class FunctionInfo(BaseModel):
    file: Optional["FunctionInfoFile"]


class FunctionInfoFile(BaseModel):
    decompile_result: Optional["FunctionInfoFileDecompileResult"] = Field(alias="decompileResult")


class FunctionInfoFileDecompileResult(BaseModel):
    function: Optional["FunctionInfoFileDecompileResultFunction"]


class FunctionInfoFileDecompileResultFunction(BaseModel):
    offset: Any
    name: str
    embedding: Optional["FunctionInfoFileDecompileResultFunctionEmbedding"]
    pseudo_code: Optional["FunctionInfoFileDecompileResultFunctionPseudoCode"] = Field(alias="pseudoCode")


class FunctionInfoFileDecompileResultFunctionEmbedding(BaseModel):
    vector: List[float]
    version: str


class FunctionInfoFileDecompileResultFunctionPseudoCode(BaseModel):
    code: str


FunctionInfo.model_rebuild()
FunctionInfoFile.model_rebuild()
FunctionInfoFileDecompileResult.model_rebuild()
FunctionInfoFileDecompileResultFunction.model_rebuild()
FunctionInfoFileDecompileResultFunctionEmbedding.model_rebuild()
FunctionInfoFileDecompileResultFunctionPseudoCode.model_rebuild()
