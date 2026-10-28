import unittest

from semvers import is_prerelease, latest_version, major_of, minor_of, newer, older, parse_version, patch_of, release_of, same_release, same_version, sort_versions, stable_versions, same_minor


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
        self.assertTrue(same_release("1.2.0-rc.1", "1.2.0"))
        self.assertFalse(same_release("1.2.0", "1.3.0"))
        self.assertTrue(older("1.2.0", "1.10.0"))
        self.assertFalse(older("1.2.0", "1.2.0-rc.1"))
        self.assertTrue(newer("1.10.0", "1.2.0"))
        self.assertFalse(newer("1.2.0-rc.1", "1.2.0"))
        self.assertTrue(same_version("1.2.0", "1.2.0"))
        self.assertFalse(same_version("1.2.0", "1.2.0-rc.1"))
        self.assertEqual(stable_versions(["1.2.0", "1.2.0-rc.1", "1.10.0"]), ["1.2.0", "1.10.0"])
        self.assertEqual(major_of("1.10.0"), 1)
        self.assertEqual(major_of("2.0.0-rc.1"), 2)
        self.assertEqual(minor_of("1.10.0"), 10)
        self.assertEqual(patch_of("1.2.9"), 9)
        with self.assertRaises(ValueError):
            latest_version([])

    def test_reject(self) -> None:
        with self.assertRaises(ValueError):
            parse_version("1.2")


        self.assertTrue(same_minor("1.10.0", "2.10.3"))
        self.assertFalse(same_minor("1.2.0", "1.3.0"))

if __name__ == "__main__":
    unittest.main()
