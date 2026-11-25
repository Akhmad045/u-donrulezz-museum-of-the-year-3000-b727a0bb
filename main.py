#!/usr/bin/env python3
"""Museum of the Year 3000 — the label beside a group chat.

A museum in the year 3000 has never seen a group chat in use, so it
describes the thing the way a curator describes a relic: object, date,
then one deadpan sentence that misreads it as a physical chamber where
hundreds of people gathered every night for the sole purpose of ignoring
one another at the same time.

The program writes exactly that label, one line, to /output/entry.txt.
"""
import argparse
import hashlib
import sys
import tempfile
from pathlib import Path

LABEL = (
    "Group chat, c. 2025. A chamber where 214 humans gathered nightly "
    "to ignore one another in perfect unison."
)

ENTRY_PATH = Path("/output/entry.txt")
LIMIT = 200


def label() -> str:
    """The museum label, exactly as it goes into the entry file."""
    return LABEL


def check(text: str) -> list[str]:
    """Return every way the text breaks the entry gate, or [] if valid."""
    faults = []
    if not text.strip():
        faults.append("entry is blank")
    if len(text) < 1 or len(text) > LIMIT:
        faults.append("length %d is outside 1..%d" % (len(text), LIMIT))
    if text != text.strip():
        faults.append("leading or trailing whitespace")
    for bad in ("\n", "\r", "\t"):
        if bad in text:
            faults.append("must be one line with no control characters")
            break
    return faults


def write_entry(text: str, where: Path = ENTRY_PATH) -> Path:
    """Write the label to the entry file, creating its folder as needed."""
    where.parent.mkdir(parents=True, exist_ok=True)
    where.write_text(text, encoding="utf-8")
    return where


def summary(text: str) -> str:
    """Chars, bytes, sha256 and gate verdict for one line of text."""
    raw = text.encode("utf-8")
    digest = hashlib.sha256(raw).hexdigest()
    faults = check(text)
    verdict = "OK" if not faults else "FAIL: " + "; ".join(faults)
    return "chars=%d bytes=%d sha256=%s gate=%s" % (
        len(text), len(raw), digest, verdict)


def run_self_test() -> int:
    """Gate the label, prove a write round-trips, probe the boundaries."""
    problems = []
    if check(label()):
        problems.append("label fails its own gate: %s" % check(label()))
    with tempfile.TemporaryDirectory() as tmp:
        probe = Path(tmp) / "entry.txt"
        write_entry(label(), probe)
        if probe.read_bytes() != label().encode("utf-8"):
            problems.append("round-trip mismatch: written bytes differ")
    cases = [
        ("", False),
        ("   ", False),
        ("x" * 201, False),
        ("two\nlines", False),
        (" padded ", False),
        ("x", True),
        ("y" * 200, True),
    ]
    for text, should_pass in cases:
        passed = not check(text)
        if passed != should_pass:
            problems.append(
                "probe %r: expected %s, got %s"
                % (text[:20], "pass" if should_pass else "fail",
                   "pass" if passed else "fail"))
    if problems:
        print("self-test FAILED")
        for problem in problems:
            print("  - " + problem)
        return 1
    print("self-test OK: " + summary(label()))
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true",
                        help="gate checks, boundary probes and write round-trip")
    parser.add_argument("--info", action="store_true",
                        help="print chars, bytes, sha256 and gate verdict")
    parser.add_argument("--out", default=str(ENTRY_PATH),
                        help="where to write the entry (default: %(default)s)")
    args = parser.parse_args(argv)
    if args.self_test:
        return run_self_test()
    if args.info:
        print(summary(label()))
        return 0
    faults = check(label())
    if faults:
        print("entry fails the gate: " + "; ".join(faults), file=sys.stderr)
        return 1
    write_entry(label(), Path(args.out))
    print("wrote %s (%d chars)" % (args.out, len(label())))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
