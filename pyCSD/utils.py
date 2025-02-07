def format_results(results: list) -> str:
    """Format analysis results for display"""
    return '\n'.join(
        f"Sentence: {res['sentence']}\nComplex: {res['is_complex']} (Score: {res['complexity_score']})\n"
        for res in results
    )