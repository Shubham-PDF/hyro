# Job Portal Backend API Documentation

## Base URL

```
http://localhost:8000/
```

---

## Table of Contents

1. [Authentication](#authentication)
2. [User Management (Accounts)](#user-management-accounts)
3. [Jobs](#jobs)
4. [Applications](#applications)
5. [Error Handling](#error-handling)

---

## Authentication

### 1. User Signup

**Endpoint:** `POST /auth/signup/`

**Description:** Create a new user account

**Permission:** Public (No authentication required)

**Request Body:**

```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "securepassword123",
  "role": "applicant",
  "full_name": "John Doe",
  "phone": "+1234567890"
}
```

**Request Parameters:**

- `username` (string, required): Unique username for login
- `email` (string, required): Valid email address
- `password` (string, required): Password for authentication
- `role` (string, required): Either `"recruiter"` or `"applicant"`
- `full_name` (string, required): Full name of the user
- `phone` (string, optional): Phone number

**Response (201 Created):**

```json
{
  "id": 1,
  "username": "john_doe",
  "email": "john@example.com",
  "role": "applicant",
  "full_name": "John Doe",
  "phone": "+1234567890"
}
```

**Error Responses:**

- `400 Bad Request`: Invalid data (e.g., missing required fields, password too short, email already exists)
- `409 Conflict`: Username or email already exists

---

### 2. User Login

**Endpoint:** `POST /auth/login/`

**Description:** Get JWT access and refresh tokens

**Permission:** Public (No authentication required)

**Request Body:**

```json
{
  "username": "john_doe",
  "password": "securepassword123"
}
```

**Request Parameters:**

- `username` (string, required): User's username
- `password` (string, required): User's password

**Response (200 OK):**

```json
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**Response Parameters:**

- `access`: JWT token for API requests (valid for ~5 minutes)
- `refresh`: Token to refresh access token (valid for longer)

**Error Responses:**

- `401 Unauthorized`: Invalid credentials
- `400 Bad Request`: Missing username or password

---

### 3. Refresh Token

**Endpoint:** `POST /auth/refresh/`

**Description:** Get a new access token using refresh token

**Permission:** Public (No authentication required)

**Request Body:**

```json
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**Request Parameters:**

- `refresh` (string, required): The refresh token

**Response (200 OK):**

```json
{
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**Error Responses:**

- `401 Unauthorized`: Invalid or expired refresh token

---

## User Management (Accounts)

### 4. Get Current User Profile

**Endpoint:** `GET /auth/me/`

**Description:** Get the authenticated user's profile information

**Permission:** IsAuthenticated (Requires valid JWT token)

**Headers:**

```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

**Response (200 OK):**

```json
{
  "id": 1,
  "username": "john_doe",
  "email": "john@example.com",
  "role": "applicant",
  "full_name": "John Doe",
  "phone": "+1234567890",
  "linkedin_url": "https://linkedin.com/in/johndoe",
  "github_url": "https://github.com/johndoe"
}
```

**Error Responses:**

- `401 Unauthorized`: Missing or invalid token
- `404 Not Found`: User not found

---

### 5. Update User Profile

**Endpoint:** `PATCH /auth/me/update/`

**Description:** Update user profile information

**Permission:** IsAuthenticated (Requires valid JWT token)

**Headers:**

```
Authorization: Bearer YOUR_ACCESS_TOKEN
Content-Type: application/json
```

**Request Body (all fields optional):**

```json
{
  "full_name": "John Doe Updated",
  "phone": "+1234567891",
  "about": "Full-stack developer with 5 years of experience",
  "linkedin_url": "https://linkedin.com/in/johndoe",
  "github_url": "https://github.com/johndoe",
  "portfolio_url": "https://johndoe.com",
  "skills": ["Python", "Django", "React", "PostgreSQL"]
}
```

**Request Parameters:**

- `full_name` (string, optional): Full name
- `phone` (string, optional): Phone number
- `about` (string, optional): About/Bio
- `linkedin_url` (string, optional): LinkedIn profile URL
- `github_url` (string, optional): GitHub profile URL
- `portfolio_url` (string, optional): Portfolio website URL
- `skills` (array, optional): List of skills

**Response (200 OK):**

```json
{
  "message": "Profile updated successfully"
}
```

**Error Responses:**

- `400 Bad Request`: Invalid data format
- `401 Unauthorized`: Missing or invalid token

---

### 6. Delete User Account

**Endpoint:** `DELETE /auth/me/delete/`

**Description:** Permanently delete user account and all associated data

**Permission:** IsAuthenticated (Requires valid JWT token)

**Headers:**

```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

**Response (204 No Content):**

```
No content
```

**Error Responses:**

- `401 Unauthorized`: Missing or invalid token
- `404 Not Found`: User not found

---

## Jobs

### 7. Create Job Posting

**Endpoint:** `POST /jobs/create/`

**Description:** Create a new job posting (Recruiters only)

**Permission:** IsAuthenticated + IsRecruiter (User must be logged in with recruiter role)

**Headers:**

```
Authorization: Bearer YOUR_ACCESS_TOKEN
Content-Type: application/json
```

**Request Body:**

```json
{
  "title": "Senior Python Developer",
  "description": "We are looking for an experienced Python developer...",
  "company_name": "Tech Company Inc",
  "requirements": "5+ years of Python experience, Django, REST APIs",
  "keywords": ["Python", "Django", "PostgreSQL", "REST API"],
  "location": "San Francisco, CA",
  "experience_required": "5+ years",
  "salary_min": 120000,
  "salary_max": 160000
}
```

**Request Parameters:**

- `title` (string, required): Job title
- `description` (string, required): Job description
- `company_name` (string, required): Company name
- `requirements` (string, optional): Job requirements
- `keywords` (array, required): List of required skills/keywords (used for matching)
- `location` (string, required): Job location
- `experience_required` (string, required): Experience level required
- `salary_min` (integer, optional): Minimum salary
- `salary_max` (integer, optional): Maximum salary

**Response (201 Created):**

```json
{
  "job_id": "550e8400-e29b-41d4-a716-446655440000",
  "title": "Senior Python Developer",
  "description": "We are looking for an experienced Python developer...",
  "company_name": "Tech Company Inc",
  "requirements": "5+ years of Python experience, Django, REST APIs",
  "keywords": ["Python", "Django", "PostgreSQL", "REST API"],
  "location": "San Francisco, CA",
  "experience_required": "5+ years",
  "salary_min": 120000,
  "salary_max": 160000,
  "is_active": true,
  "created_at": "2025-12-11T10:30:00Z",
  "applicant_count": 0
}
```

**Error Responses:**

- `400 Bad Request`: Invalid data (salary_min > salary_max, missing keywords, etc.)
- `401 Unauthorized`: Not authenticated
- `403 Forbidden`: User is not a recruiter

---

### 8. Get All Active Jobs

**Endpoint:** `GET /jobs/`

**Description:** Get list of all active job postings with filtering and pagination

**Permission:** Public (No authentication required)

**Query Parameters:**

- `search` (string, optional): Search in title, description, and keywords
- `location` (string, optional): Filter by location
- `exp` (integer, optional): Filter by experience required
- `min_salary` (integer, optional): Filter by minimum salary
- `max_salary` (integer, optional): Filter by maximum salary
- `page` (integer, optional): Page number (default: 1)

**Example Request:**

```
GET /jobs/?search=Python&location=San+Francisco&min_salary=100000
```

**Response (200 OK):**

```json
{
  "count": 25,
  "next": "http://localhost:8000/api/jobs/?page=2",
  "previous": null,
  "results": [
    {
      "job_id": "550e8400-e29b-41d4-a716-446655440000",
      "title": "Senior Python Developer",
      "description": "We are looking for an experienced Python developer...",
      "company_name": "Tech Company Inc",
      "requirements": "5+ years of Python experience",
      "location": "San Francisco, CA",
      "experience_required": "5+ years",
      "salary_min": 120000,
      "salary_max": 160000,
      "is_active": true,
      "created_at": "2025-12-11T10:30:00Z",
      "applicant_count": 5
    }
  ]
}
```

**Response Parameters:**

- `count`: Total number of jobs
- `next`: URL to next page
- `previous`: URL to previous page
- `results`: Array of job objects

**Error Responses:**

- `400 Bad Request`: Invalid query parameters

---

### 9. Get Job Details

**Endpoint:** `GET /jobs/{job_id}/`

**Description:** Get detailed information about a specific job

**Permission:** Public (No authentication required)

**Path Parameters:**

- `job_id` (UUID, required): The unique job ID

**Example Request:**

```
GET /jobs/550e8400-e29b-41d4-a716-446655440000/
```

**Response (200 OK):**

```json
{
  "job_id": "550e8400-e29b-41d4-a716-446655440000",
  "title": "Senior Python Developer",
  "description": "We are looking for an experienced Python developer...",
  "company_name": "Tech Company Inc",
  "requirements": "5+ years of Python experience",
  "keywords": ["Python", "Django", "PostgreSQL"],
  "location": "San Francisco, CA",
  "experience_required": "5+ years",
  "salary_min": 120000,
  "salary_max": 160000,
  "is_active": true,
  "created_at": "2025-12-11T10:30:00Z",
  "applicant_count": 5
}
```

**Error Responses:**

- `404 Not Found`: Job not found

---

### 10. Get My Posted Jobs (Recruiter)

**Endpoint:** `GET /jobs/me/`

**Description:** Get all jobs posted by the authenticated recruiter

**Permission:** IsAuthenticated + IsRecruiter

**Headers:**

```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

**Response (200 OK):**

```json
[
  {
    "job_id": "550e8400-e29b-41d4-a716-446655440000",
    "title": "Senior Python Developer",
    "description": "We are looking for an experienced Python developer...",
    "company_name": "Tech Company Inc",
    "keywords": ["Python", "Django", "PostgreSQL"],
    "location": "San Francisco, CA",
    "experience_required": "5+ years",
    "salary_min": 120000,
    "salary_max": 160000,
    "is_active": true,
    "created_at": "2025-12-11T10:30:00Z",
    "applicant_count": 5
  }
]
```

**Error Responses:**

- `401 Unauthorized`: Not authenticated
- `403 Forbidden`: User is not a recruiter

---

### 11. Update Job Posting

**Endpoint:** `PATCH /jobs/{job_id}/edit/`

**Description:** Update a job posting (Recruiters can only update their own jobs)

**Permission:** IsAuthenticated + IsRecruiter

**Headers:**

```
Authorization: Bearer YOUR_ACCESS_TOKEN
Content-Type: application/json
```

**Path Parameters:**

- `job_id` (UUID, required): The unique job ID

**Request Body (all fields optional):**

```json
{
  "title": "Senior Python Developer (Updated)",
  "description": "Updated description...",
  "salary_min": 130000,
  "salary_max": 170000,
  "keywords": ["Python", "Django", "PostgreSQL", "AWS"]
}
```

**Response (200 OK):**

```json
{
  "job_id": "550e8400-e29b-41d4-a716-446655440000",
  "title": "Senior Python Developer (Updated)",
  "description": "Updated description...",
  "company_name": "Tech Company Inc",
  "requirements": "5+ years of Python experience",
  "keywords": ["Python", "Django", "PostgreSQL", "AWS"],
  "location": "San Francisco, CA",
  "experience_required": "5+ years",
  "salary_min": 130000,
  "salary_max": 170000,
  "is_active": true,
  "created_at": "2025-12-11T10:30:00Z",
  "applicant_count": 5
}
```

**Error Responses:**

- `400 Bad Request`: Invalid data
- `401 Unauthorized`: Not authenticated
- `403 Forbidden`: Not the job owner
- `404 Not Found`: Job not found

---

### 12. Activate Job Posting

**Endpoint:** `PATCH /jobs/{job_id}/activate/`

**Description:** Activate a job posting to make it visible to applicants

**Permission:** IsAuthenticated + IsRecruiter

**Headers:**

```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

**Path Parameters:**

- `job_id` (UUID, required): The unique job ID

**Response (200 OK):**

```json
{
  "message": "Job activated"
}
```

**Error Responses:**

- `401 Unauthorized`: Not authenticated
- `403 Forbidden`: Not the job owner
- `404 Not Found`: Job not found

---

### 13. Deactivate Job Posting

**Endpoint:** `PATCH /jobs/{job_id}/deactivate/`

**Description:** Deactivate a job posting to hide it from applicants

**Permission:** IsAuthenticated + IsRecruiter

**Headers:**

```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

**Path Parameters:**

- `job_id` (UUID, required): The unique job ID

**Response (200 OK):**

```json
{
  "message": "Job Deactivated"
}
```

**Error Responses:**

- `401 Unauthorized`: Not authenticated
- `403 Forbidden`: Not the job owner
- `404 Not Found`: Job not found

---

## Applications

### 14. Apply to a Job

**Endpoint:** `POST /applications/{job_id}/apply/`

**Description:** Submit an application for a job with resume

**Permission:** IsAuthenticated + IsApplicant

**Headers:**

```
Authorization: Bearer YOUR_ACCESS_TOKEN
Content-Type: multipart/form-data
```

**Path Parameters:**

- `job_id` (UUID, required): The unique job ID

**Request Body:**

```
resume: [PDF File] (required)
```

**Form Parameters:**

- `resume` (file, required): PDF file of the resume

**Response (201 Created):**

```json
{
  "message": "Applied successfully",
  "match_score": 0.85,
  "application_id": 1,
  "resume_url": "https://supabase.example.com/storage/v1/object/public/resumes/user_123/job_id/resume.pdf"
}
```

**Response Parameters:**

- `message`: Success message
- `match_score`: Match score (0-1) calculated based on resume content and job keywords
- `application_id`: Unique application ID
- `resume_url`: URL to the uploaded resume

**Error Responses:**

- `400 Bad Request`:
  - Resume file not provided
  - Invalid job ID
  - Already applied to this job
- `401 Unauthorized`: Not authenticated
- `403 Forbidden`: User is not an applicant
- `404 Not Found`: Job not found or inactive
- `500 Internal Server Error`: Resume upload failed

---

### 15. Get Job Applicants

**Endpoint:** `GET /applications/{job_id}/applicants/`

**Description:** Get all applicants for a specific job (Recruiters only)

**Permission:** IsAuthenticated + IsRecruiter (Can only view applicants for own jobs)

**Headers:**

```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

**Path Parameters:**

- `job_id` (UUID, required): The unique job ID

**Example Request:**

```
GET /applications/550e8400-e29b-41d4-a716-446655440000/applicants/
```

**Response (200 OK):**

```json
{
  "job_id": "550e8400-e29b-41d4-a716-446655440000",
  "total_applicants": 3,
  "applicants": [
    {
      "id": 1,
      "user": 2,
      "job": "550e8400-e29b-41d4-a716-446655440000",
      "resume_file": "https://supabase.example.com/storage/v1/object/public/resumes/user_2/job_id/resume.pdf",
      "extracted_text": "John Doe\nPython Developer\n5 years experience...",
      "match_score": 0.92,
      "applied_at": "2025-12-11T09:30:00Z"
    },
    {
      "id": 2,
      "user": 3,
      "job": "550e8400-e29b-41d4-a716-446655440000",
      "resume_file": "https://supabase.example.com/storage/v1/object/public/resumes/user_3/job_id/resume.pdf",
      "extracted_text": "Jane Smith\nFull Stack Developer...",
      "match_score": 0.78,
      "applied_at": "2025-12-10T14:20:00Z"
    }
  ]
}
```

**Response Parameters:**

- `job_id`: The job ID
- `total_applicants`: Total number of applicants
- `applicants`: Array of applicants sorted by match_score (highest first)
  - `id`: Application ID
  - `user`: User ID of applicant
  - `job`: Job ID
  - `resume_file`: URL to uploaded resume
  - `extracted_text`: Text extracted from resume
  - `match_score`: Match score (0-1) between resume and job keywords
  - `applied_at`: Application submission timestamp

**Error Responses:**

- `401 Unauthorized`: Not authenticated
- `403 Forbidden`: Not the job owner
- `404 Not Found`: Job not found

---

## Error Handling

### Standard Error Responses

**400 Bad Request:**

```json
{
  "detail": "Invalid request data",
  "errors": {
    "field_name": ["Error message about this field"]
  }
}
```

**401 Unauthorized:**

```json
{
  "detail": "Authentication credentials were not provided."
}
```

**403 Forbidden:**

```json
{
  "detail": "You do not have permission to perform this action."
}
```

**404 Not Found:**

```json
{
  "detail": "Not found."
}
```

**500 Internal Server Error:**

```json
{
  "error": "An internal server error occurred"
}
```

---

## Authentication Header Format

All authenticated endpoints require the Authorization header in the following format:

```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

Replace `YOUR_ACCESS_TOKEN` with the `access` token received from the login endpoint.

---

## Rate Limiting

Currently, there are no rate limits applied. This may change in future versions.

---

## Pagination

List endpoints support pagination with the following query parameters:

- `page` (integer): Page number (default: 1)
- `page_size` (integer): Number of items per page (default: varies by endpoint)

**Response Format:**

```json
{
  "count": 100,
  "next": "http://localhost:8000/api/jobs/?page=2",
  "previous": null,
  "results": [...]
}
```

---

## CORS

The API supports Cross-Origin requests. Frontend applications can make requests from any origin.

---

## API Base URL Configuration

Update the base URL based on your environment:

- **Development:** `http://localhost:8000/api`
- **Production:** `https://yourdomain.com/api`

---

## User Roles

### Recruiter

- Can create, update, activate, and deactivate job postings
- Can view applicants for their jobs
- Cannot apply to jobs

### Applicant

- Can apply to jobs with resume
- Can view available jobs
- Cannot post or manage jobs

---

## Match Score Calculation

The match score is calculated by comparing the extracted text from the applicant's resume with the job's keywords. The score ranges from 0 to 1:

- **0.9 - 1.0**: Excellent match
- **0.7 - 0.9**: Good match
- **0.5 - 0.7**: Fair match
- **0.0 - 0.5**: Poor match

---

## File Uploads

### Resume Upload

- **Format:** PDF files only
- **Storage:** Supabase Storage
- **Max Size:** No specific limit enforced (configure based on needs)
- **Auto-generated URL:** Public URL is generated automatically after upload

---

## Version History

| Version | Date       | Changes             |
| ------- | ---------- | ------------------- |
| v1      | 2025-12-11 | Initial API release |

---

## Support

For issues or questions about the API, contact the backend development team.

---

## Last Updated

December 11, 2025

## New Update:


# 📘 User & Applicant APIs Documentation

This document describes the APIs used for:
- fetching the logged-in user profile
- fetching candidate details for recruiters
- listing applicants for a job

---

## 🔐 Authentication

All APIs require authentication.

### Headers
```http
Authorization: Bearer <access_token>

1️⃣ Get Logged-in User Profile (Me API)
Purpose
Returns the profile of the currently authenticated user.Used for:
Profile page
Settings
Dashboard user info

Endpoint
GET /me/

Permissions
Authenticated user (any role)

Response – 200 OK
{
  "id": 7,
  "username": "cand100",
  "email": "rahul@gmail.com",
  "role": "applicant",
  "full_name": "Rahul Sharma",
  "phone": "+91-9876543210",
  "linkedin_url": "https://linkedin.com/in/rahul",
  "github_url": "https://github.com/rahul",
  "about": "Frontend developer with 4+ years experience",
  "skills": ["React", "JavaScript", "HTML", "CSS"],
  "portfolio_url": "https://rahul.dev"
}

Error Responses


2️⃣ Get Candidate Profile by Username (Recruiter API)
Purpose
Returns the profile of a candidate (applicant).Used when a recruiter clicks on a candidate from the applicants list.

Endpoint
GET /candidates/{username}/

Permissions
Authenticated user

Path Parameters


Response – 200 OK
Response structure is exactly the same as /me/
{
  "id": 7,
  "username": "cand100",
  "email": "rahul@gmail.com",
  "role": "applicant",
  "full_name": "Rahul Sharma",
  "phone": "+91-9876543210",
  "linkedin_url": "https://linkedin.com/in/rahul",
  "github_url": "https://github.com/rahul",
  "about": "Frontend developer with 4+ years experience",
  "skills": ["React", "JavaScript", "HTML", "CSS"],
  "portfolio_url": "https://rahul.dev"
}

Error Responses


3️⃣ Job Applicants List (Recruiter View)
Purpose
Returns a summary list of candidates who applied for a specific job.Used for shortlisting and comparison.

Endpoint
GET /api/applications/{job_id}/applicants/

Permissions
Authenticated user
Role must be Recruiter
Recruiter must be the creator of the job

Path Parameters


Response – 200 OK
{
  "job_id": "bf6c11d5-6b78-4097-a854-936157f1fcb4",
  "total_applicants": 3,
  "applicants": [
    {
      "id": 13,
      "candidate": {
        "username": "cand100"
      },
      "match_score": 83.33,
      "resume_file": "https://.../cand100.pdf",
      "applied_at": "2025-12-14T16:44:22+05:30"
    }
  ]
}

Error Responses


🔄 Frontend API Flow
Recruiter opens job applicants page
Frontend calls:
GET /api/applications/{job_id}/applicants/
Recruiter clicks a candidate
Frontend calls:
GET /api/candidates/{username}/
Profile UI uses same layout as /me/

