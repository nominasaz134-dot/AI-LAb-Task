class ClassroomAgent:

    def act(self, temp, occupied):
        if not occupied:
            return "ECO"
        elif 20 <= temp <= 25:
            return "NORMAL"
        elif temp < 18 or temp > 28:
            return "HIGH"
        elif (18 <= temp < 20) or (25 < temp <= 28):
            return "PRE_HEAT_COOL"
        else:
            return "UNKNOWN"
agent = ClassroomAgent()
test_cases = [
    {"temp": 22, "occupied": False, "expected": "ECO"},
    {"temp": 22, "occupied": True, "expected": "NORMAL"},
    {"temp": 15, "occupied": True, "expected": "HIGH"},
    {"temp": 30, "occupied": True, "expected": "HIGH"},
    {"temp": 19, "occupied": True, "expected": "PRE_HEAT_COOL"},
    {"temp": 27, "occupied": True, "expected": "PRE_HEAT_COOL"},
]

for test in test_cases:
    actual = agent.act(test["temp"], test["occupied"])
    print(f"Temp: {test['temp']}°C, Occupied: {test['occupied']} -> {actual}")