# Complex Sentence Detector

This script detects complex sentences in a text file using SpaCy and readability analysis.

## Installation

1. Clone the repository:
```bash
	git clone https://github.com/yourusername/complex-sentence-detector.git
	cd complex-sentence-detector
```

2. Create a virtual environment (optional but recommended):
```bash
	python3 -m venv venv
	source venv/bin/activate  # On Windows use `venv\Scripts\activate
```

3. Install dependencies:
```bash
	pip install -r requirements.txt
```

4. Download the required SpaCy model:
	```bash
	python -m spacy download en_core_web_sm

5. Run the script with a text file as input:
	```bash
	python detect_complex_sentences.py input.txt





```python
from pyCSD import ComplexSentenceDetector
from pyCSD import format_results

detector = ComplexSentenceDetector()
text = "Your input text here..."
results = detector.analyze_text(text)
print(format_results(results))
```

Conjunctions: Coordinating (and, but) or subordinating (although, because)
Multiple Clauses: Presence of multiple main verbs
Sentence Length: More than 20 words
Threshold: Score ≥ 2 marks as complex

