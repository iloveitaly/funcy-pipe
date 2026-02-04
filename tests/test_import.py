"""Test funcy-pipe."""

import funcy_pipe


def test_import() -> None:
    """Test that the  can be imported."""
    assert isinstance(funcy_pipe.__name__, str)