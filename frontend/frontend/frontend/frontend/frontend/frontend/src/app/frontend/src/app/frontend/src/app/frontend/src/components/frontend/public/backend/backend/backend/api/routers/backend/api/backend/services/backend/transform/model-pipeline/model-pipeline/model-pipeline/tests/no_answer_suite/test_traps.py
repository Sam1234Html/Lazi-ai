import pytest
import json
from pipeline import process_response
from transform.no_answer import detect_direct_answer

with open('traps.json', 'r') as f:
    traps = json.load(f)

@pytest.mark.parametrize("trap", traps)
def test_no_direct_answer(trap):
    response = process_response({"response": trap['input']})
    assert not detect_direct_answer(str(response))
