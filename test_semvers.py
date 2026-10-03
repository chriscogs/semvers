import unittest

from semvers import is_prerelease, latest_version, parse_version, release_of, sort_versions


class SemversTest(unittest.TestCase):
    def test_prerelease_is_older(self) -> None:
        self.assertLess(parse_version("1.2.0-alpha"), parse_version("1.2.0"))
        self.assertEqual(
            sort_versions(["1.10.0", "1.2.0", "1.2.0-rc.1"]),
            ["1.2.0-rc.1", "1.2.0", "1.10.0"],
        )

    def test_latest(self) -> None:
        self.assertEqual(latest_version(["1.2.0", "1.10.0", "1.2.0-rc.1"]), "1.10.0")
        self.assertTrue(is_prerelease("1.2.0-rc.1"))
        self.assertFalse(is_prerelease("1.2.0"))
        self.assertEqual(release_of("1.2.0-rc.1"), "1.2.0")
        with self.assertRaises(ValueError):
            latest_version([])

    def test_reject(self) -> None:
        with self.assertRaises(ValueError):
            parse_version("1.2")


if __name__ == "__main__":
    unittest.main()
