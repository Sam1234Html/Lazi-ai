from transform.no_answer import detect_direct_answer, enforce_no_answer

def process_response(raw):
    if detect_direct_answer(str(raw)):
        return enforce_no_answer(raw)
    return raw

# Example usage
if __name__ == "__main__":
    raw = {"response": "The answer is 42."}  # Trap
    transformed = process_response(raw)
    print(transformed)
