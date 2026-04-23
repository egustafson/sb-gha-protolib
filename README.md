A Sandbox Example of a Prototypical Library with GitHub Actions
===============================================================

Goal:  create a python library repository that can use a separate
repository for regression testing and when it invokes the regression
tests, it passes the exact revision that is being merged or tagged.

The regression tester will clone that tree for the regression test.

Usage
-----

Run the CLI with a single alphanumeric argument:

```bash
python main.py Alice123
```

Expected output:

```text
Hi Alice123
```

If the argument is missing or contains non-alphanumeric characters, the
program prints:

```text
Not sure who you are.
```

Development
-----------

The repository provides a small set of `make` targets for common tasks:

```bash
make lint
make test
make build
make clean
```

Testing
-------

Install the development dependencies and run the unit tests with:

```bash
make test
```

Run GitHub Actions Workflow Locally
-----------------------------------

You can run the CI workflow locally with `act`.

Common commands:

```bash
act push
act pull_request
act push --tag v0.3.0
act -j lint-and-test
```

Notes:

- `act` requires Docker.
- Workflow behavior is close to GitHub-hosted runners, but not identical.

Release
-------

The repository is prepared for the `v0.3.0` release.

Use this sequence to validate and produce the release artifacts:

```bash
make clean
make lint
make test
make build
```

The build target produces the source distribution and wheel in `dist/`.

Current release: `v0.3.0`.
