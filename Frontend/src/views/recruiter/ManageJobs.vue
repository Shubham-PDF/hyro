<script setup>
import { onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'
import { useJobs } from '@/composables/useJobs'
import {
  Users,
  Calendar,
  ArrowRight,
  FileText,
  MoreHorizontal,
  Plus,
  Pencil,
  Trash2,
  Power,
  EyeOff,
} from 'lucide-vue-next'

const router = useRouter()
const { jobs, fetchRecruiterJobs, toggleJobStatus, deleteJob, loading } = useJobs()

// Dropdown State
const activeDropdown = ref(null)

const toggleDropdown = (jobId) => {
  activeDropdown.value = activeDropdown.value === jobId ? null : jobId
}

// Close dropdown when clicking outside (simple implementation)
const closeDropdown = () => {
  activeDropdown.value = null
}

onMounted(() => {
  fetchRecruiterJobs()
  // Add global click listener to close dropdowns
  document.addEventListener('click', (e) => {
    if (!e.target.closest('.dropdown-container')) {
      closeDropdown()
    }
  })
})

const formatDate = (dateStr) => {
  if (!dateStr) return 'Recently'
  return new Date(dateStr).toLocaleDateString('en-US', {
    month: 'short',
    day: 'numeric',
    year: 'numeric',
  })
}

const handleEdit = (jobId) => {
  router.push(`/recruiter/jobs/${jobId}/edit`)
}

const viewCandidates = (jobId) => {
  router.push({ name: 'job-applicants', params: { id: jobId } })
}
</script>

<template>
  <div class="space-y-8 pb-12 min-h-screen">
    <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
      <div>
        <h1 class="text-3xl font-bold text-slate-900 tracking-tight">My Job Postings</h1>
        <p class="text-slate-500 mt-1">Manage active listings and review incoming applications.</p>
      </div>
      <router-link
        to="/recruiter/create-job"
        class="bg-orange-500 hover:bg-orange-600 text-white pl-6 pr-8 py-4 rounded-2xl font-bold text-lg shadow-lg shadow-orange-500/20 transition-all active:scale-95 flex items-center gap-2 group"
      >
        <Plus class="w-5 h-5" /> Post New Job
      </router-link>
    </div>

    <div v-if="loading" class="space-y-4">
      <div
        v-for="n in 3"
        :key="n"
        class="h-32 bg-white rounded-[2rem] border border-slate-100 animate-pulse"
      ></div>
    </div>

    <div
      v-else-if="jobs.length === 0"
      class="text-center py-24 bg-white rounded-[2rem] border border-slate-200 border-dashed flex flex-col items-center justify-center"
    >
      <div class="w-20 h-20 bg-slate-50 rounded-full flex items-center justify-center mb-6">
        <FileText class="w-10 h-10 text-slate-300" />
      </div>
      <h3 class="text-xl font-bold text-slate-900 mb-2">No jobs posted yet</h3>
      <p class="text-slate-500 mb-8 max-w-sm">Create your first listing to start finding talent.</p>
      <router-link to="/recruiter/create-job" class="text-orange-600 font-bold hover:underline">
        Post a Job Now
      </router-link>
    </div>

    <div v-else class="grid grid-cols-1 gap-6">
      <div
        v-for="job in jobs"
        :key="job.job_id"
        class="group bg-white p-6 md:p-8 rounded-[2rem] border transition-all duration-300 relative"
        :class="
          job.is_active
            ? 'border-slate-200 hover:border-orange-500/30 hover:shadow-xl'
            : 'border-slate-100 bg-slate-50/50 opacity-80'
        "
      >
        <div class="flex flex-col md:flex-row justify-between gap-6 md:items-center relative z-10">
          <div class="flex-1">
            <div class="flex items-center gap-3 mb-3">
              <h3
                class="text-xl font-bold text-slate-900 transition-colors"
                :class="{ 'text-slate-500': !job.is_active }"
              >
                {{ job.title }}
              </h3>
              <span
                class="px-2.5 py-1 rounded-lg text-xs font-bold uppercase tracking-wider border"
                :class="
                  job.is_active
                    ? 'bg-emerald-50 text-emerald-700 border-emerald-100'
                    : 'bg-slate-200 text-slate-500 border-slate-300'
                "
              >
                {{ job.is_active ? 'Active Hiring' : 'Inactive' }}
              </span>
            </div>

            <p class="text-slate-500 line-clamp-1 max-w-2xl mb-5 font-medium">
              {{ job.description }}
            </p>

            <div class="flex flex-wrap items-center gap-6 text-sm font-bold text-slate-400">
              <span class="flex items-center gap-2">
                <Calendar class="w-4 h-4" /> Posted {{ formatDate(job.created_at) }}
              </span>
              <span class="flex items-center gap-2 text-slate-700 bg-slate-50 px-3 py-1 rounded-lg">
                <Users class="w-4 h-4 text-orange-500" />
                {{ job.applicant_count || 0 }} Applicants
              </span>
            </div>
          </div>

          <div class="flex items-center gap-3 w-full md:w-auto relative">
            <div class="relative dropdown-container">
              <button
                @click.stop="toggleDropdown(job.job_id)"
                class="p-3.5 text-slate-400 hover:text-slate-900 hover:bg-slate-50 rounded-xl transition-colors border border-transparent hover:border-slate-200"
              >
                <MoreHorizontal class="w-5 h-5" />
              </button>

              <div
                v-if="activeDropdown === job.job_id"
                class="absolute right-0 top-full mt-2 w-48 bg-white rounded-xl shadow-xl border border-slate-100 z-50 overflow-hidden animate-in fade-in zoom-in-95 duration-100"
              >
                <button
                  @click="handleEdit(job.job_id)"
                  class="w-full text-left px-4 py-3 text-sm font-bold text-slate-600 hover:bg-slate-50 hover:text-slate-900 flex items-center gap-2"
                >
                  <Pencil class="w-4 h-4" /> Edit Job
                </button>

                <button
                  @click="toggleJobStatus(job)"
                  class="w-full text-left px-4 py-3 text-sm font-bold text-slate-600 hover:bg-slate-50 hover:text-slate-900 flex items-center gap-2"
                >
                  <component :is="job.is_active ? EyeOff : Power" class="w-4 h-4" />
                  {{ job.is_active ? 'Deactivate' : 'Activate' }}
                </button>

                <div class="h-px bg-slate-100 my-1"></div>

                <button
                  @click="deleteJob(job.job_id)"
                  class="w-full text-left px-4 py-3 text-sm font-bold text-red-600 hover:bg-red-50 flex items-center gap-2"
                >
                  <Trash2 class="w-4 h-4" /> Delete
                </button>
              </div>
            </div>

            <button
              @click="viewCandidates(job.job_id)"
              class="bg-orange-400 hover:bg-orange-300 text-white pl-6 pr-8 py-4 rounded-2xl font-bold text-lg shadow-lg shadow-orange-300/20 transition-all active:scale-95 flex items-center gap-2 group"
            >
              Review Candidates <ArrowRight class="w-4 h-4" />
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
