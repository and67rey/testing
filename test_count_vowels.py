import pytest
from AT02 import count_vowels

@pytest.mark.parametrize("test_input,expected", [
    ('апрель', 2),
    ('Антарес', 3),
    ('Python', 2),
    ('Orion', 3),
    ('АоУЕ', 4),
    ('uEaiO', 5),
    ('йЦКнГшЩз', 0),
    ('QwrTPsDFg', 0),
    ('', 0),
    ('12345', 0),
    ('~!@#$%^&*()_-+=|:;/.,', 0),
])
def test_count_vowels(test_input, expected):
    assert count_vowels(test_input) == expected