import subprocess, sys

def validate_md5() -> bool:
    """Reads arguments from terminal, it must be file_path and then the given md5 string.

    Usage:
        python md5_checker 'path_to_file' 'correct_md5'
        
    Returns:
        bool: It returns true if both strings are equal, false otherwise.
    """
    file_path = sys.argv[1]
    given_md5_str = sys.argv[2]
    file_md5 = subprocess.run(['md5', file_path], capture_output=True)
    file_md5_str = file_md5.stdout.decode().split('= ')[1].replace('\n', '')
    if file_md5_str == given_md5_str:
        return True
    return False

if __name__ == '__main__':
    result = validate_md5()
    print(result)

