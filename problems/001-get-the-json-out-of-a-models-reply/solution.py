import json


def parse_model_json(reply):
    """Return the JSON object in a model's reply, or None if there isn't one."""
    decoder = json.JSONDecoder()

    for i, char in enumerate(reply):
        if char == "{":
            try:
                obj, _ = decoder.raw_decode(reply[i:])
                if isinstance(obj, dict):
                    return obj
            except json.JSONDecodeError:
                continue

    return None
    
