import spacy

class ComplexSentenceDetector:
    """Detect complex sentences using linguistic features"""
    
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')
        if 'sentencizer' not in self.nlp.pipe_names:
            self.nlp.add_pipe('sentencizer')
    
    def analyze_text(self, text: str) -> list:
        """Analyze text and return sentence complexity"""
        doc = self.nlp(text)
        return [self._analyze_sentence(sent) for sent in doc.sents]
    
    def _analyze_sentence(self, sentence) -> dict:
        """Analyze individual sentence complexity"""
        return {
            'sentence': sentence.text,
            'is_complex': self._is_complex(sentence),
            'complexity_score': self._calculate_complexity(sentence)
        }
    
    def _is_complex(self, sentence) -> bool:
        """Determine if sentence is complex based on rules"""
        return self._calculate_complexity(sentence) >= 2
    
    def _calculate_complexity(self, sentence) -> int:
        """Calculate complexity score based on multiple features"""
        score = 0
        score += self._check_conjunctions(sentence)
        score += self._check_clauses(sentence)
        score += self._check_sentence_length(sentence)
        return score
    
    @staticmethod
    def _check_conjunctions(sentence) -> int:
        """Check for coordinating/subordinating conjunctions"""
        return 1 if any(token.dep_ in ('cc', 'mark') for token in sentence) else 0
    
    @staticmethod
    def _check_clauses(sentence) -> int:
        """Estimate clauses by counting main verbs"""
        return 1 if len([token for token in sentence if token.pos_ == 'VERB']) > 1 else 0
    
    @staticmethod
    def _check_sentence_length(sentence) -> int:
        """Check sentence length threshold"""
        return 1 if len(sentence.text.split()) > 20 else 0