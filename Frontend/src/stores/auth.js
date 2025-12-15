import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import api from '@/api/axios'
import { useRouter } from 'vue-router'

export const useAuthStore = defineStore('auth', () => {
  const user = ref(null)
  const token = ref(localStorage.getItem('access_token') || null)

  // ⭐ This flag ensures router guards wait for auth to load
  const initialized = ref(false)

  const router = useRouter()

  // --- COMPUTED STATES ---
  const isAuthenticated = computed(() => !!token.value)
  const isRecruiter = computed(() => user.value?.role === 'recruiter')
  const isApplicant = computed(() => user.value?.role === 'applicant')

  // ---------------------------------------------------------
  // ⭐ RESTORE AUTH (Runs on refresh BEFORE router guard)
  // ---------------------------------------------------------
  const restoreAuth = async () => {
    // Avoid running twice
    if (initialized.value) return

    // If token exists, try to fetch user
    if (token.value) {
      try {
        const { data } = await api.get('/auth/me/')
        user.value = data

        // Attach token to axios headers
        api.defaults.headers.common['Authorization'] = `Bearer ${token.value}`
      } catch (err) {
        console.error('Failed to restore session:', err)

        // Token invalid → wipe everything
        token.value = null
        user.value = null
        localStorage.removeItem('access_token')
        localStorage.removeItem('refresh_token')
      }
    }

    initialized.value = true
  }

  // ---------------------------------------------------------
  //  LOGIN
  // ---------------------------------------------------------
  const login = async (credentials) => {
    try {
      const { data } = await api.post('/auth/login/', credentials)

      token.value = data.access
      localStorage.setItem('access_token', data.access)
      localStorage.setItem('refresh_token', data.refresh)

      api.defaults.headers.common['Authorization'] = `Bearer ${data.access}`

      await fetchUser()
      return true
    } catch (error) {
      console.error('Login failed:', error.response?.data)
      throw error
    }
  }

  // ---------------------------------------------------------
  // FETCH USER DETAILS
  // ---------------------------------------------------------
  const fetchUser = async () => {
    if (!token.value) return

    try {
      const { data } = await api.get('/auth/me/')
      user.value = data
    } catch (err) {
      console.error('Failed to fetch user:', err)
      logout() // ✔ no more VS code error
    }
  }

  // ---------------------------------------------------------
  // SIGNUP
  // ---------------------------------------------------------
  const signup = async (userData) => {
    try {
      // Build payload EXACTLY as backend expects
      const payload = {
        full_name: userData.full_name,
        username: userData.username,
        email: userData.email,
        phone: userData.phone,
        password: userData.password,
        role: userData.role,
      }

      const { data } = await api.post('/auth/signup/', payload)

      return data // your API may return success message or user object
    } catch (error) {
      const backendError = error.response?.data

      console.error('Signup failed:', backendError || error)

      // Throw readable error so UI can show messages
      throw backendError || { message: 'Signup failed. Please try again.' }
    }
  }

  // ---------------------------------------------------------
  // LOGOUT
  // ---------------------------------------------------------
  const logout = () => {
    token.value = null
    user.value = null
    localStorage.removeItem('access_token')
    localStorage.removeItem('refresh_token')
    router.push('/login')
  }

  // ---------------------------------------------------------
  // EXPORT EVERYTHING
  // ---------------------------------------------------------
  return {
    // state
    user,
    token,
    initialized,

    // computed getters
    isAuthenticated,
    isRecruiter,
    isApplicant,

    // actions
    login,
    restoreAuth,
    fetchUser,
    signup,
    logout,
  }
})
