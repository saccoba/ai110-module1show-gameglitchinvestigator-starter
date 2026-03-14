def get_range_for_difficulty(difficulty: str): 
    d = (difficulty or "").strip().lower()

    if d == "easy":
        return 1, 20
    elif d == "normal":
        return 1, 100
    elif d == "hard":
        return 1, 1000  #Fixme: Updated the range for "Hard" difficulty to 1-1000 to make it more challenging, with AI help.
    

    raise ValueError(f"Unknown difficulty: {difficulty!r}")


def parse_guess(raw: str):
    if raw is None:
        return False, None, "Enter a guess."
    
    raw = raw.strip()  #Fixme: Added a new line and remove the spaces.

    if raw == "":
        return False, None, "Enter a guess."
    
    try:
        value = int(float(raw))    #Fixme: Removed "if "." in raw:"" and handle decimal safely.
    except ValueError:             #Fixme:Removed " else:, and value = int(raw)" so that it can handle both int and float inputs.
        return False, None, "That is not a number."
    return True, value, None


def check_guess(guess, secret):
    if guess == secret:
        return "Win", "🎉 Correct!"
    elif guess > secret:
        return "Too High", "📈 Go LOWER!"  #Fixme: Reverse the hint corrected after debugging with AI
    else:
        return "Too Low", "📉 Go HIGHER!"  #Fixme: Reverse the hint corrected after debugging with AI


def update_score(current_score: int, outcome: str, attempt_number: int):
    if outcome != "Win":
        return current_score

    points = 100 - 10 * attempt_number   #fixme: Changed the points calculation to 100 - 10 * attempt_number, so that the player gets more points for winning in fewer attempts, with AI help.
    if points < 10:
        points = 10
    return current_score + points
