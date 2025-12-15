import { ref } from 'vue'
import api from '@/api/axios'

export function useJobs() {
  // ---------------------------------------------------
  // GLOBAL STATE
  // ---------------------------------------------------
  const loading = ref(false)
  const error = ref(null)

  // ---------------------------------------------------
  // RECRUITER JOBS STATE
  // ---------------------------------------------------
  const jobs = ref([])

  /**
   * Fetch recruiter jobs
   * - Sorts active jobs first
   * - Then sorts by created_at (latest first)
   */
  const fetchRecruiterJobs = async () => {
    loading.value = true
    error.value = null

    try {
      const { data } = await api.get('/jobs/me/')

      jobs.value = data.sort((a, b) => {
        if (a.is_active === b.is_active) {
          return new Date(b.created_at) - new Date(a.created_at)
        }
        return b.is_active - a.is_active
      })
    } catch (err) {
      console.error(err)
      error.value = 'Failed to load jobs.'
    } finally {
      loading.value = false
    }
  }

  /**
   * Create Job
   */
  const createJob = async (jobData) => {
    loading.value = true
    error.value = null

    try {
      const { data } = await api.post('/jobs/create/', jobData)

      // Add new job on top
      jobs.value.unshift(data)

      return data
    } catch (err) {
      error.value = err.response?.data || 'Failed to create job.'
      throw err
    } finally {
      loading.value = false
    }
  }

  /**
   * Activate / Deactivate Job
   */
  const toggleJobStatus = async (job) => {
    try {
      const endpoint = job.is_active
        ? `/jobs/${job.job_id}/deactivate/`
        : `/jobs/${job.job_id}/activate/`

      await api.patch(endpoint)

      // Update local state immediately
      job.is_active = !job.is_active

      // Re-sort so inactive jobs move down
      jobs.value.sort((a, b) => b.is_active - a.is_active)
    } catch (err) {
      console.error(err)
      alert('Failed to update job status')
    }
  }

  /**
   * Delete Job
   */
  const deleteJob = async (jobId) => {
    if (!confirm("Are you sure? This will permanently delete this job.")) return

    try {
      // 👇 UPDATE THIS LINE to match your new API path:
      await api.delete(`/jobs/delete/${jobId}/`)
      
      // Remove from local list so it disappears from UI immediately
      jobs.value = jobs.value.filter(j => j.job_id !== jobId)
      
    } catch (err) {
      console.error(err)
      alert("Failed to delete job.")
    }
  }

  /**
   * Update Job (Edit Mode)
   */
  const updateJob = async (jobId, payload) => {
    loading.value = true
    error.value = null

    try {
      await api.patch(`/jobs/${jobId}/edit/`, payload)
    } catch (err) {
      console.error(err)
      error.value = 'Failed to update job'
      throw err
    } finally {
      loading.value = false
    }
  }

  // ---------------------------------------------------
  // PUBLIC JOB LISTING + PAGINATION
  // ---------------------------------------------------
  const publicJobs = ref([])
  const totalJobs = ref(0)
  const currentPage = ref(1)
  const totalPages = ref(0)

  const fetchPublicJobs = async (filters = {}, append = false) => {
    loading.value = true
    error.value = null

    try {
      const params = {
        search: filters.search || '',
        location: filters.location || '',
        page: filters.page || 1,
      }

      const { data } = await api.get('/jobs/', { params })

      if (append) {
        publicJobs.value = [...publicJobs.value, ...data.results]
      } else {
        publicJobs.value = data.results
      }

      totalJobs.value = data.total_results
      currentPage.value = data.current_page
      totalPages.value = data.total_pages
    } catch (err) {
      console.error(err)
      error.value = 'Failed to load jobs.'
      if (!append) publicJobs.value = []
    } finally {
      loading.value = false
    }
  }

  // ---------------------------------------------------
  // SINGLE JOB DETAIL
  // ---------------------------------------------------
  const currentJob = ref(null)

  const fetchJobById = async (id) => {
    loading.value = true
    currentJob.value = null

    try {
      const { data } = await api.get(`/jobs/${id}/`)
      currentJob.value = data
    } catch (err) {
      console.error(err)
      error.value = 'Failed to load job details'
    } finally {
      loading.value = false
    }
  }

  // ---------------------------------------------------
  // EXPORT
  // ---------------------------------------------------
  return {
    // State
    loading,
    error,

    // Recruiter Jobs
    jobs,
    fetchRecruiterJobs,
    createJob,
    toggleJobStatus,
    deleteJob,
    updateJob,

    // Public Jobs
    publicJobs,
    totalJobs,
    currentPage,
    totalPages,
    fetchPublicJobs,

    // Single Job
    currentJob,
    fetchJobById,
  }
}
