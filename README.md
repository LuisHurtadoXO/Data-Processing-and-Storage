# Data-Processing-and-Storage

## Overview

This project implements a simple in-memory key-value database with transaction support. The database supports the following operations:

- `begin_transaction()`
- `put(key, value)`
- `get(key)`
- `commit()`
- `rollback()`

All keys are strings and values are integers. You can call `get()` at any time, but `put()` operations are only allowed inside a transaction. Transactions ensure changes are not visible to `get()` until the transaction is committed. Rolling back a transaction discards all uncommitted changes.

## How to Run: 

### Prerequisites
- Python 3 is installed on your machine.

### Steps
1. Clone this repository or download the source files.
2. Open a terminal or command prompt and navigate to the directory containing `in_memory_db.py` and `main.py`.
3. Run the following command to execute the test driver:
   
   'python3 main.py' or 'python main.py'

4. If compiled correctly, the output should confirm the correct behavior of the database.

## Suggested Modifications for an Official Assignment:

Clarifications in Instructions: Explicitly state that get() should never return uncommitted changes, and emphasize that only one transaction can exist at a time.
Additional Methods and Testing: Introduce helper methods and require students to write their own more complex unit tests. Provide a starter test suite to ensure basic correctness.
Grading Enhancements: Implement automated grading scripts that run a suite of tests (maybe both provided and hidden) to check that code is adequate. This encourages students to evaluate and follow best practices in testing.
