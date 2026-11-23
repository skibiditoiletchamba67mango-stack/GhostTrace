

# GhostTrace OSINT

A simple, beginner-friendly Python OSINT tool for checking publicly available information and metadata.

## Features

- **Email Checker** — Checks email format and domain MX records.
- **Username Search** — Creates links to public profile pages.
- **Phone Checker** — Checks phone number format and region.
- **Photo Inspector** — Reads image metadata and GPS coordinates when available.
- **Discord ID Decoder** — Estimates when a Discord ID was created.

## Installation

### 1. Install Python

Download Python from https://www.python.org/downloads/

### 2. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/GhostTrace.git
cd GhostTrace
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run GhostTrace

```bash
python main.py
```

## Requirements

- Python 3.10 or newer
- Internet connection for email MX checks
- Dependencies listed in `requirements.txt`

## Disclaimer

GhostTrace is an educational OSINT project.

Use it responsibly and only with information you are authorized to investigate.

This tool does not:
- Hack accounts or bypass security.
- Access private profiles or messages.
- Track someone's live location.
- Identify the owner of a phone number or Discord ID.
- Guarantee that a username exists on a platform.

Photo GPS information is read only from metadata already present in the supplied image.

## License

This project is licensed under the MIT License.
