# Corporate Asset Tracking System

## Overview
This Django application is designed to track corporate assets such as phones, tablets, laptops, and other gears assigned to employees. The application allows companies to manage their assets efficiently, track their usage, and maintain a log of device assignments and returns.

## Features
- **Company Management**: Companies can register and manage their information within the system.
- **Employee Management**: Employees can be added and associated with their respective companies.
- **Device Management**: Devices can be added, assigned to employees, and tracked for usage.
- **Device Log**: A log is maintained for each device, recording details of checkouts and check-ins, including the condition of the device.

## Installation
1. Clone the repository:
   ```
   git clone <repository_url>
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```
   python manage.py migrate
   ```
4. Create a superuser (for admin access):
   ```
   python manage.py createsuperuser
   ```
5. Run the development server:
   ```
   python manage.py runserver
   ```

## Usage
- Access the Django admin interface at `http://localhost:8000/admin` to manage companies, employees, devices, and device logs.
- Use the provided API endpoints to interact with the system programmatically. API documentation can be found at `http://localhost:8000/swagger/` or `http://localhost:8000/redoc/`.

## API Endpoints
- **Companies**: `/api/companies/`
- **Employees**: `/api/employees/`
- **Devices**: `/api/devices/`
- **Device Logs**: `/api/devicelogs/`

## Testing
Unit tests are provided to ensure the correctness of the application. Run tests using:
```
python manage.py test
```

