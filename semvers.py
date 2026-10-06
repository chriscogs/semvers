"""Compare dotted version strings with an optional prerelease."""
from __future__ import annotations

from functools import total_ordering


@total_ordering
class Version:
    def __init__(self, major: int, minor: int, patch: int, pre: tuple[str, ...] = ()) -> None:
        self.major = major
        self.minor = minor
        self.patch = patch
        self.pre = pre

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Version):
            return NotImplemented
        return (self.major, self.minor, self.patch, self.pre) == (
            other.major,
            other.minor,
            other.patch,
            other.pre,
        )

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Version):
            return NotImplemented
        core = (self.major, self.minor, self.patch)
        other_core = (other.major, other.minor, other.patch)
        if core != other_core:
            return core < other_core
        if not self.pre and other.pre:
            return False
        if self.pre and not other.pre:
            return True
        return self.pre < other.pre

    def __repr__(self) -> str:
        text = f"{self.major}.{self.minor}.{self.patch}"
        if self.pre:
            text += "-" + ".".join(self.pre)
        return text


def parse_version(text: str) -> Version:
    raw = (text or "").strip()
    if not raw or raw.startswith("-") or raw.endswith("-"):
        raise ValueError(f"版本号不合法: {text}")
    core, _, pre = raw.partition("-")
    parts = core.split(".")
    if len(parts) != 3 or not all(part.isdigit() for part in parts):
        raise ValueError(f"版本号不合法: {text}")
    pre_parts = tuple(piece for piece in pre.split(".") if piece) if pre else ()
    if pre and len(pre_parts) != pre.count(".") + 1:
        raise ValueError(f"预发布不合法: {text}")
    return Version(int(parts[0]), int(parts[1]), int(parts[2]), pre_parts)


def sort_versions(items: list[str]) -> list[str]:
    return sorted(items, key=parse_version)


def is_prerelease(text: str) -> bool:
    return bool(parse_version(text).pre)


def same_release(left: str, right: str) -> bool:
    return release_of(left) == release_of(right)


def release_of(text: str) -> str:
    parsed = parse_version(text)
    return f"{parsed.major}.{parsed.minor}.{parsed.patch}"


def latest_version(items: list[str]) -> str:
    if not items:
        raise ValueError("没有版本")
    return max(items, key=parse_version)
