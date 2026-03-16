import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from app import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_check_guess_secret_always_integer():
    # Bug fix: secret was previously cast to a string on even attempts.
    # When secret is a string "10", string comparison makes "9" > "10" (alphabetically),
    # so check_guess(9, "10") would wrongly return "Too High".
    # With an integer secret, check_guess(9, 10) must correctly return "Too Low".
    outcome, _ = check_guess(9, 10)
    assert outcome == "Too Low", (
        "check_guess(9, 10) returned wrong outcome — "
        "likely caused by secret being compared as a string"
    )
