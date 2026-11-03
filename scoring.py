"""Shared typing metrics. WPM uses the standard five-character convention."""
from collections import Counter

def analyze_result(target: str, typed: str, elapsed: float) -> dict:
    correct = sum(1 for i, c in enumerate(typed) if i < len(target) and c == target[i])
    errors = len(typed) - correct
    duration_min = max(elapsed, .001) / 60
    gross_wpm = (len(typed)/5)/duration_min
    net_wpm = (correct/5)/duration_min
    accuracy = (correct / len(typed) * 100) if typed else 0
    wrong_keys = Counter(c.lower() for i,c in enumerate(typed) if i >= len(target) or c != target[i])
    return {
        'gross_wpm': round(gross_wpm,1), 'net_wpm': round(net_wpm,1),
        'accuracy': round(accuracy,1), 'errors':errors, 'correct':correct,
        'typed_chars':len(typed), 'elapsed':round(elapsed,1),
        'completion':round(min(len(typed)/len(target)*100,100),1),
        'problem_keys':[{'key':k if k!=' ' else 'Space','count':v} for k,v in wrong_keys.most_common(5)]
    }
