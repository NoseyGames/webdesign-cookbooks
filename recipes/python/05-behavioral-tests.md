# Test behavior that would matter if it broke

**Use when:** fixing a bug, adding a boundary, changing calculations, or establishing a reusable example.

Choose a small set of observations that defines success. A test should fail if the implementation is wrong, not merely if its internal structure changes.

## Before: a smoke check misses the bug

```python
def test_report():
    assert summarize(example_manifest)
```

Any truthy report passes, including one with wrong totals, an incorrect budget comparison, or missing assets.

## After: pin down a boundary with observable behavior

```python
import unittest
from asset_budget import parse_manifest, summarize


class BudgetBoundaryTests(unittest.TestCase):
    def test_equality_passes_and_one_more_byte_fails(self):
        for size, expected in ((100, False), (101, True)):
            with self.subTest(size=size):
                manifest = parse_manifest({
                    "budget_bytes": 100,
                    "assets": [
                        {"path": "app.js", "kind": "script", "bytes": size}
                    ],
                })
                self.assertEqual(summarize(manifest).over_budget, expected)
```

Run this snippet with `examples/python` on the import path, or run the [complete suite](../../tests/test_python_example.py) from the repository root:

```sh
python -m unittest discover -s tests -p test_python_example.py -v
```

## A useful test matrix

| Concern | Example observation |
| --- | --- |
| Ordinary result | 40 + 60 bytes produces a total of 100 |
| Boundary | Equal budget passes; one byte over fails |
| Invalid input | `True`, missing size, and negative size fail |
| Empty input | Empty asset list produces zero and no largest assets |
| Determinism | Equal-size assets sort by path |
| Resource policy | Oversized file fails before JSON decoding |
| Integration | CLI returns the documented code and separates stdout/stderr |

Use temporary directories for real file behavior. Use a real subprocess for a few CLI checks so imports, argument parsing, streams, and process status are exercised together. These small local tests are inexpensive and need no mocks. Python's [unittest reference](https://docs.python.org/3.11/library/unittest.html) documents discovery, assertion methods, fixtures, cleanup, and subtests.

## Decisions and tradeoffs

- Prefer pure-function tests for calculations and a few integration checks for adapters. Do not mock every function until the test only confirms that mocks were called.
- For a bug fix, add the smallest regression case that fails before the fix and passes after it.
- Use hand-computed expected values. Reimplementing the same algorithm in the assertion can reproduce its mistake.
- Test error categories and useful context. Avoid pinning full platform-specific OS error messages.
- Snapshot output only when the full output is the contract. Huge snapshots make meaningful changes hard to review.
- Add property-based tests when input combinations warrant them; they add a dependency and require thoughtful properties.
- Record the Python version and command actually run. Passing locally on one interpreter does not prove every supported platform works.

**Review question:** if `>` accidentally became `>=`, or `True` slipped through as a byte count, would the suite fail? The complete example deliberately covers both.
