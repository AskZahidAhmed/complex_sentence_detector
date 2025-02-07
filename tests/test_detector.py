import pytest
from complex_sentence_detector.detector import ComplexSentenceDetector

@pytest.fixture
def detector():
    return ComplexSentenceDetector()

def test_simple_sentence(detector):
    text = "The quick brown fox jumps over the lazy dog."
    results = detector.analyze_text(text)
    assert not results[0]['is_complex']

def test_complex_sentence(detector):
    text = "Although it was raining heavily, I went for a walk because I needed fresh air."
    results = detector.analyze_text(text)
    assert results[0]['is_complex']