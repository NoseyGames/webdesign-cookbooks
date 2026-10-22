# Validate once at the boundary; use types inside

**Use when:** decoding JSON, reading configuration, consuming API payloads, or accepting user input.

Write the contract before the implementation. Include shape, units, ranges, empty values, unknown fields, and whether coercion is allowed. A successful JSON parse establishes syntax, not domain validity.

## Before: coercion hides bad data

```python
def total(payload):
    return sum(int(row.get("bytes", 0)) for row in payload["assets"])
```

This silently treats a missing size as zero, accepts `True` as `1`, truncates floats, and makes failures depend on where the value happens to be used.

## After: explicit domain meaning

```python
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Asset:
    path: str
    bytes: int


def parse_asset(value: object) -> Asset:
    if not isinstance(value, dict) or set(value) != {"path", "bytes"}:
        raise ValueError("asset must contain exactly path and bytes")
    path, size = value["path"], value["bytes"]
    if not isinstance(path, str) or not path.strip():
        raise ValueError("path must be a nonempty string")
    if type(size) is not int or size < 0:
        raise ValueError("bytes must be a nonnegative integer")
    return Asset(path=path, bytes=size)
```

The exact `int` check deliberately excludes booleans for this schema. Do not apply exact-type checks indiscriminately to extensible application objects. A frozen dataclass prevents normal field reassignment; nested mutable members would still need their own treatment. The full example uses a tuple of records.

Python annotations are not runtime checks, and dataclasses do not automatically enforce annotated field types. Use runtime validation for outside data and a static checker for internal mistakes; they solve different problems. See the official [typing](https://docs.python.org/3.11/library/typing.html) and [dataclasses](https://docs.python.org/3.11/library/dataclasses.html) references.

## Decisions and tradeoffs

- Reject unknown fields for a tightly controlled configuration format so typos are visible. A public API may need forward compatibility instead; document that policy.
- Permit coercion only when the product contract calls for it, such as parsing human-entered numeric text. Never let `int()` silently define the business rules.
- Use `object` for an unchecked value and narrow it. Use `Any` where integration truly requires it, rather than letting it erase checks throughout the program.
- Add `TypedDict` for useful static dictionary shapes, `Literal` for a small closed set, and a dataclass for stable records. None replaces boundary validation.
- For a large evolving schema, an established validation library can reduce custom code. Evaluate its coercion rules and dependency cost first.

**Verify:** missing fields, unknown fields, `None`, `True`, negative values, zero, exact limits, excessive values, and malformed nested shapes. Use exact integers for byte counts. For money, choose decimal arithmetic or integer minor units with an explicit currency/rounding policy.

**Runnable reference:** [`parse_manifest()`](../../examples/python/asset_budget.py) and [manifest tests](../../tests/test_python_example.py).
