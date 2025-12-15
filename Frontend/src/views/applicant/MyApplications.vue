<script setup>
import { onMounted } from 'vue'
import { useApplications } from '@/composables/useApplications'
import { Search } from 'lucide-vue-next'
import { useRouter } from 'vue-router'
import JobViewCard from './JobViewCard.vue'

const { applications, fetchMyApplications, loading } = useApplications()
const router = useRouter()

onMounted(() => {
  fetchMyApplications()
})

const formatDate = (dateString) => {
  if (!dateString) return ''
  return new Date(dateString).toLocaleDateString('en-US', {
    month: 'short',
    day: 'numeric',
    year: 'numeric',
  })
}
</script>

<template>
  <div class="space-y-8 h-full pb-12">
    <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
      <div>
        <h1 class="text-3xl font-bold text-slate-900 tracking-tight">My Applications</h1>
        <p class="text-slate-500 mt-1">Track your history and resume match scores.</p>
      </div>
      <div
        v-if="!loading"
        class="bg-white px-5 py-2.5 rounded-xl border border-slate-200 shadow-sm flex gap-3 items-center self-start"
      >
        <span class="text-xs font-bold text-slate-400 uppercase tracking-wider">Total Applied</span>
        <span class="text-xl font-bold text-slate-900">{{ applications.length }}</span>
      </div>
    </div>

    <div v-if="loading" class="grid grid-cols-1 gap-4">
      <div
        v-for="n in 3"
        :key="n"
        class="bg-white p-6 rounded-[2rem] border border-slate-100 h-48 animate-pulse flex flex-col justify-between"
      >
        <div class="flex gap-4">
          <div class="w-16 h-16 bg-slate-100 rounded-xl"></div>
          <div class="space-y-3 flex-1">
            <div class="h-6 w-1/3 bg-slate-100 rounded-lg"></div>
            <div class="h-4 w-1/4 bg-slate-100 rounded-lg"></div>
          </div>
        </div>
      </div>
    </div>

    <div
      v-else-if="applications.length === 0"
      class="bg-white rounded-[2rem] border border-slate-200 border-dashed p-12 text-center flex flex-col items-center justify-center py-24"
    >
      <div class="w-20 h-20 bg-slate-50 rounded-full flex items-center justify-center mb-6">
        <Search class="w-10 h-10 text-slate-400" />
      </div>
      <h3 class="text-xl font-bold text-slate-900 mb-2">No applications yet</h3>
      <p class="text-slate-500 mb-8 max-w-sm mx-auto">
        You haven't applied to any jobs yet. Start browsing to find your next role.
      </p>
      <button
        @click="router.push('/applicant/jobs')"
        class="bg-slate-900 text-white px-8 py-3.5 rounded-xl font-bold hover:bg-slate-800 transition-all active:scale-95 shadow-lg shadow-slate-900/20"
      >
        Browse Jobs
      </button>
    </div>

    <div v-else class="grid grid-cols-2 gap-6">
      <JobViewCard
        v-for="app in applications"
        :key="app.id"
        :job="app.job_details"
        :appliedAt="formatDate(app.applied_at)"
        :resumeFile="app.resume_file"
        :showExtras="true"
      />
    </div>
  </div>
</template>
