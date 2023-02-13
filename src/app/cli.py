import typer

app = typer.Typer()


@app.callback()
def callback():
    """
    Awesome Portal Gun
    """


@app.command()
def shoot(name: str) -> str:
    """
    Shoot the portal gun
    """
    # s = f'Shoot portal gun {name}'
    s = "Shoot portal gun {}".format(name)
    typer.echo(s)
    # print(s)
    return s


@app.command()
def load():
    """
    Load the portal gun
    """
    typer.echo("Loading portal gun")
