import os

from invoke import task

here = os.path.dirname(os.path.realpath(__file__))


@task
def set_pythonpath(c):
    os.environ["PYTHONPATH"] = here


@task(pre=[set_pythonpath])
def test(c):
    c.run(f"python {here}/fabelio_price_tracker/manage.py behave")


@task
def service(c, stop=False):
    if stop:
        c.run("docker-compose stop")
    else:
        c.run("docker-compose up -d")


@task(pre=[service, set_pythonpath])
def migrate(c):
    c.run(f"python {here}/fabelio_price_tracker/manage.py migrate")


@task(pre=[set_pythonpath])
def makemigrations(c, check=False):
    cmd = f"python {here}/fabelio_price_tracker/manage.py makemigrations"
    if check:
        cmd = f"{cmd} --check --dry-run"
    c.run(cmd)
