import os
import hashlib
from datetime import datetime
from unittest.mock import patch, mock_open
from your_code_file import (  # change this to your actual Python file
    hash_password,
    add_glucose,
    calculate_insulin,
    log_meal,
    current_time
)

# ---------- Test hash_password ----------
def test_hash_password_same():
    assert hash_password("mypassword") == hash_password("mypassword")

def test_hash_password_different():
    assert hash_password("mypassword") != hash_password("otherpassword")

# ---------- Test add_glucose ----------
@patch("builtins.input", side_effect=["150"])
@patch("builtins.open", new_callable=mock_open)
@patch("your_code_file.logged_in_user", "testuser")
def test_add_glucose(mock_input, mock_file, mock_user):
    add_glucose()
    assert mock_file.called

# ---------- Test calculate_insulin ----------
@patch("builtins.input", return_value="250")
def test_calculate_insulin_above_180(mock_input):
    # Should suggest insulin dose
    calculate_insulin()

@patch("builtins.input", return_value="120")
def test_calculate_insulin_below_180(mock_input):
    # Should say no insulin needed
    calculate_insulin()

# ---------- Test log_meal ----------
@patch("builtins.input", side_effect=["Lunch", "45"])
@patch("builtins.open", new_callable=mock_open)
@patch("your_code_file.logged_in_user", "testuser")
def test_log_meal(mock_input, mock_file, mock_user):
    log_meal()
    assert mock_file.called

# ---------- Test current_time ----------
def test_current_time_format():
    time_str = current_time()
    datetime.strptime(time_str, "%Y-%m-%d %H:%M")
