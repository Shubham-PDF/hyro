<script setup>
import { onMounted, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useRecruiter } from '@/composables/useRecruiter'
import CandidateCard from '@/views/recruiter/CandidateCard.vue'
import { ArrowLeft, UserX, Users } from 'lucide-vue-next'

const route = useRoute()
const router = useRouter()
const { applicants, fetchApplicants, loading } = useRecruiter()

onMounted(() => {
  fetchApplicants(route.params.id)
})

// Sorting: Active first, then by Match Score
const sortedApplicants = computed(() => {
  const active = applicants.value.filter((a) => !a.isIgnored)
  const ignored = applicants.value.filter((a) => a.isIgnored)

  active.sort((a, b) => b.match_score - a.match_score)
  ignored.sort((a, b) => b.match_score - a.match_score)

  return [...active, ...ignored]
})

const toggleIgnore = (appId) => {
  const app = applicants.value.find((a) => a.id === appId)
  if (app) app.isIgnored = !app.isIgnored
}
</script>

<template>
  <div class="space-y-8 pb-20">
    <div
      class="flex flex-col md:flex-row md:items-center justify-between gap-6 bg-white p-6 rounded-[2rem] border border-slate-200 shadow-sm"
    >
      <div class="flex items-center gap-5">
        <button
          @click="router.back()"
          class="w-12 h-12 flex items-center justify-center rounded-full border border-slate-200 text-slate-500 hover:bg-slate-50 hover:text-slate-900 transition-colors"
        >
          <ArrowLeft class="w-5 h-5" />
        </button>
        <div>
          <h1 class="text-2xl font-bold text-slate-900 tracking-tight">Review Applicants</h1>
          <p class="text-slate-500 font-medium flex items-center gap-2">
            <Users class="w-4 h-4" /> {{ applicants.length }} Total Candidates
          </p>
        </div>
      </div>
    </div>

    <TransitionGroup name="list" tag="div" class="space-y-4 relative" v-if="applicants.length > 0">
      <CandidateCard
        v-for="app in sortedApplicants"
        :key="app.id"
        :application="app"
        @toggle-ignore="toggleIgnore"
      />
    </TransitionGroup>

    <div
      v-else-if="!loading"
      class="text-center py-24 bg-white rounded-[2rem] border border-slate-200 border-dashed"
    >
      <div class="w-20 h-20 bg-slate-50 rounded-full flex items-center justify-center mx-auto mb-6">
        <UserX class="w-10 h-10 text-slate-300" />
      </div>
      <h3 class="text-xl font-bold text-slate-900 mb-2">No Applicants Yet</h3>
      <p class="text-slate-500">Wait for candidates to apply to this job.</p>
    </div>
  </div>
</template>

<style scoped>
/* Smooth Reordering Animation for movement of user */
.list-move,
.list-enter-active,
.list-leave-active {
  transition: all 0.5s cubic-bezier(0.55, 0, 0.1, 1);
}
.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: scale(0.95);
}
.list-leave-active {
  position: absolute;
  width: 100%; /* Ensures layout doesn't collapse during exit */
}
</style>
