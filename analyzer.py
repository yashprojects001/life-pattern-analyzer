def analyze_life_pattern(sleep, screen, work, mood):
    burnout_score = 0

    if sleep < 6:
        burnout_score += 2
    if screen > 7:
        burnout_score += 2
    if work > 8:
        burnout_score += 2
    if mood <= 2:
        burnout_score += 2

    if burnout_score >= 6:
        burnout = "HIGH 🔴"
        advice = "You are at high risk of burnout. Reduce screen time and rest more."
    elif burnout_score >= 3:
        burnout = "MODERATE 🟠"
        advice = "Your balance is off. Try improving sleep and mood."
    else:
        burnout = "LOW 🟢"
        advice = "You are managing your life patterns well. Keep it up!"

    productivity = "HIGH" if work <= 6 and sleep >= 7 else "MEDIUM" if work <= 8 else "LOW"

    return {
        "burnout": burnout,
        "productivity": productivity,
        "advice": advice
    }
