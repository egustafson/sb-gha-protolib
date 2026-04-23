# Changelog

All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog and this project follows Semantic
Versioning.

## [Unreleased]

### Added

- Added a GitHub Actions CI workflow for lint and test on pushes, pull
  requests to main, and tags.
- Documented how to run the CI workflow locally using `act`.

## [0.1.0] - 2026-04-23

### Added

- Added the `greet` module with a `greeter()` function for validating and
  formatting greetings.
- Added a CLI entry point in `main.py` that delegates to `greeter()`.
- Added pytest unit tests covering valid, invalid, and missing CLI
  arguments.
- Added `make` targets for linting, testing, building, and cleaning.

### Changed

- Added packaging metadata for building source and wheel distributions.
- Documented usage, development commands, and release steps in the README.
