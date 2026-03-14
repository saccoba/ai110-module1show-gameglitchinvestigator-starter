def get_range_for_difficulty(difficulty: str):
    d = (difficulty or "").strip().lower()

    if d == "easy":
        return 1, 20
    elif d == "normal":
        return 1, 100
    elif d == "hard":
        return 1, 1000

    raise ValueError(f"Unknown difficulty: {difficulty!r}")


def parse_guess(raw: str):
    if raw is None:
        return False, None, "Enter a guess."

    raw = raw.strip()
    if raw == "":
        return False, None, "Enter a guess."

    try:
        value = int(raw)
    except ValueError:
        return False, None, "That is not a number."
    return True, value, None


def check_guess(guess, secret):
    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        return "Too High", "📈 Go LOWER!"
    return "Too Low", "📉 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    if outcome != "Win":
        return current_score

    points = 100 - 10 * (attempt_number - 1)
    if points < 10:
        points = 10
    return current_score + points