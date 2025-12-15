<script setup>
import { onMounted, computed } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useJobs } from '@/composables/useJobs'
import { useRouter } from 'vue-router'
import { ArrowRight, Briefcase, Sparkles } from 'lucide-vue-next'
import JobViewCard from '@/views/applicant/JobViewCard.vue'

const authStore = useAuthStore()
const { publicJobs, fetchPublicJobs, loading } = useJobs()
const router = useRouter()

// Get first name for a more personal touch
const userName = computed(() => {
  const full = authStore.user?.username || 'Applicant'
  return full.charAt(0).toUpperCase() + full.slice(1)
})

// Fetch jobs on mount
onMounted(() => {
  fetchPublicJobs()
})
</script>

<template>
  <div class="h-full flex flex-col gap-6">
    <div
      class="relative w-full bg-slate-900 rounded-[2rem] p-8 md:p-10 shadow-xl overflow-hidden group"
    >
      <div
        class="absolute top-0 right-0 w-96 h-96 bg-gradient-to-br from-orange-500/20 to-purple-500/20 rounded-full blur-3xl -mr-20 -mt-20 pointer-events-none"
      ></div>

      <div class="relative z-10 flex flex-col md:flex-row justify-between items-start md:items-center gap-6">
  
  <div class="max-w-2xl">
    <div class="flex items-center gap-3 mb-3">
      <h1 class="text-3xl md:text-4xl font-bold text-white tracking-tight">
        Welcome Back, {{ userName }}
      </h1>
    </div>
    
    <p class="text-slate-400 text-lg font-medium leading-relaxed mb-6">
      Let's find the best opportunities for you and
      <span class="text-white font-semibold">outshine your career</span> today.
    </p>

    <div 
      @click="router.push('/applicant/profile')" 
      class="inline-flex items-start gap-3 p-4 rounded-xl bg-white/5 border border-white/10 hover:bg-white/10 hover:border-orange-500/30 transition-all cursor-pointer group"
    >
      <div class="p-2 bg-orange-500/10 rounded-lg text-orange-400 group-hover:bg-orange-500 group-hover:text-white transition-colors">
        <Sparkles class="w-5 h-5" />
      </div>
      <div>
        <p class="text-slate-200 text-sm font-medium">
          <span class="text-orange-400 font-bold">Boost your chances!</span> 
          Complete your profile details to get noticed by top recruiters 3x faster.
        </p>
        <div class="text-xs font-bold text-slate-400 mt-1 flex items-center gap-1 group-hover:text-white transition-colors">
          Update Profile Now <ArrowRight class="w-3 h-3" />
        </div>
      </div>
    </div>
    </div>

  <div class="w-full md:w-auto mt-6 md:mt-0">
    <button
      @click="router.push('/applicant/jobsView')"
      class="bg-orange-500 hover:bg-orange-600 text-white pl-6 pr-8 py-4 rounded-2xl font-bold text-lg shadow-lg shadow-orange-500/20 transition-all active:scale-95 flex items-center gap-2 group w-full md:w-auto justify-center"
    >
      Search For Jobs
      <ArrowRight class="w-4 h-4 group-hover:translate-x-1 transition-transform" />
    </button>
  </div>

</div>
    </div>

    <div class="flex-1 bg-white border border-slate-200 rounded-[2rem] p-8 shadow-sm flex flex-col">
      <div class="flex items-center gap-3 mb-8">
        <div class="p-2 bg-orange-50 rounded-lg">
          <Briefcase class="w-6 h-6 text-orange-600" />
        </div>
        <h2 class="text-2xl font-bold text-slate-900">Browse Some Jobs</h2>
      </div>

      <div v-if="loading" class="flex-1 flex flex-col items-center justify-center gap-4 py-12">
        <div
          class="animate-spin w-10 h-10 border-4 border-orange-500 border-t-transparent rounded-full"
        ></div>
        <p class="text-slate-400 font-medium animate-pulse">Curating jobs for you...</p>
      </div>

      <div
        v-else-if="publicJobs.length === 0"
        class="flex-1 flex flex-col items-center justify-center text-center py-12"
      >
        <div class="w-16 h-16 bg-slate-50 rounded-full flex items-center justify-center mb-4">
          <Briefcase class="w-8 h-8 text-slate-400" />
        </div>
        <h3 class="text-lg font-bold text-slate-900">No jobs found</h3>
        <p class="text-slate-500">Check back later for new opportunities.</p>
      </div>

      <div v-else class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8 flex-1">
        <JobViewCard v-for="job in publicJobs.slice(0, 4)" :key="job.job_id" :job="job" />
      </div>

      <div class="mt-auto">
        <button
          @click="router.push('/applicant/jobsView')"
          class="w-full py-4 bg-slate-900 hover:bg-slate-800 text-white rounded-xl font-bold text-sm tracking-wide shadow-lg shadow-slate-900/20 transition-all active:scale-[0.98] flex items-center justify-center gap-2 group"
        >
          Browse More Jobs
          <ArrowRight class="w-4 h-4 group-hover:translate-x-1 transition-transform" />
        </button>
      </div>
    </div>
  </div>
</template>
