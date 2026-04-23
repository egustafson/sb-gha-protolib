from greet import greeter
import main


def test_greeter_greets_alphanumeric_argument():
    assert greeter("Alice123") == "Hi Alice123"


def test_greeter_rejects_non_alphanumeric_argument():
    assert greeter("Alice-123") == "Not sure who you are."


def test_main_greets_alphanumeric_argument(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["main.py", "Alice123"])

    main.main()

    captured = capsys.readouterr()
    assert captured.out == "Hi Alice123\n"


def test_main_rejects_non_alphanumeric_argument(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["main.py", "Alice-123"])

    main.main()

    captured = capsys.readouterr()
    assert captured.out == "Not sure who you are.\n"


def test_main_rejects_missing_argument(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["main.py"])

    main.main()

    captured = capsys.readouterr()
    assert captured.out == "Not sure who you are.\n"
