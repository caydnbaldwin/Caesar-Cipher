from byu_pytest_utils import max_score, test_files, dialog


@max_score(10)
@dialog(
    test_files / "simple.frequency.expected.txt",
    "frequency.py",
    test_files / "simple.txt"
)
def test_frequency_simple(): ...


@max_score(10)
@dialog(
    test_files / "message.frequency.expected.txt",
    "frequency.py",
    test_files / "message.txt"
)
def test_frequency_message(): ...


@max_score(10)
@dialog(
    test_files / "1Nephi.v1.frequency.expected.txt",
    "frequency.py",
    test_files / "1Nephi.v1.txt"
)
def test_frequency_nephi(): ...
