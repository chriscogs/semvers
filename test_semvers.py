import unittest

from semvers import parse_version, sort_versions


class SemversTest(unittest.TestCase):
    def test_prerelease_is_older(self) -> None:
        self.assertLess(parse_version("1.2.0-alpha"), parse_version("1.2.0"))
        self.assertEqual(
            sort_versions(["1.10.0", "1.2.0", "1.2.0-rc.1"]),
            ["1.2.0-rc.1", "1.2.0", "1.10.0"],
        )

    def test_reject(self) -> None:
        with self.assertRaises(ValueError):
            parse_version("1.2")


if __name__ == "__main__":
    unittest.main()
