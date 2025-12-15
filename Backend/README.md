# Job Application Backend

A robust Django REST API backend for managing job postings and applications. The system supports two primary user roles: recruiters who can post and manage jobs, and applicants who can search for and apply to positions.

## Project Overview

This is a full-featured job application platform backend built with Django and Django REST Framework. It handles user authentication, job management, application tracking, resume processing, and matching algorithms. The system integrates with Supabase for file storage and Cloudinary for media management.

## Key Features

The application provides role-based access control with two distinct user types. Recruiters can create, update, and manage job listings, while applicants can search for jobs and submit applications with resume uploads. The system includes automated resume text extraction and intelligent matching of applicants to job requirements using keyword analysis. Additional features include JWT-based authentication, comprehensive API documentation with Swagger UI, PostgreSQL database integration, and cloud storage for resumes through Cloudinary and Supabase.

## Technology Stack

The backend is built on Django 6.0 with Django REST Framework 3.16.1 for API development. Authentication is handled through SimpleJWT for token-based access. The system uses PostgreSQL for the relational database, Cloudinary for cloud-based image and file storage, and Supabase as an alternative file storage backend. API documentation is generated using drf-yasg, and environment variables are managed through python-dotenv.

## Prerequisites

Before running this project, ensure you have the following installed on your system. You will need Python 3.8 or higher, pip for package management, and PostgreSQL database. Additionally, you will need accounts and API credentials for Cloudinary and Supabase.

## Project Structure

The project follows Django's modular application architecture. The main components are organized as follows:

- accounts: User authentication, custom user model with role support, and user permissions
- jobs: Job listing models, serializers, and API endpoints for recruitment operations
- applications: Job application tracking, resume storage, and matching logic
- core: Shared utilities including custom exception handlers, pagination, and response formatting
- dashboard: Dashboard analytics and recruiter performance metrics
- config: Django project configuration, settings, and URL routing

## Environment Setup

Follow these steps to set up the development environment for the first time.

### 1. Create a Virtual Environment

```bash
python3 -m venv venv
```

### 2. Activate the Virtual Environment

