# Keep decisions separate from I/O

**Use when:** a function reads files, calls services, calculates a result, prints output, and exits the process.

Start with a direct flow: read → validate → calculate → present. Name the steps after their responsibilities. The goal is to make behavior easy to reason about and change, not to maximize the number of layers.

## Before: everything happens together

```python
import json
from pathlib import Path


def check(path):
    data = json.loads(Path(path).read_text())
    total = sum(row["bytes"] for row in data["assets"])
    print(total)
    if total > data["budget_bytes"]:
        raise SystemExit(1)
```

Testing the arithmetic now involves a filesystem and captured output. Reusing it from a web handler risks terminating the process.

## After: a pure decision and a small adapter

```python
from collections.abc import Iterable


def is_over_budget(sizes: Iterable[int], budget: int) -> bool:
    """Trusted inputs: nonnegative byte counts and a positive budget."""
    return sum(sizes) > budget


def run_check(manifest) -> int:
    # The caller has already validated the manifest.
    total = sum(asset.bytes for asset in manifest.assets)
    print(f"{total} / {manifest.budget_bytes} bytes")
    return int(total > manifest.budget_bytes)
```

This small illustration separates process policy from calculation. In the complete example, `summarize()` returns a typed `Report`, `format_text()` builds presentation, and `main()` translates the report into output and an exit code. Only the `__main__` guard exits.

## Decisions and tradeoffs

- Accept the narrowest useful interface. `Sequence` expresses indexed/repeated access; `Iterable` expresses one pass. Do not consume a generator twice accidentally.
- Pass a clock, client, or repository only when the calculation actually needs that dependency. Keep framework-specific request objects out of the domain core.
- A record with three fields is often clearer than a factory, interface, service, and manager around the same three fields.
- Extract a module when a responsibility is stable and reused, or the current file becomes hard to navigate. A small CLI can remain a single well-organized file.
- Keep mutable state local. Cache only after measurement and with defined invalidation, bounds, and concurrency behavior.
- Streaming reduces peak memory but can complicate sorting and validation. The example bounds input and sorts at most 10,000 records; a much larger dataset needs a different plan.

The example's aggregation is linear in asset count; sorting the largest list is `O(n log n)`. If only a tiny top list is needed over millions of assets, consider a bounded heap after measuring the actual bottleneck.

**Verify:** deterministic outputs, identical totals for reordered inputs, explicit tie-breaking, no hidden network access, and no process exit on library import.

**Runnable reference:** [`summarize()`, `format_text()`, and `main()`](../../examples/python/asset_budget.py). Python's [dataclasses reference](https://docs.python.org/3.11/library/dataclasses.html) explains the generated record methods used here.
