<script setup>
import { onMounted, computed } from 'vue'
import { useJobs } from '@/composables/useJobs'
import { useAuthStore } from '@/stores/auth'
import { Users, FileText, Zap, ArrowRight, Plus } from 'lucide-vue-next'

const authStore = useAuthStore()
const { jobs, fetchRecruiterJobs, loading } = useJobs()

// 1. Fetch Data on Mount
onMounted(() => {
  fetchRecruiterJobs()
})

// 2. Compute Stats
const totalJobs = computed(() => jobs.value.length)
const activeJobs = computed(() => jobs.value.filter((job) => job.is_active).length)
const totalCandidates = computed(() =>
  jobs.value.reduce((sum, job) => sum + (job.applicant_count || 0), 0),
)
const recentJobs = computed(() => jobs.value.slice(0, 3))
</script>

<template>
  <div class="space-y-8 pb-12">
    <div
      class="relative bg-slate-900 rounded-[2.5rem] p-8 md:p-12 overflow-hidden shadow-2xl shadow-slate-200"
    >
      <div
        class="absolute top-0 right-0 w-96 h-96 bg-orange-500/20 rounded-full blur-[100px] -mr-20 -mt-20 pointer-events-none"
      ></div>

      <div
        class="relative z-10 flex flex-col md:flex-row justify-between items-start md:items-center gap-6"
      >
        <div>
          <div class="flex items-center gap-2 mb-2">
            <span
              class="px-3 py-1 rounded-full bg-orange-500/10 text-orange-400 text-xs font-bold uppercase tracking-wider border border-orange-500/20"
            >
              Recruiter Dashboard
            </span>
          </div>
          <h1 class="text-3xl md:text-5xl font-bold text-white tracking-tight mb-2">
            Hello,
            <span class="text-orange-500">{{
              authStore.user?.full_name || authStore.user?.username || 'Recruiter'
            }}</span
            >!
          </h1>
          <p class="text-slate-400 text-lg max-w-xl">
            You have
            <span class="text-white font-bold">{{ totalCandidates }} active candidates</span>
            waiting for review today.
          </p>
        </div>

        <router-link
          to="/recruiter/create-job"
          class="bg-orange-500 hover:bg-orange-600 text-white pl-6 pr-8 py-4 rounded-2xl font-bold text-lg shadow-lg shadow-orange-500/20 transition-all active:scale-95 flex items-center gap-2 group"
        >
          <Plus
            class="w-6 h-6 bg-white/20 rounded-full p-1 group-hover:rotate-90 transition-transform"
          />
          Post a Job
        </router-link>
      </div>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      <div
        class="bg-white p-8 rounded-[2rem] border border-slate-100 shadow-sm hover:shadow-md transition-all group"
      >
        <div class="flex items-center justify-between mb-4">
          <div
            class="p-4 bg-slate-50 text-slate-600 rounded-2xl group-hover:bg-slate-900 group-hover:text-white transition-colors"
          >
            <FileText class="w-7 h-7" />
          </div>
          <span class="text-3xl font-extrabold text-slate-900">{{
            loading ? '-' : totalJobs
          }}</span>
        </div>
        <p class="text-slate-500 font-bold text-sm uppercase tracking-wide">Total Posted Jobs</p>
      </div>

      <div
        class="bg-white p-8 rounded-[2rem] border border-orange-100 shadow-sm hover:shadow-md transition-all group relative overflow-hidden"
      >
        <div
          class="absolute right-0 top-0 w-32 h-32 bg-orange-50 rounded-full blur-3xl -mr-10 -mt-10"
        ></div>
        <div class="relative z-10 flex items-center justify-between mb-4">
          <div
            class="p-4 bg-orange-50 text-orange-600 rounded-2xl group-hover:bg-orange-500 group-hover:text-white transition-colors"
          >
            <Zap class="w-7 h-7" />
          </div>
          <span class="text-3xl font-extrabold text-slate-900">{{
            loading ? '-' : activeJobs
          }}</span>
        </div>
        <p class="text-slate-500 font-bold text-sm uppercase tracking-wide relative z-10">
          Active Listings
        </p>
      </div>

      <div
        class="bg-white p-8 rounded-[2rem] border border-slate-100 shadow-sm hover:shadow-md transition-all group"
      >
        <div class="flex items-center justify-between mb-4">
          <div
            class="p-4 bg-blue-50 text-blue-600 rounded-2xl group-hover:bg-blue-600 group-hover:text-white transition-colors"
          >
            <Users class="w-7 h-7" />
          </div>
          <span class="text-3xl font-extrabold text-slate-900">{{
            loading ? '-' : totalCandidates
          }}</span>
        </div>
        <p class="text-slate-500 font-bold text-sm uppercase tracking-wide">Total Applicants</p>
      </div>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
      <div class="lg:col-span-2 bg-white rounded-[2.5rem] border border-slate-200 p-8 shadow-sm">
        <div class="flex items-center justify-between mb-8">
          <h2 class="text-2xl font-bold text-slate-900">Recent Postings</h2>
          <router-link
            to="/recruiter/jobs"
            class="text-orange-600 font-bold text-sm hover:underline"
          >
            View All
          </router-link>
        </div>

        <div v-if="loading" class="space-y-4">
          <div v-for="n in 3" :key="n" class="h-20 bg-slate-50 rounded-2xl animate-pulse"></div>
        </div>

        <div v-else-if="jobs.length === 0" class="text-center py-10">
          <p class="text-slate-500">No jobs posted yet.</p>
        </div>

        <div v-else class="space-y-4">
          <div
            v-for="job in recentJobs"
            :key="job.id"
            class="flex items-center justify-between p-5 rounded-2xl border border-slate-100 hover:border-orange-200 hover:bg-orange-50/30 transition-all group cursor-pointer"
            
          >
            <div class="flex items-center gap-4">
              <div
                class="w-12 h-12 bg-slate-100 rounded-xl flex items-center justify-center font-bold text-slate-500 group-hover:bg-white group-hover:text-orange-600 transition-colors"
              >
                {{ job.title.charAt(0) }}
              </div>
              <div>
                <h4 class="font-bold text-slate-900 group-hover:text-orange-600 transition-colors">
                  {{ job.title }}
                </h4>
                <p class="text-xs font-bold text-slate-400 uppercase tracking-wide">
                  {{ job.location }}
                </p>
              </div>
            </div>

            <div class="flex items-center gap-6">
              <div class="text-right hidden sm:block">
                <p class="text-xs font-bold text-slate-400 uppercase">Applicants</p>
                <p class="font-bold text-slate-900">{{ job.applicant_count || 0 }}</p>
              </div>

            </div>
          </div>
        </div>
      </div>

      <div
        class="bg-gradient-to-br from-orange-500 to-red-600 rounded-[2.5rem] p-8 text-white relative overflow-hidden flex flex-col justify-between"
      >
        <div class="relative z-10">
          <div
            class="w-12 h-12 bg-white/20 backdrop-blur-md rounded-2xl flex items-center justify-center mb-6"
          >
            <Zap class="w-6 h-6 text-white" />
          </div>
          <h3 class="text-2xl font-bold mb-3">AI Power Tip</h3>
          <p class="text-orange-100 leading-relaxed">
            Did you know? Jobs with auto-generated keywords get
            <span class="font-bold text-white">40% better matches</span>. Use our AI tool when
            posting new roles!
          </p>
        </div>

        <button
          @click="$router.push('/recruiter/create-job')"
          class="mt-8 bg-white text-orange-600 w-full py-4 rounded-xl font-bold hover:bg-orange-50 transition-colors relative z-10"
        >
          Try it Now
        </button>

        <div
          class="absolute bottom-0 right-0 w-48 h-48 bg-white/10 rounded-full blur-2xl -mb-10 -mr-10"
        ></div>
      </div>
    </div>
  </div>
</template>
