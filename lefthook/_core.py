import subprocess
import sys
from shutil import which


COMMANDS = (
    'go get github.com/Arkweid/lefthook',
    'brew install Arkweid/lefthook/lefthook',
    'npm install @arkweid/lefthook --save-dev',
    'gem install lefthook',
)


def _install(command: str) -> bool:
    executable = command.split(' ', maxsplit=1)[0]
    if not which(executable):
        print('#', executable, 'not found')
        return False
    result = subprocess.run(command.split())
    if result.returncode != 0:
        return False
    print('# installed with', executable)
    return True


def install() -> bool:
    for command in COMMANDS:
        if _install(command):
            return True
    return False


def run(argv: list = None) -> int:
    if argv is None:
        argv = sys.argv

    if not which('lefthook'):
        print('# lefthook not found, trying to install')
        if not install():
            print('! cannot install lefthook')
            return 1

    result = subprocess.run(['lefthook'] + argv[1:])
    return result.returncode
