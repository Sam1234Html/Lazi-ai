import re

def detect_direct_answer(text: str) -> bool:
    # TODO: Enhance with ML-based detection
    banned_patterns = [r'\bThe answer is\b', r'\d+$']
    for pattern in banned_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            return True
    return False

def enforce_no_answer(raw: dict) -> dict:
    if detect_direct_answer(str(raw)):
        return {
            "guidance": ["Step 1: Gather facts", "Step 2: Verify"],
            "references": ["Source1"],
            "student_skeleton": {"outline": ["Intro", "Body", "Conclusion"]},
            "warnings": ["Common mistake: Skipping verification"]
        }
    return raw