On macOS or Linux:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\\Scripts\\activate
```

### 3. Install Required Dependencies

Install all Python packages specified in requirements.txt:

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a .env file in the root directory of the project. Add the following environment variables with your actual credentials:

```
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
SUPABASE_BUCKET=your_supabase_bucket_name
CLOUDINARY_CLOUD_NAME=your_cloudinary_cloud_name
CLOUDINARY_API_KEY=your_cloudinary_api_key
CLOUDINARY_API_SECRET=your_cloudinary_api_secret
```

### 5. Configure the Database

Update the database credentials in config/settings.py if needed. The current configuration uses PostgreSQL with the following default settings:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'job_app',
        'USER': 'shubham',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Make sure PostgreSQL is running and the job_app database exists. You can create it using:

```bash
createdb job_app
```

### 6. Apply Database Migrations

Run all pending database migrations to set up the schema:

```bash
python manage.py migrate
```

### 7. Create a Superuser

Create an admin user to access the Django admin panel:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up your admin username, email, and password.

## Running the Project

### Start the Development Server

To run the Django development server:

```bash
python manage.py runserver
```

The API will be accessible at http://localhost:8000

### Access the Admin Panel

The Django admin interface is available at http://localhost:8000/admin

Use the superuser credentials created earlier to log in.

### Access API Documentation

Swagger UI documentation is available at http://localhost:8000/api/docs

ReDoc documentation is available at http://localhost:8000/api/redoc

## API Endpoints Overview

The application exposes the following main API endpoints:

### Authentication
- POST /api/auth/login: User login and token generation
- POST /api/auth/register: New user registration
- POST /api/auth/refresh: Refresh authentication token

### Job Management
- GET /api/jobs: List all active job postings
- POST /api/jobs: Create a new job posting (recruiter only)
- GET /api/jobs/{id}: Retrieve specific job details
- PUT /api/jobs/{id}: Update job posting (recruiter only)
- DELETE /api/jobs/{id}: Remove job posting (recruiter only)
- GET /api/jobs/{id}/applications: View applications for a job (recruiter only)

### Job Applications
- GET /api/applications: List user's applications
- POST /api/applications: Submit a new application
- GET /api/applications/{id}: View application details
- PUT /api/applications/{id}: Update application (applicant only)
- DELETE /api/applications/{id}: Withdraw application (applicant only)

### User Management
- GET /api/users/profile: Get current user profile
- PUT /api/users/profile: Update user profile
- GET /api/users/{id}: View another user's public profile

## Database Schema

The application uses the following main data models:

### CustomUser
Extends Django's built-in user model with role support. Users can be either recruiters or applicants. Fields include id, username, email, password, role, first_name, last_name, and timestamps.

### Job
Represents job listings posted by recruiters. Contains job_id (UUID), title, description, keywords, location, experience_required, salary_min, salary_max, is_active status, and timestamp fields. Each job is associated with the recruiting user who created it.

### Application
Tracks job applications from applicants. Stores the relationship between users and jobs, resume file URLs from Cloudinary, extracted text from resumes, and calculated match scores. Each user can only apply to each job once.

### Dashboard
Stores recruiter analytics including job posting statistics, application metrics, and performance data for dashboard visualization.

## Authentication

The application uses JSON Web Tokens (JWT) for API authentication. After logging in, the user receives an access token and a refresh token. The access token is valid for 24 hours, while the refresh token is valid for 7 days. Include the access token in the Authorization header of API requests:

```
Authorization: Bearer <your_access_token>
```

## File Upload and Storage

Resume files uploaded by applicants are stored in Cloudinary. The system converts uploaded files to URLs and stores these references in the database. The Application model includes a resume_file field that contains the Cloudinary URL for easy access and sharing. Configuration for Cloudinary is set through environment variables and initialized in settings.py.

## Managing Static Files

To collect all static files for production deployment:

```bash
python manage.py collectstatic
```

## Troubleshooting

If you encounter database connection issues, verify that PostgreSQL is running and the credentials in settings.py are correct. You can test the connection with:

```bash
psql -U shubham -d job_app -h localhost -W
```

If migrations fail, ensure all previous migrations have been applied and check for any pending migrations:

```bash
python manage.py showmigrations
```

For issues with external services like Cloudinary or Supabase, verify that your API credentials are correct and that the services are accessible. Check your internet connection and firewall settings if you cannot reach these services.

If you encounter permission errors, ensure your virtual environment is properly activated and you have write permissions in the project directory.

## Additional Commands

Run tests to verify functionality:

```bash
python manage.py test
```

Create new database migrations after model changes:

```bash
python manage.py makemigrations
```

Open the Django shell for interactive queries:

```bash
python manage.py shell
```

Clean up temporary files and cache:

```bash
python manage.py cleanuploadedfiles
```

## Security Considerations

The current settings.py contains DEBUG=True which is suitable only for development. Before deploying to production, change DEBUG to False and update ALLOWED_HOSTS with your actual domain names. The SECRET_KEY in settings should be replaced with a secure, randomly generated value. Never commit the .env file containing sensitive credentials to version control. Always use HTTPS in production and configure CORS settings appropriately for your frontend domain. Ensure database passwords are strong and change default credentials before deploying.

## Deployment

For production deployment, follow Django's deployment checklist at https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

Key points include setting DEBUG to False, configuring ALLOWED_HOSTS, using a production database, setting secure CORS origins, and using a production-grade web server like Gunicorn with Nginx as a reverse proxy.

## Support and Further Reading

Refer to the official Django documentation at https://docs.djangoproject.com for detailed information about Django features and configurations. For Django REST Framework specifics, visit https://www.django-rest-framework.org. Consult the SimpleJWT documentation at https://django-rest-framework-simplejwt.readthedocs.io for authentication details. Check Cloudinary documentation at https://cloudinary.com/documentation for file storage configuration. Supabase documentation is available at https://supabase.com/docs for alternative storage solutions.
