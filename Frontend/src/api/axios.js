import axios from 'axios'

const api = axios.create({
  // We will update this base URL once you share the Django docs
  baseURL: 'https://hyro-diel.onrender.com/',
  headers: {
    'Content-Type': 'application/json',
  },
})

// Interceptor: Attach Token to every request
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('access_token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

export default api
