import pytest
from AT02 import count_vowels

@pytest.mark.parametrize("test_input,expected", [
    ('апрель', 2),
    ('Антарес', 3),
    ('эффект наблюдателя', 7),
    ('Осип охрип, Архип осип', 8),
    ('Python', 2),
    ('Orion', 3),
    ('East or West home is best', 8),
    ('АоУЕ', 4),
    ('uEaiO', 5),
    ('оУАиюЯ EuoAI', 11),
    ('йЦКнГшЩз', 0),
    ('QwrTPsDFg', 0),
    ('zXDrnGtPKmq цНгКтРМЧж', 0),
    ('', 0),
    ('12345', 0),
    ('Лаланд 21185', 2),
    ('TRAPPIST-1', 2),
    ('~!@#$% ^&*()_- +=| :;/.,', 0),
])
def test_count_vowels(test_input, expected):
    assert count_vowels(test_input) == expected