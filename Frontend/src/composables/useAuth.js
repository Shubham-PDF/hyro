import { ref, computed } from 'vue'
import axios from 'axios'

const token = ref(localStorage.getItem('token') || null)
const user = ref(JSON.parse(localStorage.getItem('user') || 'null'))

export function useAuth() {
  const isAuthenticated = computed(() => !!token.value)
  const role = computed(() => user.value?.role || null)

  async function login(email, password) {
    // Replace URL with your backend login endpoint
    const res = await axios.post('/api/auth/login/', { email, password })
    token.value = res.data.token
    user.value = res.data.user
    localStorage.setItem('token', token.value)
    localStorage.setItem('user', JSON.stringify(user.value))
    axios.defaults.headers.common['Authorization'] = `Bearer ${token.value}`
  }

  function logout() {
    token.value = null
    user.value = null
    localStorage.removeItem('token')
    localStorage.removeItem('user')
    delete axios.defaults.headers.common['Authorization']
  }

  // helpers for router file
  function getToken() {
    return token.value
  }
  function getRole() {
    return role.value
  }

  return { token, user, isAuthenticated, role, login, logout, getToken, getRole }
}
