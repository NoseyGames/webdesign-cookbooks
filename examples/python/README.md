# Python example: asset budget report

A small, complete example for `webdesign-cookbooks`: validate a build's asset manifest, total declared bytes, and fail CI when a project-specific budget is exceeded. It uses Python 3.11+ and the standard library. No installation, credentials, AI API, or network access is needed.

From the repository root:

```sh
python examples/python/asset_budget.py examples/python/assets.sample.json
python examples/python/asset_budget.py examples/python/assets.sample.json --format json --top 3
python -m unittest discover -s tests -p test_python_example.py -v
```

The sample totals **216,000 bytes** against a **250,000-byte** illustrative budget, leaving **34,000 bytes**. Choose a budget for the actual product, device, and network conditions; the sample is not a universal performance target.

## Input contract

```json
{
  "budget_bytes": 250000,
  "assets": [
    {"path": "assets/app.js", "kind": "script", "bytes": 62000}
  ]
}
```

| Field | Contract |
| --- | --- |
| `budget_bytes` | Integer from 1 through 1,000,000,000,000 |
| `assets` | Array of at most 10,000 assets; an empty array is allowed |
| `path` | Unique, case-sensitive relative POSIX identifier, 1–512 printable characters; no empty, `.` or `..` segments, backslashes, or colons |
| `kind` | `script`, `style`, `image`, `font`, or `other` |
| `bytes` | Integer from 0 through 1,000,000,000,000; booleans, floats, and numeric strings are rejected |

Unknown/missing fields and duplicate JSON keys fail. Files must be UTF-8 JSON and at most 1 MiB. This example uses decimal byte counts, without rounding. Equality with the budget passes.

`path` is a label: the program never opens these asset paths. It opens only the manifest selected on the command line. Names are case-sensitive even when the host filesystem is not. The restrictions avoid ambiguous identifiers; they are not a general filesystem sandbox.

## Output and integration

| Exit code | Meaning | Output |
| --- | --- | --- |
| `0` | Valid manifest within budget | Report on stdout |
| `1` | Valid manifest over budget | Report on stdout |
| `2` | Invalid invocation, invalid manifest, or read error | Explanation on stderr |

JSON reports include total, budget, remaining bytes, count, totals per kind, and largest assets. A negative remaining count means over budget. Largest assets sort by descending size, then ascending path. `--top` accepts 1–100.

The module separates `load_manifest()` (I/O), `parse_manifest()` (validation), `summarize()` (calculation), and `main()` (CLI). Domain record constructors are for trusted internal callers; external data must go through `parse_manifest()` or `load_manifest()`. Type annotations alone do not validate constructors.

## What this example demonstrates

- [Validate at boundaries and use types inside](../../recipes/python/01-validation-and-types.md).
- [Separate calculations from I/O](../../recipes/python/02-core-and-boundaries.md).
- [Make errors and CLI behavior explicit](../../recipes/python/03-errors-and-cli.md).
- [Bound input and keep data out of code](../../recipes/python/04-safe-io.md).
- [Test observable contracts](../../recipes/python/05-behavioral-tests.md).

## Limits and next steps

This checks **declared sizes**, not files, compression ratios, browser transfer sizes, caching, loading priorities, or rendering performance. Supply measurements from a build tool using one consistent definition of bytes. A byte budget does not establish that a page is fast.

For a real build integration, first define whether bytes mean raw, gzip, Brotli, or actual transfer sizes. Add an adapter for that build tool's manifest while keeping the existing validated core. If adding file measurement, separately design root containment and symlink behavior. If adding network fetching, separately design timeouts, redirect handling, host policy, and response limits.

Tests exercise invalid input, limits, totals, exact budget boundaries, ordering, and CLI streams/status. They do not claim a security audit or benchmark of the Python program.
