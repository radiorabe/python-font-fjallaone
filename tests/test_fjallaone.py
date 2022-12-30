"""Tests for the main package."""

from pathlib import PurePath

import font_fjallaone


def test_is_defined():
    """Check if the font is loaded and defined."""
    assert len(font_fjallaone.font_files) == 1
    assert font_fjallaone.font_name == "FjallaOne"

    path = PurePath(font_fjallaone.font)
    assert path.name == "FjallaOne-Regular.ttf"
