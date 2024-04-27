"""Fjalla One from from Sorkin Type as distributed by Google Fonts."""

from pathlib import Path

font_directory = Path(__file__).parent.resolve() / "files"

font_files = {}

for font in list(font_directory.glob("*.ttf")):
    font_name = (
        Path(font).name.replace(".ttf", "").replace("-Regular", "").replace("-", "")
    )
    font_files[font_name] = font
    globals()[font_name] = font
