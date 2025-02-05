# Flask-api
This is a public API developed for the HNG Stage 0 Backend Task using **Flask**.

## API Documentation

### Endpoint
- **GET** `/`

### Response Format
```json
{
  "email": "olawlehabibat81@gmail.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/abibat_dev/flask-api"
}
```
## Setup Instructions

### Install dependencies
```
pip install -r requirements.txt
```

### run app
```
gunicorn app:app
```

### Open `http://127.0.0.1:8000/` in your browser to test 

### Backlink
[HNG Hire Python Developers](https://hng.tech/hire/python-developers)
