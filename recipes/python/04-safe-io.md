# Bound input and keep data out of executable syntax

**Use when:** accepting outside data, launching a process, querying a database, or reading files.

Identify the actual boundary. A local configuration reader needs size and schema rules. A URL fetcher also needs host/redirect policy and timeouts. A file uploader needs storage and path rules. Do not assume one validator solves all of these.

## Before: external text becomes a shell command

```python
import os

def inspect_size(filename: str) -> None:
    os.system("wc -c " + filename)
```

Shell metacharacters and whitespace now have executable meaning. The command also depends on a platform-specific tool.

## After: use a direct API when it meets the need

```python
from pathlib import Path

def inspect_size(filename: str) -> int:
    return Path(filename).stat().st_size
```

This reads metadata for the requested path; it does not establish that the path is authorized. If an application restricts files to a root, enforce that separately and consider symlinks and concurrent changes.

When a subprocess is necessary, use an explicitly selected executable, an argument list, `shell=False`, a timeout, and a deliberate nonzero-exit policy. Argument lists avoid shell interpolation, but the target program can still interpret options. Do not accept arbitrary executables or assume `shell=False` makes untrusted Windows batch scripts safe. See Python's [subprocess security considerations](https://docs.python.org/3.11/library/subprocess.html#security-considerations).

## Bound parsing before parsing

```python
LIMIT = 1_048_576
with path.open("rb") as stream:
    content = stream.read(LIMIT + 1)
if len(content) > LIMIT:
    raise ValueError("configuration is too large")
```

Reading one extra byte distinguishes a complete bounded input from a larger file without first reading it all. A prior `stat()` size check alone would not bound the subsequent read. The JSON documentation recommends limiting untrusted data because decoding consumes CPU and memory. The example additionally rejects duplicate keys and non-finite constants. See the official [JSON reference](https://docs.python.org/3.11/library/json.html).

## The same principle in SQL

```python
# Before: input is embedded into SQL syntax.
query = f"SELECT id FROM users WHERE email = '{email}'"

# After: pass values separately from the statement.
row = connection.execute(
    "SELECT id FROM users WHERE email = ?", (email,)
).fetchone()
```

Placeholders bind values, not table names or sort directions. Choose dynamic identifiers from an allowlist. See the official [sqlite3 placeholder guidance](https://docs.python.org/3.11/library/sqlite3.html#how-to-use-placeholders-to-bind-values-in-sql-queries).

**Tradeoffs:** limits need a documented reason and an upgrade path for legitimate large inputs. JSON size limits are useful controls, not a sandbox against every hostile workload. For remote inputs add response caps and deadline policy; for secrets avoid payload logging; for writes define overwrite, cleanup, and atomicity requirements.

**Runnable reference:** [`load_manifest()`](../../examples/python/asset_budget.py) bounds a local JSON read and never opens paths embedded in that JSON.
