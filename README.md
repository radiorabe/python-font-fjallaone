# Python Package with Fjalla One Font

Python Package with [Fjalla One](https://fonts.google.com/specimen/Fjalla+One) from
[Sorkin Type](https://github.com/pimoroni/fonts-python) as distributed by
[Google Fonts](https://fonts.google.com) for use with
[fonts-python](https://github.com/pimoroni/fonts-python).

## Installation

```bash
pip install font_fjallaone
```

## Usage

```python
from font_fjallaone import FjallaOne
```

## Release Management

The CI/CD setup uses semantic commit messages following the [conventional commits standard](https://www.conventionalcommits.org/en/v1.0.0/).
There is a GitHub Action in [.github/workflows/semantic-release.yaml](./.github/workflows/semantic-release.yaml)
that uses [go-semantic-commit](https://go-semantic-release.xyz/) to create new
releases.

The commit message should be structured as follows:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

The commit contains the following structural elements, to communicate intent to the consumers of your library:

1. **fix:** a commit of the type `fix` patches gets released with a PATCH version bump
1. **feat:** a commit of the type `feat` gets released as a MINOR version bump
1. **BREAKING CHANGE:** a commit that has a footer `BREAKING CHANGE:` gets released as a MAJOR version bump
1. types other than `fix:` and `feat:` are allowed and don't trigger a release

If a commit does not contain a conventional commit style message you can fix
it during the squash and merge operation on the PR.

Once a commit has landed on the `main` branch a release will be created and automatically published to [pypi](https://pypi.org/)
using the GitHub Action in [.github/workflows/release.yaml](./.github/workflows/release.yaml) which uses [poetry](https://python-poetry.org/)
to publish the package to pypi.

## Copyright

Copyright (c) 2022 [Radio Bern RaBe](http://www.rabe.ch)
