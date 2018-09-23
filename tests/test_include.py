def test_import():
    import osa_cli_bugs.bugmgmt #noqa: F401
    import osa_cli_bugs.cli #noqa: F401


def test_import_when_click():
    try:
        import click #noqa: F401
    except ImportError:
        pass
    else:
        import osa_cli_bugs.click #noqa: F401
