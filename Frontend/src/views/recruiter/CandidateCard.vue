<script setup>
import { computed } from 'vue'
import { FileText, Ban, CheckCircle, Undo2, User } from 'lucide-vue-next'

const props = defineProps({
  application: {
    type: Object,
    required: true,
  },
})

defineEmits(['toggle-ignore'])

// Access the nested candidate object safely
const candidate = computed(() => props.application.candidate || {})

// Color logic for 0-100 score
const getScoreColor = (score) => {
  if (score >= 80) return 'text-emerald-700 bg-emerald-50 border-emerald-200'
  if (score >= 50) return 'text-orange-700 bg-orange-50 border-orange-200'
  return 'text-slate-600 bg-slate-100 border-slate-200'
}
</script>

<template>
  <div
    class="bg-white rounded-[1.5rem] border p-6 transition-all duration-300 group hover:border-orange-300 hover:shadow-lg"
    :class="application.isIgnored ? 'border-slate-100 opacity-60 grayscale' : 'border-slate-200'"
  >
    <div class="flex justify-between items-start mb-4">
      <div class="flex items-center gap-4">
        <div
          class="w-12 h-12 bg-slate-900 text-white rounded-xl flex items-center justify-center text-lg font-bold shadow-md uppercase"
        >
          {{ candidate.full_name?.charAt(0) || candidate.username?.charAt(0) || 'U' }}
        </div>
        <div>
          <h3 class="text-lg font-bold text-slate-900 leading-tight">
            {{ candidate.full_name || candidate.username }}
          </h3>
          <p class="text-xs text-slate-500 font-medium">
            Applied {{ new Date(application.applied_at).toLocaleDateString() }}
          </p>
        </div>
      </div>

      <div
        class="px-3 py-1.5 rounded-lg border flex items-center gap-1.5 font-bold text-sm"
        :class="getScoreColor(application.match_score)"
      >
        <CheckCircle class="w-4 h-4" />
        <span>Match Score: {{ Math.round(application.match_score) }}%</span>
      </div>
    </div>

    <div class="mb-6 pl-[4rem]">
      <div v-if="candidate.skills && candidate.skills.length" class="flex flex-wrap gap-2">
        <span
          v-for="skill in candidate.skills.slice(0, 4)"
          :key="skill"
          class="px-2.5 py-1 bg-slate-50 border border-slate-200 rounded-md text-xs font-bold text-slate-600"
        >
          {{ skill }}
        </span>
        <span v-if="candidate.skills.length > 4" class="text-xs text-slate-400 self-center">
          +{{ candidate.skills.length - 4 }}
        </span>
      </div>
      <p v-else class="text-xs text-slate-400 italic">No skills listed</p>
    </div>

    <div class="flex items-center gap-3 pt-4 border-t border-slate-100">
      <router-link
        :to="{ name: 'candidate-profile', params: { username: candidate.username } }"
        target="_blank"
        class="px-4 py-2 bg-white border border-slate-200 rounded-lg text-sm font-bold text-slate-700 hover:border-slate-900 hover:bg-slate-50 transition-colors flex items-center gap-2"
      >
        <User class="w-4 h-4" /> Profile
      </router-link>

      <a
        v-if="application.resume_file"
        :href="application.resume_file"
        target="_blank"
        class="px-4 py-2 bg-white border border-slate-200 rounded-lg text-sm font-bold text-slate-700 hover:text-orange-600 hover:border-orange-200 transition-colors flex items-center gap-2"
      >
        <FileText class="w-4 h-4" /> Resume PDF
      </a>

      <button
        @click="$emit('toggle-ignore', application.id)"
        class="ml-auto px-4 py-2 rounded-lg text-sm font-bold transition-colors flex items-center gap-2"
        :class="
          application.isIgnored
            ? 'bg-slate-100 text-slate-500'
            : 'text-slate-400 hover:bg-red-50 hover:text-red-500'
        "
      >
        <component :is="application.isIgnored ? Undo2 : Ban" class="w-4 h-4" />
        {{ application.isIgnored ? 'Undo' : 'Ignore' }}
      </button>
    </div>
  </div>
</template>
