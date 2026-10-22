# Give errors a contract

**Use when:** building a CLI, library boundary, API handler, or integration that needs predictable failure behavior.

Distinguish invalid input, expected operational failure, and a programming defect. Decide which layer can recover. An error should name the violated requirement or failed operation without dumping credentials or complete input documents.

## Before: a failure becomes a fake success

```python
def load(path):
    try:
        return parse_file(path)
    except Exception:
        return {}
```

The caller cannot distinguish an empty configuration from a missing file, malformed document, or application bug. A broad retry around this code could repeatedly retry a permanent input error.

## After: translate only where meaning changes

```python
import json


class InvalidConfig(ValueError):
    pass


def decode(source: str) -> object:
    try:
        return json.loads(source)
    except json.JSONDecodeError as exc:
        raise InvalidConfig(
            f"invalid JSON at line {exc.lineno}, column {exc.colno}"
        ) from exc
```

Keep the original cause for debugging. At the CLI boundary, catch known input and I/O errors, write a useful message to stderr, and return an error status. Let unexpected programming errors remain visible during development. Python documents [exception selection and chaining](https://docs.python.org/3.11/tutorial/errors.html).

## CLI policy

The [complete example](../../examples/python/README.md) reserves stdout for the report and stderr for errors. A valid over-budget report exits `1`; invalid input exits `2`; a passing report exits `0`. These are the example's interface decisions, not universal Python rules.

Use `argparse` for named options, help, choices, and argument validation. It produces usage/help and handles invalid invocations; keep business logic outside parser callbacks. See the official [argparse reference](https://docs.python.org/3.11/library/argparse.html).

## Decisions and tradeoffs

- Catch `FileNotFoundError` separately if recovery differs from permission failure. A small CLI can display both as read errors while keeping exception types intact in its library function.
- Retry transient operations only with a bounded attempt count, timeout, and clear idempotency rules. Do not retry validation failures.
- In a service, log an unexpected exception once with useful context and a request ID, then return an appropriate generic response. Do not return stack traces to clients.
- Do not log the same error at every layer. Let the layer that owns the operation own the user-facing report.
- A CLI pipeline may need a defined broken-pipe policy. File-output tools also need explicit overwrite and partial-write behavior; this read-only example does not implement them.

**Verify:** help works, malformed invocation fails, input errors omit tracebacks, stdout stays parseable, over-budget results remain available, and library callers receive useful exception types.

**Tests:** [CLI and file failure cases](../../tests/test_python_example.py).
