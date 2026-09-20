from logic_utils import check_guess, get_range_for_difficulty, update_score


def test_winning_guess():
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")


def test_guess_too_high_regression():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"


def test_guess_too_low_regression():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


def test_guess_boundary_feedback_regression():
    #FIX Preserve logical higher/lower hints at the valid range boundaries.
    assert check_guess(0, 1) == ("Too Low", "📈 Go HIGHER!")
    assert check_guess(101, 100) == ("Too High", "📉 Go LOWER!")


def test_difficulty_ranges_regression():
    #FIX Keep each difficulty's configured range aligned with the game rules.
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 50)


def test_update_score_tracks_points():
    assert update_score(0, "Win", 1, 8) == 100
    assert update_score(0, "Win", 2, 8) == 88
    assert update_score(0, "Too High", 1, 8) == -12

    score = 0
    for attempt_number in range(1, 9):
        score = update_score(score, "Too Low", attempt_number, 8)
    assert score == -100


def test_regression_game_flow_and_end_state():
    # Score must still track and increment on a win.
    assert update_score(0, "Win", 1, 8) == 100

    # The high/low feedback must be correct when the guess is on the wrong side.
    assert check_guess(60, 50) == ("Too High", "📉 Go LOWER!")
    assert check_guess(40, 50) == ("Too Low", "📈 Go HIGHER!")

    # A correct guess should end the round and stop further play.
    assert check_guess(50, 50)[0] == "Win"
