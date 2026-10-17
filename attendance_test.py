def test_mark_attendance():
    student_id = "ST101"
    attendance_status = "Present"

    assert student_id != ""
    assert attendance_status in ["Present", "Absent"]

    print("PASS: Attendance data is valid.")


def test_invalid_attendance_status():
    attendance_status = "Unknown"

    assert attendance_status not in ["Present", "Absent"]

    print("PASS: Invalid attendance status is identified.")


if __name__ == "__main__":
    test_mark_attendance()
    test_invalid_attendance_status()