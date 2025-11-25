# Configuration Directory

This directory is reserved for application configuration files and settings.

## Structure

```
config/
├── settings.json           # Main application settings
├── logging.json            # Logging configuration
└── database.json           # Database configuration (for future use)
```

## Current Configuration

Currently, all configuration is hardcoded in the source files:
- Database paths: `storage.py`
- Menu options: `main.py`, `admin_menu.py`, `user_menu.py`
- Validation rules: `admin_menu.py`, `user_menu.py`

## Future Plans

- [ ] Extract settings to `settings.json`
- [ ] Create configuration loader
- [ ] Support environment variables
- [ ] Add logging configuration
- [ ] Support different environments (dev, test, prod)

## Example: Future settings.json

```json
{
  "app": {
    "name": "K-Blacklist",
    "version": "1.0.0",
    "debug": false
  },
  "data": {
    "path": "data/",
    "format": "json"
  },
  "validation": {
    "rating_min": 0.0,
    "rating_max": 10.0,
    "min_username_length": 3,
    "min_password_length": 5
  },
  "ui": {
    "use_colors": true,
    "use_emoji": true
  }
}
```

## Usage Example (Future)

```python
from config.settings import load_settings

settings = load_settings()
rating_max = settings['validation']['rating_max']
```
