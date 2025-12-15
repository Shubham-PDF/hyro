# Hyro – AI-Assisted Hiring Platform

Hyro connects recruiters with the right applicants through AI-powered resume-to-job matching, streamlined job management, and a clean Vue-powered experience. The project ships with a Django REST backend, a Vue 3 + Vite frontend, and a Supabase-hosted Postgres + storage layer.

## What’s inside
- **Recruiter tools:** post jobs, activate/deactivate listings, view applicants, and see match scores.
- **Applicant journey:** browse and filter jobs, view details, upload resumes, track applications.
- **AI matching:** resume text is analyzed against job keywords to surface match scores.
- **Role-aware UX:** separate dashboards, navigation, and guards for applicants vs. recruiters.

## Tech stack
- **Frontend:** Vue 3, Vite, Pinia, Vue Router, Tailwind CSS, Axios.
- **Backend:** Django REST Framework, JWT auth, custom roles/permissions.
- **Data & storage:** Supabase Postgres and Supabase Storage for resumes.

## Repository layout
- `Frontend/` – Vue app (see `Frontend/frontend.md` for deep dive).
- `Backend/` – Django project and API (see `Backend/backendAPI.md` for endpoints).

## Prerequisites
- Node.js ≥ 20.19.0 (or 22.x) and npm.
- Python 3.13+ and `pip`.
- Supabase project credentials (URL, anon/service keys, bucket name) if you want to run full resume upload flows.

## Running the backend (Django)
1. `cd Backend`
2. Create and activate a virtualenv (optional but recommended).
3. Install dependencies: `pip install -r requirements.txt`
4. Configure environment (example):
   - `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`
   - Database connection (e.g., `DATABASE_URL` for Supabase Postgres)
   - Supabase storage: `SUPABASE_URL`, `SUPABASE_KEY`, `SUPABASE_BUCKET`
5. Apply migrations: `python manage.py migrate`
6. Run the server: `python manage.py runserver` (defaults to `http://localhost:8000/`)

## Running the frontend (Vue + Vite)
1. `cd Frontend`
2. Install dependencies: `npm install`
3. Start dev server: `npm run dev` (defaults to `http://localhost:5173/`)
4. Point API calls to the backend:
   - Dev: `http://localhost:8000/` (or `/api` if proxied)
   - Prod: update the base URL in `src/api/axios.js`

## Building for production
- Frontend: from `Frontend/`, run `npm run build` to produce the optimized Vite build (output in `dist/`). Preview locally with `npm run preview`.
- Backend: ensure `DEBUG=0`, set `ALLOWED_HOSTS`, configure your production database and storage, run migrations, then serve via a WSGI server (e.g., gunicorn/uvicorn behind nginx).

## Notable backend endpoints
Key routes (full list in `Backend/backendAPI.md`):
- Auth: `POST /auth/signup/`, `POST /auth/login/`, `POST /auth/refresh/`, `GET /auth/me/`, `PATCH /auth/me/update/`
- Jobs: `GET /jobs/`, `GET /jobs/{id}/`, `POST /jobs/create/`, `PATCH /jobs/{id}/edit/`, `PATCH /jobs/{id}/activate/`, `PATCH /jobs/{id}/deactivate/`
- Applications: `POST /applications/{job_id}/apply/`, `GET /applications/my-applications/`, `GET /applications/{job_id}/applicants/`
- Dashboards: `GET /dashboard/recruiter/summary/`, `GET /dashboard/applicant/applications/`

## Notes and tips
- The frontend uses Pinia for auth/session state; tokens are attached via Axios interceptors.
- If you see the `assests/` folder in the frontend, it is a known typo and can be renamed to `assets/` when convenient.
- Supabase handles resume storage; ensure bucket permissions align with your deployment plan.

## License and support
Created by the Hyro team. For issues or questions, open a ticket or reach out to the maintainers. See module-specific docs in `Frontend/frontend.md` and `Backend/backendAPI.md` for deeper details.

