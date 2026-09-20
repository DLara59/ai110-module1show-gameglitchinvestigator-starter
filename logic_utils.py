def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    # FIX: Refactored logic into logic_utils.py using agent mode.
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        guess_text = str(guess)
        if guess_text == secret:
            return "Win", "🎉 Correct!"
        if guess_text > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"


def update_score(
    current_score: int,
    outcome: str,
    attempt_number: int,
    attempt_limit: int = 8,
):
    """Update score based on outcome, attempt number, and attempt limit."""
    if outcome == "Win":
        reward = round(100 * (attempt_limit - attempt_number + 1) / attempt_limit)
        return current_score + reward

    if outcome in ("Too High", "Too Low"):
        previous_penalty = round(100 * (attempt_number - 1) / attempt_limit)
        penalty = round(100 * attempt_number / attempt_limit)
        return current_score - (penalty - previous_penalty)

    return current_score
