import sys
from typing import TextIO

def greeting(name: str = 'World') -> str:
    """Returns greeting message."""
    return f'Hello {name}'


def say_hello(name: str = 'World', file: TextIO = sys.stdout) -> str:
    """Print greeting message."""
    print(greeting(name), file=file)
