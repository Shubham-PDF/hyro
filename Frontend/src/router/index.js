import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import { useAuthStore } from '@/stores/auth'
import DashboardLayout from '@/layouts/DashboardLayout2.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/auth/LoginView.vue'),
    },
    {
      path: '/signup',
      name: 'signup',
      component: () => import('../views/auth/SignupView.vue'),
    },
    {
      path: '/test',
      name: 'test',
      component: () => import('../views/testingComponent.vue'),
    },

    // 🔒 APPLICANT ROUTES
    {
      path: '/applicant',
      component: DashboardLayout,
      meta: { requiresAuth: true, role: 'applicant' },
      children: [
        {
          path: 'dashboard',
          name: 'applicant-dashboard',
          component: () => import('../views/applicant/ApplicantDashboard.vue'),
        },
        {
          path: 'jobs/:id',
          name: 'job-details',
          component: () => import('../views/applicant/JobDetails.vue'),
        },
        {
          path: 'jobsView',
          name: 'jobs-view',
          component: () => import('../views/applicant/JobsView.vue'),
        },
        {
          path: 'profile',
          name: 'applicant-profile',
          component: () => import('../views/applicant/ProfileView.vue'),
        },
        {
          path: 'my-applications',
          name: 'my-applications',
          component: () => import('../views/applicant/MyApplications.vue'),
        },
      ],
    },

    // 🔒 RECRUITER ROUTES
    {
      path: '/recruiter',
      component: DashboardLayout,
      meta: { requiresAuth: true, role: 'recruiter' },
      children: [
        {
          path: 'dashboard',
          name: 'recruiter-dashboard',
          component: () => import('../views/recruiter/DashboardView.vue'),
        },
        {
          path: 'create-job',
          name: 'create-job',
          component: () => import('../views/recruiter/CreateJob.vue'),
        },
        {
          path: 'profile',
          name: 'recruiter-profile',
          component: () => import('../views/recruiter/ProfileViewRecruiter.vue'),
        },
        {
          path: 'jobs',
          name: 'jobs',
          component: () => import('../views/recruiter/ManageJobs.vue'),
        },
        {
          path: 'jobs/:id/candidates',
          name: 'job-applicants',
          component: () => import('../views/recruiter/JobApplicants.vue'),
        },
        {
          path: 'candidates/:username',
          name: 'candidate-profile',
          component: () => import('../views/recruiter/CandidateProfile.vue'),
        },
        {
          path: 'jobs/:id/edit', 
          name: 'edit-job', 
          component: () => import('../views/recruiter/CreateJob.vue') 
        },
      ],
    },
  ],
})

// THE GUARD: This runs on every route change
router.beforeEach(async (to, from, next) => {
  const authStore = useAuthStore()

  // Ensure user/token are restored BEFORE guarding routes
  if (!authStore.initialized) {
    await authStore.restoreAuth()
  }

  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    return next({ name: 'login' })
  }

  if (to.meta.role) {
    if (to.meta.role === 'recruiter' && !authStore.isRecruiter) {
      return next({ name: 'applicant-dashboard' })
    }
    if (to.meta.role === 'applicant' && !authStore.isApplicant) {
      return next({ name: 'recruiter-dashboard' })
    }
  }

  next()
})

export default router
