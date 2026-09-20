from logic_utils import check_guess, update_score


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


def test_update_score_tracks_points():
    assert update_score(0, "Win", 1) == 80
    assert update_score(10, "Too High", 2) == 15
    assert update_score(10, "Too Low", 3) == 5


def test_regression_game_flow_and_end_state():
    # Score must still track and increment on a win.
    assert update_score(0, "Win", 1) == 80

    # The high/low feedback must be correct when the guess is on the wrong side.
    assert check_guess(60, 50) == ("Too High", "📉 Go LOWER!")
    assert check_guess(40, 50) == ("Too Low", "📈 Go HIGHER!")

    # A correct guess should end the round and stop further play.
    assert check_guess(50, 50)[0] == "Win"
