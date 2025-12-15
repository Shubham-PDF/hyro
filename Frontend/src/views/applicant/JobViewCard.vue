<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

// Accept job object as prop
const props = defineProps({
  job: {
    type: Object,
    required: true,
  },
})
</script>

<template>
  <div
    class="bg-white rounded-[2rem] border-2 border-slate-200 p-8 hover:border-slate-900 transition-all duration-300 group flex flex-col justify-between h-[320px] relative overflow-hidden cursor-pointer"
    @click="router.push(`/applicant/jobs/${props.job.job_id}`)"
  >
    <!-- Job info -->
    <div
      class="flex-1 flex flex-col items-center justify-center text-center z-10 pointer-events-none"
    >
      <h3
        class="text-3xl font-mono font-bold text-slate-900 mb-2 group-hover:scale-105 transition-transform"
      >
        {{ props.job.title }}
      </h3>

      <p class="text-lg text-slate-500 font-medium">
        {{ props.job.company_name }}
      </p>

      <div class="mt-4 flex gap-2 justify-center">
        <span class="px-3 py-1 bg-slate-100 text-slate-600 rounded-full text-xs font-bold">
          {{ props.job.location }}
        </span>

        <span class="px-3 py-1 bg-green-50 text-green-700 rounded-full text-xs font-bold">
          ₹{{ Math.round(props.job.salary_min / 1000) }}k+
        </span>
      </div>
    </div>

    <!-- Button -->
    <div class="flex justify-end mt-4 z-10 pointer-events-none">
      <button
        class="px-6 py-3 rounded-xl border-2 border-slate-900 text-slate-900 font-bold hover:bg-slate-900 hover:text-white transition-all active:scale-95 flex items-center gap-2"
      >
        More Details
      </button>
    </div>

    <!-- Background expanding circle -->
    <div
      class="absolute -bottom-10 -left-10 w-32 h-32 bg-slate-50 rounded-full group-hover:scale-150 transition-transform duration-700 ease-in-out z-0"
    ></div>
  </div>
</template>
