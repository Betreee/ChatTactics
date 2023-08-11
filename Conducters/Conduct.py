
from typing import Dict, Any, Type
from  ChatTactics.Analyzers.AnalyizerBase import AnalyzerBaseClass as Analyzer
# TODO: Add typing for Analyzer ✅
Type[Analyzer] = Type[Analyzer]


class ConversationConductor:
    def __init__(self):
        self.analyzers: Dict[str, Analyzer] = {}

    def add_analyzer(self, name: str, analyzer: Analyzer):
        self.analyzers[name] = analyzer

    def analyze_conversation(self, text: str) -> Dict[str, Any]:
        results = {}
        for name, analyzer in self.analyzers.items():
            try:
                results[name] = analyzer.analyze(text)
            except Exception as e:
                results[name] = str(e)
        return results
