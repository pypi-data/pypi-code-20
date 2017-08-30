import pytest
from datetime import datetime
from typing import Any, List, Set
from jsonschema_extractor.typing_extractor import TypingExtractor

@pytest.fixture
def typing_extractor():
    return TypingExtractor()

@pytest.mark.parametrize("inp, expected_output", [
    (int, {"type": "integer"}),
    (float, {"type": "number"}),
    (str, {"type": "string"}),
    (type(None), {"type": "null"}),
    (datetime, {"type": "string", "format": "date-time"}),
    (List[int], {
        "type": "array",
        "items": {
            "type": "integer"
        }
    }),
])
def test_extract_typing(extractor, inp, expected_output):
    assert extractor.extract(inp) == expected_output


def test_typing_extractor_register(typing_extractor):

    def extract_set(extractor, typ):
        subtype = Any
        if typ.__args__ and typ.__args__[0] is not Any:
            subtype = typ.__args__[0]
        return {
            "type": "array",
            "title": "set",
            "items": extractor.extract(extractor, subtype)
        }

    typing_extractor.register(set, extract_set)

    assert typing_extractor.extract(typing_extractor, Set[int]) == {
        "type": "array",
        "title": "set",
        "items": {"type": "integer"}
    }
