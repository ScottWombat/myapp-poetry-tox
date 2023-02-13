from typer.testing import CliRunner

from app.cli import app


def test_shoot_command():
    runner = CliRunner()
    result = runner.invoke(app, ["shoot", "rev"])

    # assert result.exit_code == 0
    # print(result)
    assert "Shoot portal gun rev" == result.output.strip()
    # assert "Rev" in result.stdout


def test_load_command():
    runner = CliRunner()
    result = runner.invoke(app, ["load"])
    assert "Loading portal gun" == result.output.strip()


def test_callback_command():
    runner = CliRunner()
    result = runner.invoke(app, ["callback"])
    assert "callback" in result.output
