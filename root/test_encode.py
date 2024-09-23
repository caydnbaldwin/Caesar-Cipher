from byu_pytest_utils import max_score, test_files, dialog


@max_score(10)
@dialog(
    test_files / "simple.encoded.expected.txt",
    "encode.py",
    test_files / "cipher.csv",
    test_files / "simple.txt",
    test_files / "simple.encoded.observed.txt",
    output_file=test_files / "simple.encoded.observed.txt"
)
def test_encode_simple(): ...


@max_score(10)
@dialog(
    test_files / "message.encoded.expected.txt",
    "encode.py",
    test_files / "cipher.csv",
    test_files / "message.txt",
    test_files / "message.encoded.observed.txt",
    output_file=test_files / "message.encoded.observed.txt"
)
def test_encode_message(): ...


@max_score(10)
@dialog(
    test_files / "1Nephi.v1.encoded.expected.txt",
    "encode.py",
    test_files / "cipher.csv",
    test_files / "1Nephi.v1.txt",
    test_files / "1Nephi.v1.encoded.observed.txt",
    output_file=test_files / "1Nephi.v1.encoded.observed.txt"
)
def test_encode_nephi(): ...
