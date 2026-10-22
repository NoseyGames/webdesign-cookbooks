# Python cookbook

Use these recipes to guide implementation and review. They are reusable engineering instructions and examples, not model weight updates. Start with a concrete behavior and a small design; add machinery when a requirement justifies it.

| Recipe | Use when | Main question |
| --- | --- | --- |
| [Validation and types](01-validation-and-types.md) | Data enters from JSON, users, files, or APIs | What makes this value valid? |
| [Core and boundaries](02-core-and-boundaries.md) | A function mixes decisions and side effects | What can be computed without I/O? |
| [Errors and CLI](03-errors-and-cli.md) | Failures need useful, predictable behavior | Who can recover, and how? |
| [Safe I/O](04-safe-io.md) | Reading input or calling external systems | What is untrusted, and what is bounded? |
| [Behavioral tests](05-behavioral-tests.md) | A change must preserve important behavior | What failure would hurt the user? |

Run the [complete asset-budget example](../../examples/python/README.md), then inspect its [tests](../../tests/test_python_example.py).

## Prompt to use with an agent

> Target Python 3.11 or newer. Read the applicable recipes before coding. State input/output contracts and failure behavior. Keep validation at external boundaries, calculations independent of I/O, and error handling narrow. Prefer the standard library when it meets the need. Add tests for meaningful behavior and edge cases. Run them and report the actual command, outcome, and any untested environment. Explain tradeoffs without adding abstractions for hypothetical future needs.

Review criteria: correct results, explicit boundary handling, readable data flow, justified dependencies, minimal permissions, meaningful tests, and truthful verification. An attractive architecture diagram does not compensate for an incorrect result.
