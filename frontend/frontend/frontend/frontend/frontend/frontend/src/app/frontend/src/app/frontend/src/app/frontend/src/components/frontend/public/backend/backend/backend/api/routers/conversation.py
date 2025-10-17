from fastapi import APIRouter, Depends
from schemas import ConversationRequest, ConversationResponse
from services.rag import get_rag_response
from transform.no_answer import enforce_no_answer

router = APIRouter()

@router.post("/", response_model=ConversationResponse)
async def start_conversation(req: ConversationRequest):
    # TODO: Implement context retention with Redis
    raw_response = get_rag_response(req.message, req.curriculum_level)
    transformed = enforce_no_answer(raw_response)
    return ConversationResponse(
        guidance=transformed['guidance'],
        references=transformed['references'],
        student_skeleton=transformed['student_skeleton'],
        warnings=transformed['warnings'],
        meta={'source_confidence': 0.95}
  )
