from pydantic import BaseModel
from typing import List, Dict, Optional

class ConversationRequest(BaseModel):
    user_id: str
    curriculum_level: str
    message: str
    attachments: Optional[List[str]] = []
    context_id: Optional[str] = None

class ConversationResponse(BaseModel):
    guidance: List[str]
    references: List[str]
    student_skeleton: Dict
    warnings: List[str]
    meta: Dict
