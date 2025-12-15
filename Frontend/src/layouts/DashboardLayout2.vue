<script setup>
import {
  LayoutDashboard,
  Briefcase,
  User,
  LogOut,
  Menu,
  X,
  Search,
  FileText,
} from 'lucide-vue-next'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { ref, computed } from 'vue'

const router = useRouter()
const authStore = useAuthStore()
const mobileMenuOpen = ref(false)

// 1. MENU ITEMS (Matches your Skeleton Wireframe)
const applicantMenuItems = [
  // "Browse Jobs" is the Home/Dashboard view in your skeleton
  { name: 'Browse Jobs', icon: Search, route: '/applicant/dashboard' },
  { name: 'Applied Jobs', icon: Briefcase, route: '/applicant/my-applications' },
  { name: 'Profile', icon: User, route: '/applicant/profile' },
]

const recruiterMenuItems = [
  { name: 'Dashboard', icon: LayoutDashboard, route: '/recruiter/dashboard' },
  { name: 'Post Job', icon: FileText, route: '/recruiter/create-job' },
  { name: 'Manage Jobs', icon: Briefcase, route: '/recruiter/jobs' },
  { name: 'Profile', icon: User, route: '/recruiter/profile' },
]

const menuItems = computed(() => (authStore.isRecruiter ? recruiterMenuItems : applicantMenuItems))

const handleLogout = () => {
  authStore.logout()
  router.push('/login')
}
</script>

<template>
  <div class="flex h-screen bg-slate-50 font-sans">
    <div
      v-if="mobileMenuOpen"
      class="fixed inset-0 bg-slate-900/50 backdrop-blur-sm z-30 md:hidden transition-opacity"
      @click="mobileMenuOpen = false"
    ></div>

    <aside
      class="fixed md:relative w-72 bg-white border-r border-slate-200 flex flex-col h-screen z-40 transform transition-transform duration-300 ease-in-out md:transform-none shadow-xl md:shadow-none"
      :class="mobileMenuOpen ? 'translate-x-0' : '-translate-x-full md:translate-x-0'"
    >
      <div class="p-8 flex items-center justify-between">
        <div class="flex items-center gap-2">
          <div
            class="w-8 h-8 bg-orange-600 rounded-lg flex items-center justify-center text-white font-bold text-lg"
          >
            H
          </div>
          <div class="text-2xl font-extrabold text-slate-900 tracking-tight">Hyro</div>
        </div>
        <button
          @click="mobileMenuOpen = false"
          class="md:hidden text-slate-500 hover:text-slate-900"
        >
          <X class="w-6 h-6" />
        </button>
      </div>

      <nav class="flex-1 px-6 py-4 space-y-2">
        <router-link
          v-for="item in menuItems"
          :key="item.name"
          :to="item.route"
          class="flex items-center gap-3 px-4 py-3.5 text-sm font-bold text-slate-500 rounded-xl transition-all duration-200 group"
          active-class="bg-orange-50 text-orange-700 shadow-sm ring-1 ring-orange-100"
          @click="mobileMenuOpen = false"
        >
          <component
            :is="item.icon"
            class="w-5 h-5 transition-colors group-hover:text-orange-600"
          />
          {{ item.name }}
        </router-link>
      </nav>

      <div class="p-6 border-t border-slate-100">
        <div class="mb-4 flex items-center gap-3 px-2">
          <div
            class="w-10 h-10 rounded-full bg-slate-100 flex items-center justify-center font-bold text-slate-600"
          >
            {{ authStore.user?.username?.charAt(0).toUpperCase() || 'U' }}
          </div>
          <div class="overflow-hidden">
            <p class="text-sm font-bold text-slate-900 truncate">
              {{ authStore.user?.username || 'User' }}
            </p>
            <p class="text-xs text-slate-500 truncate capitalize">
              {{ authStore.user?.role || 'Guest' }}
            </p>
          </div>
        </div>

        <button
          @click="handleLogout"
          class="flex items-center gap-3 w-full px-4 py-3 text-sm font-bold text-slate-600 hover:text-red-600 hover:bg-red-50 rounded-xl transition-all"
        >
          <LogOut class="w-5 h-5" />
          Sign Out
        </button>
      </div>
    </aside>

    <button
      @click="mobileMenuOpen = !mobileMenuOpen"
      class="fixed bottom-6 right-6 md:hidden z-50 bg-slate-900 text-white p-4 rounded-full shadow-2xl hover:scale-105 transition-transform active:scale-95"
    >
      <Menu class="w-6 h-6" />
    </button>

    <main class="flex-1 overflow-auto bg-slate-50">
      <div class="p-4 md:p-8 max-w-7xl mx-auto min-h-full flex flex-col">
        <RouterView />
      </div>
    </main>
  </div>
</template>
