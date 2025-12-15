# Hyro - Job Portal Frontend Documentation

## 📋 Table of Contents

1. [Project Overview](#project-overview)
2. [Technology Stack](#technology-stack)
3. [Project Structure](#project-structure)
4. [Getting Started](#getting-started)
5. [Core Features](#core-features)
6. [Composables](#composables)
7. [Stores (State Management)](#stores-state-management)
8. [Views](#views)
9. [Components](#components)
10. [Routing & Navigation](#routing--navigation)
11. [API Integration](#api-integration)
12. [Authentication Flow](#authentication-flow)
13. [Styling & UI](#styling--ui)
14. [Development Guidelines](#development-guidelines)

---

## Project Overview

**Hyro** is a modern, full-featured job portal application that connects job seekers (applicants) with recruiters. The platform provides a seamless experience for both user types with role-based access control, job posting, application management, and intelligent job matching.

### Key Capabilities

- **For Applicants:**
  - Browse and search jobs with filtering
  - Apply to jobs with resume upload
  - Track application status
  - Manage profile and skills
  - View job details and match scores

- **For Recruiters:**
  - Create and manage job postings
  - View applicants for posted jobs
  - Activate/deactivate job listings
  - Dashboard with job statistics

### Backend API

- **Base URL:** `http://localhost:8000/`
- **API Documentation:** See `BackendAPI.md` for complete endpoint documentation
- **Authentication:** JWT-based (access & refresh tokens)

---

## Technology Stack

### Core Framework
- **Vue 3** (v3.5.25) - Progressive JavaScript framework with Composition API
- **Vite** (v7.2.4) - Next-generation frontend build tool
- **Vue Router** (v4.6.3) - Official router for Vue.js

### State Management
- **Pinia** (v3.0.4) - Official state management library for Vue

### HTTP Client
- **Axios** (v1.13.2) - Promise-based HTTP client for API requests

### Styling
- **Tailwind CSS** (v4.1.17) - Utility-first CSS framework
- **Lucide Vue Next** (v0.556.0) - Beautiful icon library

### Development Tools
- **ESLint** - Code linting
- **Prettier** - Code formatting
- **Vue DevTools** - Vue debugging extension

---

## Project Structure

```
Frontend/
├── public/                    # Static assets
│   ├── favicon.ico
│   └── svgs/                  # SVG assets
├── src/
│   ├── api/                   # API configuration
│   │   └── axios.js          # Axios instance with interceptors
│   ├── components/            # Reusable Vue components
│   │   ├── Landing.vue       # Landing page component
│   │   └── ui/               # UI component library
│   ├── composables/          # Composition API composables
│   │   ├── useAuth.js        # Authentication composable (legacy)
│   │   ├── useApplications.js # Application management
│   │   └── useJobs.js        # Job management
│   ├── layouts/              # Layout components
│   │   └── DashboardLayout2.vue  # Main dashboard layout
│   ├── router/               # Vue Router configuration
│   │   └── index.js          # Routes and navigation guards
│   ├── stores/               # Pinia stores
│   │   ├── auth.js           # Authentication store
│   │   └── counter.js        # Example store (can be removed)
│   ├── views/                # Page components
│   │   ├── applicant/        # Applicant-specific views
│   │   ├── auth/             # Authentication views
│   │   ├── recruiter/        # Recruiter-specific views
│   │   ├── HomeView.vue      # Public landing page
│   │   └── testingComponent.vue  # Testing/development component
│   ├── assests/              # Assets (note: typo in folder name)
│   │   └── main.css          # Global styles
│   ├── App.vue               # Root component
│   └── main.js               # Application entry point
├── BackendAPI.md             # Backend API documentation
├── frontend.md               # This documentation file
├── package.json              # Dependencies and scripts
├── vite.config.js            # Vite configuration
└── eslint.config.js          # ESLint configuration
```

---

## Getting Started

### Prerequisites

- **Node.js:** ^20.19.0 || >=22.12.0
- **npm** or **yarn** package manager
- Backend API server running on `http://localhost:8000/`

### Installation

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Lint code
npm run lint

# Format code
npm run format
```

### Development Server

The development server typically runs on `http://localhost:5173` (Vite default port).

---

## Core Features

### 1. Authentication System
- User registration (Applicant/Recruiter roles)
- JWT-based login with token refresh
- Protected routes with role-based access
- Session persistence on page refresh
- Automatic token attachment to API requests

### 2. Job Management
- **Public Job Listing:** Browse all active jobs with pagination
- **Search & Filter:** Filter by location, salary, experience
- **Job Details:** View complete job information
- **Recruiter Jobs:** Manage posted jobs (create, activate, deactivate)

### 3. Application System
- **Apply to Jobs:** Submit applications with PDF resume
- **Application Tracking:** View all submitted applications
- **Match Score:** AI-powered resume-to-job matching

### 4. User Profiles
- **Profile Management:** Update personal information, skills, social links
- **Role-based Dashboards:** Different views for applicants and recruiters

### 5. Responsive Design
- Mobile-first approach
- Responsive navigation with mobile menu
- Touch-friendly interactions

---

## Composables

Composables are reusable Composition API functions that encapsulate logic and state.

### `useJobs.js`

Manages all job-related operations and state.

**State:**
- `jobs` - Array of recruiter's posted jobs
- `publicJobs` - Array of public job listings
- `currentJob` - Currently viewed job details
- `loading` - Loading state
- `error` - Error messages
- `totalJobs`, `currentPage`, `totalPages` - Pagination data

**Methods:**
- `fetchRecruiterJobs()` - Get all jobs posted by authenticated recruiter
- `createJob(jobData)` - Create a new job posting
- `fetchPublicJobs(filters, append)` - Fetch public jobs with optional filters and pagination
- `fetchJobById(id)` - Get detailed information about a specific job

**Usage:**
```javascript
import { useJobs } from '@/composables/useJobs'

const { publicJobs, fetchPublicJobs, loading } = useJobs()
await fetchPublicJobs({ search: 'Python', location: 'San Francisco' })
```

### `useApplications.js`

Manages job application operations.

**State:**
- `applications` - Array of user's applications
- `loading` - Loading state
- `error` - Error messages

**Methods:**
- `fetchMyApplications()` - Get all applications submitted by the authenticated user

**Usage:**
```javascript
import { useApplications } from '@/composables/useApplications'

const { applications, fetchMyApplications, loading } = useApplications()
await fetchMyApplications()
```

### `useAuth.js` (Legacy)

⚠️ **Note:** This composable is present but not actively used. The application uses Pinia store (`useAuthStore`) for authentication instead.

---

## Stores (State Management)

### `auth.js` - Authentication Store

Central store for authentication state and operations.

**State:**
- `user` - Current authenticated user object
- `token` - JWT access token
- `initialized` - Flag to track if auth has been restored

**Computed Properties:**
- `isAuthenticated` - Boolean indicating if user is logged in
- `isRecruiter` - Boolean indicating if user has recruiter role
- `isApplicant` - Boolean indicating if user has applicant role

**Actions:**
- `restoreAuth()` - Restore authentication state from localStorage on app load
- `login(credentials)` - Authenticate user and store tokens
- `signup(userData)` - Register new user account
- `fetchUser()` - Get current user profile from API
- `logout()` - Clear authentication and redirect to login

**Usage:**
```javascript
import { useAuthStore } from '@/stores/auth'

const authStore = useAuthStore()

// Login
await authStore.login({ username: 'user', password: 'pass' })

// Check role
if (authStore.isRecruiter) {
  // Recruiter-specific logic
}
```

---

## Views

Views are page-level components that represent different routes in the application.

### Public Views

#### `HomeView.vue`
- **Route:** `/`
- **Description:** Public landing page with hero section, features, and call-to-action
- **Features:**
  - Animated hero section with floating elements
  - "Why Hyro" feature showcase
  - Separate sections for applicants and recruiters
  - Footer with links and social media

### Authentication Views

#### `LoginView.vue`
- **Route:** `/login`
- **Description:** User login page
- **Features:**
  - Split-screen design with gradient background
  - Username/password form
  - Error handling and display
  - Redirects to appropriate dashboard based on role

#### `SignupView.vue`
- **Route:** `/signup`
- **Description:** User registration page
- **Features:**
  - Role selection (Applicant/Recruiter) with visual toggle
  - Form fields: full name, username, email, phone, password
  - Dynamic UI that changes based on selected role
  - Error handling for duplicate users

### Applicant Views

All applicant views are nested under `/applicant` route and use `DashboardLayout2.vue`.

#### `ApplicantDashboard.vue`
- **Route:** `/applicant/dashboard`
- **Description:** Main dashboard for applicants
- **Features:**
  - Personalized welcome message
  - Preview of 4 featured jobs
  - Link to browse more jobs
  - Loading and empty states

#### `JobsView.vue`
- **Route:** `/applicant/jobsView`
- **Description:** Full job listing page with search and filters
- **Features:**
  - Paginated job listings
  - Search and filter functionality
  - Load more functionality

#### `JobDetails.vue`
- **Route:** `/applicant/jobs/:id`
- **Description:** Detailed view of a single job
- **Features:**
  - Complete job information
  - Application form with resume upload
  - Match score display

#### `JobViewCard.vue`
- **Description:** Reusable card component for displaying job previews
- **Props:**
  - `job` (Object, required) - Job object with title, company, location, salary
- **Features:**
  - Clickable card that navigates to job details
  - Hover effects and animations
  - Displays key job information

#### `MyApplications.vue`
- **Route:** `/applicant/my-applications`
- **Description:** List of all applications submitted by the user
- **Features:**
  - Application history
  - Status tracking
  - Resume links

#### `ProfileView.vue`
- **Route:** `/applicant/profile`
- **Description:** User profile management page
- **Features:**
  - Edit personal information
  - Update skills, bio, social links
  - Profile picture management

#### `DashboardView.vue` (Applicant)
- **Note:** This file appears to be misnamed - it contains job card component code rather than a full dashboard view.

### Recruiter Views

All recruiter views are nested under `/recruiter` route and use `DashboardLayout2.vue`.

#### `DashboardView.vue` (Recruiter)
- **Route:** `/recruiter/dashboard`
- **Description:** Main dashboard for recruiters
- **Features:**
  - Statistics and metrics
  - List of posted jobs
  - Quick actions

#### `CreateJob.vue`
- **Route:** `/recruiter/create-job`
- **Description:** Form to create new job postings
- **Features:**
  - Job title, company, location
  - Description and requirements
  - Keywords/tags
  - Salary range
  - Experience level

---

## Components

### `Landing.vue`
- **Location:** `src/components/Landing.vue`
- **Description:** Landing page component (appears to be an older version, currently unused)
- **Note:** The actual landing page is implemented in `HomeView.vue`

### UI Components
- **Location:** `src/components/ui/`
- **Description:** Reusable UI component library
- **Note:** Directory exists but specific components need to be documented based on actual files

---

## Routing & Navigation

### Router Configuration (`src/router/index.js`)

The router uses Vue Router 4 with the following structure:

#### Public Routes
- `/` - HomeView (public landing page)
- `/login` - LoginView
- `/signup` - SignupView

#### Protected Routes - Applicant
All routes under `/applicant` require:
- Authentication (`requiresAuth: true`)
- Applicant role (`role: 'applicant'`)

Routes:
- `/applicant/dashboard` - ApplicantDashboard
- `/applicant/jobs/:id` - JobDetails
- `/applicant/jobsView` - JobsView
- `/applicant/profile` - ProfileView
- `/applicant/my-applications` - MyApplications

#### Protected Routes - Recruiter
All routes under `/recruiter` require:
- Authentication (`requiresAuth: true`)
- Recruiter role (`role: 'recruiter'`)

Routes:
- `/recruiter/dashboard` - Recruiter DashboardView
- `/recruiter/create-job` - CreateJob

### Navigation Guards

The router implements a `beforeEach` guard that:

1. **Restores Authentication:**
   - Checks if auth is initialized
   - If token exists in localStorage, attempts to restore user session
   - Fetches user profile from `/auth/me/`

2. **Protects Routes:**
   - Redirects unauthenticated users to `/login` for protected routes
   - Redirects applicants trying to access recruiter routes to applicant dashboard
   - Redirects recruiters trying to access applicant routes to recruiter dashboard

3. **Role-Based Access:**
   - Validates user role matches route requirements
   - Prevents cross-role access

### Layout System

- **DashboardLayout2.vue:** Used for all authenticated routes
  - Sidebar navigation with role-specific menu items
  - User profile section
  - Logout functionality
  - Responsive mobile menu
  - Main content area with RouterView

---

## API Integration

### Axios Configuration (`src/api/axios.js`)

**Base Configuration:**
- Base URL: `http://localhost:8000/`
- Default headers: `Content-Type: application/json`

**Request Interceptor:**
- Automatically attaches JWT token from localStorage to all requests
- Token format: `Authorization: Bearer {access_token}`

**Usage:**
```javascript
import api from '@/api/axios'

// GET request
const { data } = await api.get('/jobs/')

// POST request
const { data } = await api.post('/jobs/create/', jobData)

// Request with token (automatically attached)
const { data } = await api.get('/auth/me/')
```

### API Endpoints Used

#### Authentication
- `POST /auth/signup/` - User registration
- `POST /auth/login/` - User login
- `GET /auth/me/` - Get current user profile
- `PATCH /auth/me/update/` - Update user profile

#### Jobs
- `GET /jobs/` - Get all active jobs (public, with pagination)
- `GET /jobs/{id}/` - Get job details
- `GET /jobs/me/` - Get recruiter's posted jobs
- `POST /jobs/create/` - Create new job (recruiter only)
- `PATCH /jobs/{id}/edit/` - Update job (recruiter only)
- `PATCH /jobs/{id}/activate/` - Activate job (recruiter only)
- `PATCH /jobs/{id}/deactivate/` - Deactivate job (recruiter only)

#### Applications
- `POST /applications/{job_id}/apply/` - Apply to a job (applicant only)
- `GET /applications/my-applications/` - Get user's applications (applicant only)
- `GET /applications/{job_id}/applicants/` - Get job applicants (recruiter only)

For complete API documentation, see `BackendAPI.md`.

---

## Authentication Flow

### Registration Flow

1. User fills signup form with role selection
2. Form data sent to `POST /auth/signup/`
3. On success, redirect to `/login`
4. User can then log in with credentials

### Login Flow

1. User enters username and password
2. Credentials sent to `POST /auth/login/`
3. Backend returns `access` and `refresh` tokens
4. Tokens stored in localStorage:
   - `access_token` - Short-lived token for API requests
   - `refresh_token` - Long-lived token for refreshing access token
5. User profile fetched from `GET /auth/me/`
6. User redirected to role-specific dashboard:
   - Applicants → `/applicant/dashboard`
   - Recruiters → `/recruiter/dashboard`

### Session Restoration

On app load/refresh:
1. Router guard checks if auth is initialized
2. If token exists in localStorage:
   - Token attached to axios headers
   - User profile fetched from `/auth/me/`
   - User state restored in Pinia store
3. If token is invalid:
   - Tokens cleared from localStorage
   - User redirected to login

### Logout Flow

1. Clear tokens from localStorage
2. Clear user state in Pinia store
3. Remove Authorization header from axios
4. Redirect to `/login`

---

## Styling & UI

### Tailwind CSS

The project uses Tailwind CSS 4 for styling with a utility-first approach.

**Key Design Elements:**
- **Color Scheme:**
  - Primary: Orange (`orange-500`, `orange-600`)
  - Secondary: Slate/Gray (`slate-50` to `slate-900`)
  - Accent: Blue for applicants, Orange for recruiters
- **Typography:** Sans-serif with various font weights
- **Spacing:** Consistent spacing scale using Tailwind's spacing utilities
- **Border Radius:** Rounded corners (`rounded-xl`, `rounded-2xl`, `rounded-[2rem]`)

### Responsive Design

- **Mobile-first:** Base styles for mobile, enhanced for larger screens
- **Breakpoints:**
  - `sm:` - 640px and up
  - `md:` - 768px and up
  - `lg:` - 1024px and up

### Icons

- **Lucide Vue Next:** Modern icon library
- Icons used throughout for navigation, actions, and visual elements

### Animations

- Custom CSS animations for floating elements
- Vue transitions for route changes and component updates
- Hover effects and transitions on interactive elements

---

## Development Guidelines

### Code Style

- **ESLint:** Configured for Vue 3 and JavaScript
- **Prettier:** Code formatting
- **Composition API:** Preferred over Options API
- **Script Setup:** Use `<script setup>` syntax

### File Naming

- **Components:** PascalCase (e.g., `JobViewCard.vue`)
- **Composables:** camelCase with `use` prefix (e.g., `useJobs.js`)
- **Stores:** camelCase (e.g., `auth.js`)
- **Views:** PascalCase (e.g., `ApplicantDashboard.vue`)

### State Management

- Use **Pinia stores** for global state (authentication, user data)
- Use **composables** for reusable component logic
- Use **local state** (ref/reactive) for component-specific state

### API Calls

- Always use the configured axios instance from `@/api/axios`
- Handle loading and error states
- Use try-catch blocks for error handling
- Display user-friendly error messages

### Routing

- Use named routes for navigation
- Protect routes with appropriate meta fields
- Use router guards for authentication checks

### Component Structure

```vue
<script setup>
// 1. Imports
// 2. Props/Emits
// 3. Composables/Stores
// 4. Reactive state
// 5. Computed properties
// 6. Methods
// 7. Lifecycle hooks
</script>

<template>
  <!-- Template content -->
</template>

<style scoped>
/* Component-specific styles */
</style>
```

### Best Practices

1. **Composition API:** Prefer Composition API over Options API
2. **TypeScript:** Consider migrating to TypeScript for better type safety
3. **Error Handling:** Always handle API errors gracefully
4. **Loading States:** Show loading indicators during async operations
5. **Accessibility:** Use semantic HTML and ARIA attributes
6. **Performance:** Lazy load routes and components when possible
7. **Code Splitting:** Use dynamic imports for route components

---

## Known Issues & Notes

1. **Folder Typo:** `assests/` should be `assets/` (typo in folder name)
2. **Legacy Code:** `useAuth.js` composable exists but is not used (Pinia store is used instead)
3. **Testing Component:** `testingComponent.vue` contains profile editing code that may need to be integrated
4. **Empty Components:** Some component files may be placeholders
5. **DashboardView Naming:** Applicant's `DashboardView.vue` appears to be misnamed (contains job card code)

---

## Future Enhancements

### Potential Features
- Resume upload and management
- Advanced job search with multiple filters
- Saved jobs/bookmarks
- Email notifications
- Real-time application status updates
- Recruiter analytics dashboard
- Candidate ranking and filtering
- Interview scheduling
- Messaging system between applicants and recruiters

### Technical Improvements
- Migrate to TypeScript
- Add unit and integration tests
- Implement error boundary components
- Add loading skeletons
- Optimize bundle size
- Implement service worker for offline support
- Add internationalization (i18n)
- Improve accessibility (a11y)

---

## Support & Resources

- **Vue 3 Documentation:** https://vuejs.org/
- **Vite Documentation:** https://vite.dev/
- **Pinia Documentation:** https://pinia.vuejs.org/
- **Vue Router Documentation:** https://router.vuejs.org/
- **Tailwind CSS Documentation:** https://tailwindcss.com/
- **Axios Documentation:** https://axios-http.com/

---

## Last Updated

December 2025

---

## Contributors

Documentation maintained by the development team. For questions or contributions, please refer to the project repository.
