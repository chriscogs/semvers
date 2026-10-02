# semvers

Sort version strings that look like `1.2.3` or `1.2.3-rc.1`.

A prerelease sorts before the matching release. Numeric core parts compare as integers, so `1.10.0` comes after `1.2.0`. Build metadata (`+git`) is not accepted.

```python
from semvers import sort_versions, latest_version, is_prerelease

sort_versions(["1.10.0", "1.2.0", "1.2.0-rc.1"])
latest_version(["1.2.0", "1.10.0"])  # "1.10.0"
is_prerelease("1.2.0-rc.1")          # True
```

```bash
python -m unittest test_semvers.py
```

MIT
