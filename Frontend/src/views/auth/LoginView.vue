<script setup>
import { reactive, ref } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useRouter } from 'vue-router'
import { LogIn, Lock, ArrowRight } from 'lucide-vue-next'

const authStore = useAuthStore()
const router = useRouter()

const form = reactive({
  username: '',
  password: '',
})

const isLoading = ref(false)
const errorMessage = ref('')

const handleLogin = async () => {
  isLoading.value = true
  errorMessage.value = ''

  try {
    await authStore.login(form)

    if (authStore.isRecruiter) {
      router.push({ name: 'recruiter-dashboard' })
    } else {
      router.push({ name: 'applicant-dashboard' })
    }
  } catch (error) {
    errorMessage.value = error.response?.data?.detail || 'Invalid credentials. Please try again.'
  } finally {
    isLoading.value = false
  }
}
</script>

<template>
  <div
    class="min-h-screen bg-slate-50 flex items-center justify-center p-4 sm:p-6 transition-colors duration-500"
  >
    <div
      class="w-full max-w-5xl bg-white rounded-[2rem] shadow-2xl border border-slate-100 overflow-hidden flex flex-col lg:flex-row min-h-[600px]"
    >
      <div
        class="hidden lg:flex w-1/2 flex-col justify-center items-center text-white px-12 relative overflow-hidden bg-gradient-to-br from-orange-400 to-red-600"
      >
        <div
          class="absolute inset-0 opacity-10 bg-[url('https://www.transparenttextures.com/patterns/cubes.png')]"
        ></div>

        <div class="relative z-10 text-center">
          <div
            class="bg-white/20 p-6 rounded-3xl inline-block mb-8 backdrop-blur-md shadow-xl animate-float-slow"
          >
            <LogIn class="w-16 h-16 text-white" />
          </div>
          <h2 class="text-4xl font-extrabold mb-4">Welcome Back!</h2>
          <p class="text-lg text-white/90 max-w-md mx-auto leading-relaxed">
            Log in to access your dashboard, track applications, and manage your job postings.
          </p>
        </div>
      </div>

      <div class="w-full lg:w-1/2 flex flex-col justify-center items-center px-8 py-12 bg-white">
        <div class="max-w-md w-full">
          <div class="text-center mb-10">
            <h1 class="text-3xl font-bold text-slate-900 mb-2">Sign In</h1>
            <p class="text-slate-500">Enter your credentials to continue</p>
          </div>

          <div
            v-if="errorMessage"
            class="mb-6 p-4 bg-red-50 border border-red-100 rounded-xl flex items-center gap-3 animate-pulse"
          >
            <div class="p-1 bg-red-100 rounded-full">
              <Lock class="w-4 h-4 text-red-600" />
            </div>
            <span class="text-sm text-red-700 font-medium">{{ errorMessage }}</span>
          </div>

          <form @submit.prevent="handleLogin" class="space-y-6">
            <div>
              <label class="block text-sm font-bold text-slate-700 mb-1.5 ml-1">Username</label>
              <input
                v-model="form.username"
                type="text"
                required
                class="w-full px-4 py-3.5 rounded-xl border border-slate-200 outline-none focus:ring-2 focus:ring-orange-500/20 focus:border-orange-500 transition-all bg-slate-50 focus:bg-white text-slate-900 placeholder:text-slate-400"
                placeholder="Enter your username"
              />
            </div>

            <div>
              <div class="flex justify-between items-center mb-1.5 ml-1">
                <label class="block text-sm font-bold text-slate-700">Password</label>
              </div>
              <input
                v-model="form.password"
                type="password"
                required
                class="w-full px-4 py-3.5 rounded-xl border border-slate-200 outline-none focus:ring-2 focus:ring-orange-500/20 focus:border-orange-500 transition-all bg-slate-50 focus:bg-white text-slate-900 placeholder:text-slate-400"
                placeholder="••••••••"
              />
            </div>

            <button
              type="submit"
              :disabled="isLoading"
              class="w-full bg-black hover:bg-slate-800 text-white font-bold py-4 rounded-xl shadow-lg shadow-slate-200 transition-all transform active:scale-95 flex justify-center items-center gap-2 disabled:opacity-70 disabled:cursor-not-allowed mt-2"
            >
              <span v-if="isLoading">Verifying...</span>
              <span v-else>Sign In <ArrowRight class="w-4 h-4 inline" /></span>
            </button>

            <p class="text-center text-slate-600 text-sm mt-6">
              Don't have an account?
              <router-link to="/signup" class="text-orange-600 font-bold hover:underline">
                Create Account
              </router-link>
            </p>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Same float animation as Signup for consistency */
@keyframes float {
  0% {
    transform: translateY(0px);
  }
  50% {
    transform: translateY(-10px);
  }
  100% {
    transform: translateY(0px);
  }
}
.animate-float-slow {
  animation: float 6s ease-in-out infinite;
}
</style>
