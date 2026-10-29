def check_eligibility(score, documents_complete, attendance, fee_clear):

    if score < 70:
        return "Hold", "Score is below 70."

    if not documents_complete:
        return "Hold", "Required documents are incomplete."


    if attendance < 75:
        return "Hold", "Attendance is below 75%."

    if not fee_clear:
        return "Hold", "Fee status is not clear."

    return "Review", "All four conditions are satisfied."

test_cases = [
    {
        "name": "Test 1 - All Conditions Pass",
        "score": 80,
        "documents_complete": True,
        "attendance": 85,
        "fee_clear": True,
        "expected": "Review"
    },
    {
        "name": "Test 2 - Attendance Failure",
        "score": 80,
        "documents_complete": True,
        "attendance": 70,
        "fee_clear": True,
        "expected": "Hold"
    },
    {
        "name": "Test 3 - Fee Condition Failure",
        "score": 85,
        "documents_complete": True,
        "attendance": 90,
        "fee_clear": False,
        "expected": "Hold"
    },
    {
        "name": "Test 4 - Threshold Boundary",
        "score": 70,
        "documents_complete": True,
        "attendance": 75,
        "fee_clear": True,
        "expected": "Review"
    }
]

print("=" * 60)
print("       RULE-BASED SCHOLARSHIP SCREENING SYSTEM")
print("=" * 60)

for test in test_cases:
    actual, reason = check_eligibility(
        test["score"],
        test["documents_complete"],
        test["attendance"],
        test["fee_clear"]
    )

    print("\n", test["name"])
    print("Input:")
    print("Score:", test["score"])
    print("Documents Complete:", test["documents_complete"])
    print("Attendance:", str(test["attendance"]) + "%")
    print("Fee Clear:", test["fee_clear"])

    print("Expected Result:", test["expected"])
    print("Actual Result:", actual)
    print("Reason:", reason)

    if actual == test["expected"]:
        print("Test Status: PASS")
    else:
        print("Test Status: FAIL")

    print("-" * 60)