import { ref } from 'vue'
import api from '@/api/axios'

export function useApplications() {
  const applications = ref([])
  const loading = ref(false)
  const error = ref(null)

  // FETCH APPLIED JOBS
  // Endpoint: GET /applications/my-applications/
  const fetchMyApplications = async () => {
    loading.value = true
    error.value = null
    try {
      const { data } = await api.get('/applications/my-applications/')
      // The API returns { message, total_applications, applications: [...] }
      applications.value = data.applications
    } catch (err) {
      console.error('Failed to fetch applications', err)
      error.value = 'Could not load applications.'
    } finally {
      loading.value = false
    }
  }

  return {
    applications,
    loading,
    error,
    fetchMyApplications,
  }
}
