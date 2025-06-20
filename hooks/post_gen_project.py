from subprocess import run


run(["git", "init"], check=True)
run(["pre-commit", "autoupdate"], check=True)
