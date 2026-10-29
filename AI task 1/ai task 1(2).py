def symbolic_checker(score, complete):
    return "Review" if complete and score >= 70 else "Hold"


def simulated_llm_assistant(score, complete):
    if score >= 70:
        return f"Approved: High score of {score} achieves priority benchmark."
    return "Hold: Low score."

score, complete = 91, False
rule_decision = symbolic_checker(score, complete)
llm_response = simulated_llm_assistant(score, complete)

print(f"Symbolic Rule Decision : {rule_decision}")  # Output: Hold
print(f"Conversational Output  : {llm_response}")  # Output: Approved...
print(
    f"Policy Violation Flag  : {rule_decision != 'Review' and 'Approved' in llm_response}"
)  