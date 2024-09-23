from pathlib import Path

from byu_pytest_utils import max_score, this_folder, run_python_script
import string


def read_cipher(cipher_file: Path) -> dict:
    with open(cipher_file) as file:
        cipher = {}
        for line in file:
            s, t = line.strip().split(',')
            cipher[s] = t
    return cipher

@max_score(10)
def test_build():
    cipher_file = this_folder / "cipher.observed.csv"
    cipher_file.unlink(missing_ok=True)
    build_codex_old = this_folder / 'build_codex.py'
    if build_codex_old.exists():
        build_codex_old.rename('build_cipher.py')
    run_python_script("build_cipher.py", cipher_file)

    cipher1 = read_cipher(cipher_file)

    for c in string.ascii_lowercase:
        if c not in cipher1.keys():
            raise Exception(f'"{c}" not found as key in cipher. Not all letters of alphabet are found in first column.')

    for c in string.ascii_lowercase:
        if c not in cipher1.values():
            raise Exception(f'"{c}" not found as value in cipher. '
                            f'Not all letters of alphabet are found in second column.')

    run_python_script("build_cipher.py", cipher_file)

    cipher2 = read_cipher(cipher_file)

    if cipher1 == cipher2:
        raise Exception('Re-running build_cipher.py produced the same dictionary. '
                        'build_cipher.py should be produce a random cipher each time.')