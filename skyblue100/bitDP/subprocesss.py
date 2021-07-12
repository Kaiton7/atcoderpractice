import subprocess
def run():
    commands = {'Flake8': 'flake8 --config=.flake8rc .'.split(),
                'Pylint': 'pylint --rcfile=.pylintrc howdoi'.split()}

    for linter, command in commands.items():
        try:
            print(f'\nRunning {linter}...')
            subprocess.check_call(command)
            print(f'No lint errors found by {linter}')
        except FileNotFoundError:
            print(f'{linter} not installed')
        except subprocess.CalledProcessError:
            pass

print(run())