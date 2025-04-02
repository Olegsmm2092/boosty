# Project Setup

## Overview
This project requires initializing the database state before starting work. You can reset the database to its initial state using either a shell script (`reset.sh`) or a Python script (`reset.py`).

## Getting Started

### Prerequisites
- Ensure `reset.sh` has execution permissions by running:
  ```sh
  chmod +x reset.sh
  ```

### Resetting the Database
Before starting, reset the database using one of the following methods:

#### Using Python:
```sh
python3 reset.py
```

#### Using Shell Script:
```sh
./reset.sh
```

## Notes
- Running `reset.py` or `reset.sh` will overwrite `db.json` with `freshdb.json`.
- Ensure `reset.sh` has execution permissions (`chmod +x reset.sh`).

## License
This project is licensed under the MIT License.

