import { ref } from 'vue'
import api from '@/api/axios'

export function useRecruiter() {
  const applicants = ref([])
  const currentCandidateProfile = ref(null)
  const loading = ref(false)
  const profileLoading = ref(false)
  const error = ref(null)

  // 1. FETCH APPLICANTS LIST (Thin Data)
  // Endpoint: GET /api/applications/{job_id}/applicants/
  const fetchApplicants = async (jobId) => {
    loading.value = true
    error.value = null
    try {
      // Note: Added /api/ prefix as per your doc flow, remove if baseURL handles it
      const { data } = await api.get(`/applications/${jobId}/applicants/`)

      // Map response to add local UI state
      applicants.value = data.applicants.map((app) => ({
        ...app,
        isIgnored: false,
      }))
    } catch (err) {
      console.error(err)
      error.value = 'Failed to load applicants.'
    } finally {
      loading.value = false
    }
  }

  // 2. FETCH FULL PROFILE (Rich Data)
  // Endpoint: GET /candidates/{username}/
  const fetchCandidateProfile = async (username) => {
    profileLoading.value = true
    currentCandidateProfile.value = null
    try {
      // FIX: Add 'accounts/' (or your specific api prefix) before candidates
      // Also ensure 'api' base URL is pointing to your Django server (e.g., localhost:8000)
      const { data } = await api.get(`/accounts/candidates/${username}/`) 
      currentCandidateProfile.value = data
    } catch (err) {
      console.error('Failed to load profile', err)
    } finally {
      profileLoading.value = false
    }
}

  return {
    applicants,
    currentCandidateProfile,
    loading,
    profileLoading,
    error,
    fetchApplicants,
    fetchCandidateProfile,
  }
}
