# create a factory class
class AnalyzerFactory:
    _analyzers = {
        # "Behavioral": BehavioralAnalyzer,
        # "Complex": ComplexModelsAnalyzer,
        # "Conflict": ConflictDetectionAnalyzer,
        # "Contextual": ContextualUnderstandingAnalyzer,
        # "Cooperation": CooperationDetectionAnalyzer,
        # "Cultural": CulturalReferencesAnalyzer,
        # "Emotion": EmotionAnalyzer,
        # "Handler": emotionHandler,
        # "Fact": FactCheckingAnalyzer,
        # "Gaussian": GaussianAnalyzer,
        # "Happiness": HappinessAnalyzer,
        # "Humor": HumorAnalyzer,
        # "Influence": InfluenceAndPersuasionAnalyzer,
        # "Intent": IntentAnalyzer,
        # "Interpersonal": InterpersonalRelationsAnalyzer,
        # "Ironyand": IronyandHumorAnalyzer,
        # "Irony": IronyandHumorAnalyzer,
        # "Language": LanguageAndMeaningAnalyzer,
        # "Socialnetwork": SocialnetworkAnalyzer,
        # "N": NLPAnalyzer,
        # "Politeness": PolitenessFormalityAnalyzer,
        # "Power": PowerDynamicsAnalyzer,
        # "Relationship": RelationshipAnalyzer,
        # "Role": RoleAndPowerAnalyzer,
        # "Detailed": DetailedSentimentAnalyzer,
        # "Social": SocialAndInfluenceAnalyzer,
        # "Subjectivity": SubjectivityAndObjectivityAnalyzer,
        # "Trigger": TriggerWordIdentifier
    }

    # define a method to get an analyzer
    @staticmethod
    def get_analyzer(analyzer_type, *args, **kwargs):
        # try to return the analyzer and place its prompt from the dict
        try:
            analyzer_class = AnalyzerFactory._analyzers.get(analyzer_type)
            if analyzer_class:
                return analyzer_class(*args, **kwargs)
            else:
                raise Exception(
                    "Analyzer type not supported, please try again.",
                    analyzer_type,
                )
        finally:
            print()
