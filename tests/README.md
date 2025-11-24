# Tests Directory

This directory is reserved for unit tests and integration tests.

## Structure

```
tests/
├── test_admin_menu.py      # Admin menu tests
├── test_user_menu.py       # User menu tests
├── test_autentikasi.py     # Authentication tests
├── test_storage.py         # Storage/data tests
└── fixtures/               # Test data and fixtures
    └── sample_data.json
```

## Running Tests

Once tests are added, run with:

```bash
# Using pytest
pytest

# Using unittest
python -m unittest discover -s tests -p "test_*.py"

# With coverage
pytest --cov=src tests/
```

## Testing Guidelines

- Use pytest or unittest framework
- Create fixtures for test data
- Test both success and failure cases
- Maintain >80% code coverage
- Test validation and error handling

## TODO

- [ ] Add pytest dependency to requirements.txt
- [ ] Create test fixtures
- [ ] Write unit tests for each module
- [ ] Add integration tests
- [ ] Set up CI/CD with GitHub Actions
