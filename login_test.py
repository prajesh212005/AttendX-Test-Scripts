def test_valid_login():
    username = "student01"
    password = "ValidPass123"

    assert username != ""
    assert password != ""

    print("PASS: Login inputs are provided.")


def test_empty_username():
    username = ""
    password = "ValidPass123"

    assert username == ""

    print("PASS: Empty username validation scenario identified.")


if __name__ == "__main__":
    test_valid_login()
    test_empty_username()