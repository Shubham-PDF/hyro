<script setup>
import { reactive, ref, computed } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useRouter } from 'vue-router'
import { User, Briefcase, ArrowRight } from 'lucide-vue-next'

const authStore = useAuthStore()
const router = useRouter()

const role = ref('applicant')

const form = reactive({
  full_name: '',
  username: '',
  email: '',
  phone: '',
  password: '',
})

const isLoading = ref(false)
const errorMessage = ref('')

const content = computed(() => {
  return role.value === 'applicant'
    ? {
        key: 'app', // Unique key triggers the animation
        title: 'Find Your Dream Job',
        desc: 'Join thousands of developers getting hired at top companies.',
        icon: User,
        switchText: 'Sign up as Recruiter',
      }
    : {
        key: 'rec',
        title: 'Hire Top Talent',
        desc: 'Post jobs and find the perfect candidate for your team.',
        icon: Briefcase,
        switchText: 'Sign up as Applicant',
      }
})

const toggleRole = () => {
  role.value = role.value === 'applicant' ? 'recruiter' : 'applicant'
  errorMessage.value = ''
}

const handleSignup = async () => {
  isLoading.value = true
  errorMessage.value = ''

  try {
    await authStore.signup({ ...form, role: role.value })
    router.push('/login')
  } catch (error) {
    const errData = error.response?.data
    if (errData?.username || errData?.email) {
      errorMessage.value = 'User already exists! Please proceed to Login.'
    } else {
      errorMessage.value = 'Signup failed. Please try again.'
    }
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
      class="w-full max-w-5xl bg-white rounded-[2rem] shadow-2xl border border-slate-100 overflow-hidden flex flex-col lg:flex-row min-h-[650px]"
    >
      <div
        class="hidden lg:flex w-1/2 flex-col justify-center items-center text-white px-12 relative overflow-hidden"
      >
        <div class="absolute inset-0 bg-gradient-to-br from-blue-600 to-indigo-800 z-0"></div>

        <div
          class="absolute inset-0 bg-gradient-to-br from-orange-500 to-red-600 z-0 transition-opacity duration-700 ease-in-out"
          :class="role === 'recruiter' ? 'opacity-100' : 'opacity-0'"
        ></div>

        <div
          class="absolute inset-0 opacity-10 bg-[url('https://www.transparenttextures.com/patterns/cubes.png')] z-0"
        ></div>

        <div class="relative z-10 text-center">
          <Transition name="fade-slide" mode="out-in">
            <div :key="content.key">
              <div class="bg-white/20 p-6 rounded-3xl inline-block mb-8 backdrop-blur-md shadow-xl">
                <component :is="content.icon" class="w-16 h-16 text-white" />
              </div>
              <h2 class="text-4xl font-extrabold mb-4">{{ content.title }}</h2>
              <p class="text-lg text-white/90 max-w-md mx-auto leading-relaxed">
                {{ content.desc }}
              </p>
            </div>
          </Transition>
        </div>
      </div>

      <div
        class="w-full lg:w-1/2 flex flex-col justify-center items-center px-8 py-12 bg-white relative"
      >
        <div class="max-w-md w-full">
          <div class="text-center mb-10">
            <h1 class="text-3xl font-bold text-slate-900 mb-2">Create Account</h1>
            <p class="text-slate-500 transition-all duration-300">
              Sign up as
              <span
                class="font-bold capitalize transition-colors duration-500"
                :class="role === 'recruiter' ? 'text-orange-600' : 'text-blue-600'"
              >
                {{ role }}
              </span>
            </p>
          </div>

          <Transition name="bounce">
            <div
              v-if="errorMessage"
              class="mb-6 p-4 bg-red-50 border border-red-100 rounded-xl flex items-center justify-between"
            >
              <div class="text-sm text-red-700 font-medium">⚠️ {{ errorMessage }}</div>
              <router-link
                to="/login"
                class="text-xs bg-white border border-red-200 px-3 py-1 rounded-md text-red-700 hover:bg-red-50 font-bold"
              >
                Login
              </router-link>
            </div>
          </Transition>

          <form @submit.prevent="handleSignup" class="space-y-5">
            <div>
              <label class="block text-sm font-medium text-slate-700 mb-1">Full Name</label>
              <input
                v-model="form.full_name"
                type="text"
                required
                class="w-full px-4 py-3 rounded-xl border border-slate-200 outline-none focus:ring-2 focus:border-transparent transition-all bg-slate-50 focus:bg-white"
                :class="role === 'recruiter' ? 'focus:ring-orange-500' : 'focus:ring-blue-500'"
                placeholder="Shubham"
              />
            </div>

            <div>
              <label class="block text-sm font-medium text-slate-700 mb-1">Username</label>
              <input
                v-model="form.username"
                type="text"
                required
                class="w-full px-4 py-3 rounded-xl border border-slate-200 outline-none focus:ring-2 focus:border-transparent transition-all bg-slate-50 focus:bg-white"
                :class="role === 'recruiter' ? 'focus:ring-orange-500' : 'focus:ring-blue-500'"
                placeholder="Shubham"
              />
            </div>

            <div>
              <label class="block text-sm font-medium text-slate-700 mb-1">Email Address</label>
              <input
                v-model="form.email"
                type="email"
                required
                class="w-full px-4 py-3 rounded-xl border border-slate-200 outline-none focus:ring-2 focus:border-transparent transition-all bg-slate-50 focus:bg-white"
                :class="role === 'recruiter' ? 'focus:ring-orange-500' : 'focus:ring-blue-500'"
                placeholder="email@hyro.com"
              />
            </div>

            <div>
              <label class="block text-sm font-medium text-slate-700 mb-1">Phone Number</label>
              <input
                v-model="form.phone"
                type="tel"
                class="w-full px-4 py-3 rounded-xl border border-slate-200 outline-none focus:ring-2 focus:border-transparent transition-all bg-slate-50 focus:bg-white"
                :class="role === 'recruiter' ? 'focus:ring-orange-500' : 'focus:ring-blue-500'"
                placeholder="+91 234 567 8900"
              />
            </div>

            <div>
              <label class="block text-sm font-medium text-slate-700 mb-1">Password</label>
              <input
                v-model="form.password"
                type="password"
                required
                class="w-full px-4 py-3 rounded-xl border border-slate-200 outline-none focus:ring-2 focus:border-transparent transition-all bg-slate-50 focus:bg-white"
                :class="role === 'recruiter' ? 'focus:ring-orange-500' : 'focus:ring-blue-500'"
                placeholder="••••••••"
              />
            </div>

            <button
              type="submit"
              :disabled="isLoading"
              class="w-full text-white font-bold py-4 rounded-xl shadow-lg transition-all duration-300 transform active:scale-95 flex justify-center items-center gap-2"
              :class="
                role === 'recruiter'
                  ? 'bg-orange-600 hover:bg-orange-700 shadow-orange-200'
                  : 'bg-slate-900 hover:bg-slate-800 shadow-slate-200'
              "
            >
              <span v-if="isLoading">Creating Account...</span>
              <span v-else>Get Started <ArrowRight class="w-4 h-4 inline" /></span>
            </button>
          </form>

          <div class="mt-8 text-center pt-6 border-t border-slate-100">
            <button
              @click="toggleRole"
              class="text-sm font-medium text-slate-500 hover:text-slate-800 transition-colors flex items-center justify-center gap-2 mx-auto group"
            >
              Want to {{ role === 'applicant' ? 'hire talent' : 'find a job' }}?
              <span
                class="font-bold underline cursor-pointer transition-colors duration-300"
                :class="
                  role === 'recruiter'
                    ? 'text-blue-600 group-hover:text-blue-700'
                    : 'text-orange-600 group-hover:text-orange-700'
                "
              >
                {{ content.switchText }}
              </span>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* ✨ CSS ANIMATIONS
  These define how the content slides in and out when the role changes.
*/

.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}

.fade-slide-enter-from {
  opacity: 0;
  transform: translateY(20px);
}

.fade-slide-leave-to {
  opacity: 0;
  transform: translateY(-20px);
}

/* Bounce animation for error messages */
.bounce-enter-active {
  animation: bounce-in 0.5s;
}
.bounce-leave-active {
  animation: bounce-in 0.5s reverse;
}
@keyframes bounce-in {
  0% {
    transform: scale(0);
  }
  50% {
    transform: scale(1.05);
  }
  100% {
    transform: scale(1);
  }
}
</style>
