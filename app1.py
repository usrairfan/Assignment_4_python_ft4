import app
def test_main():
    result = app.add(2,4)
    assert result == 6, "2+4 should be 6"