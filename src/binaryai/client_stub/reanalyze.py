# Generated by ariadne-codegen on 2023-09-18 11:53
# Source: ./src/binaryai/query.graphql

from typing import Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import NoopReason, Status


class Reanalyze(BaseModel):
    reanalyze: "ReanalyzeReanalyze"


class ReanalyzeReanalyze(BaseModel):
    noop_reason: Optional[NoopReason] = Field(alias="noopReason")
    file: "ReanalyzeReanalyzeFile"


class ReanalyzeReanalyzeFile(BaseModel):
    analyze_status: Optional["ReanalyzeReanalyzeFileAnalyzeStatus"] = Field(alias="analyzeStatus")


class ReanalyzeReanalyzeFileAnalyzeStatus(BaseModel):
    status: Status


Reanalyze.model_rebuild()
ReanalyzeReanalyze.model_rebuild()
ReanalyzeReanalyzeFile.model_rebuild()
ReanalyzeReanalyzeFileAnalyzeStatus.model_rebuild()
