<script setup>
import { onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useRecruiter } from '@/composables/useRecruiter'
import {
  Mail,
  Phone,
  Linkedin,
  Github,
  Globe,
  Briefcase,
  Code2,
  User,
  ExternalLink,
} from 'lucide-vue-next'

const route = useRoute()
const { currentCandidateProfile, fetchCandidateProfile, profileLoading } = useRecruiter()

onMounted(() => {
  if (route.params.username) {
    fetchCandidateProfile(route.params.username)
  }
})
</script>

<template>
  <div class="min-h-screen bg-slate-50 p-6 md:p-10 font-sans">
    <div v-if="profileLoading" class="flex flex-col items-center justify-center h-[80vh]">
      <div
        class="w-12 h-12 border-4 border-orange-500 border-t-transparent rounded-full animate-spin mb-4"
      ></div>
      <p class="text-slate-500 font-bold">Loading Profile...</p>
    </div>

    <div v-else-if="currentCandidateProfile" class="max-w-4xl mx-auto space-y-8">
      <div
        class="bg-white rounded-[2rem] p-8 md:p-10 border border-slate-200 shadow-xl relative overflow-hidden"
      >
        <div
          class="absolute top-0 right-0 w-64 h-64 bg-orange-50 rounded-full blur-3xl -mr-16 -mt-16 pointer-events-none"
        ></div>

        <div
          class="relative z-10 flex flex-col md:flex-row items-center gap-8 text-center md:text-left"
        >
          <div
            class="w-32 h-32 bg-slate-900 text-white rounded-[2rem] flex items-center justify-center text-4xl font-bold shadow-2xl shadow-slate-900/20 uppercase"
          >
            {{
              currentCandidateProfile.full_name?.charAt(0) ||
              currentCandidateProfile.username?.charAt(0)
            }}
          </div>

          <div>
            <h1 class="text-4xl font-extrabold text-slate-900 tracking-tight mb-2">
              {{ currentCandidateProfile.full_name || '@' + currentCandidateProfile.username }}
            </h1>
            <p class="text-lg text-slate-500 font-medium mb-6">
              {{ currentCandidateProfile.role }} • @{{ currentCandidateProfile.username }}
            </p>

            <div class="flex flex-wrap justify-center md:justify-start gap-3">
              <a
                v-if="currentCandidateProfile.email"
                :href="`mailto:${currentCandidateProfile.email}`"
                class="flex items-center gap-2 px-4 py-2 bg-slate-50 border border-slate-200 rounded-xl text-slate-700 font-bold hover:bg-white hover:border-orange-200 hover:text-orange-600 transition-colors"
              >
                <Mail class="w-4 h-4" /> {{ currentCandidateProfile.email }}
              </a>
              <a
                v-if="currentCandidateProfile.phone"
                :href="`tel:${currentCandidateProfile.phone}`"
                class="flex items-center gap-2 px-4 py-2 bg-slate-50 border border-slate-200 rounded-xl text-slate-700 font-bold hover:bg-white hover:border-orange-200 hover:text-orange-600 transition-colors"
              >
                <Phone class="w-4 h-4" /> {{ currentCandidateProfile.phone }}
              </a>
            </div>
          </div>
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="md:col-span-2 space-y-8">
          <div class="bg-white rounded-[2rem] p-8 border border-slate-200 shadow-sm">
            <h3 class="text-lg font-bold text-slate-900 mb-4 flex items-center gap-2">
              <User class="w-5 h-5 text-orange-500" /> About
            </h3>
            <p class="text-slate-600 leading-relaxed whitespace-pre-line">
              {{ currentCandidateProfile.about || 'No bio provided.' }}
            </p>
          </div>

          <div class="bg-white rounded-[2rem] p-8 border border-slate-200 shadow-sm">
            <h3 class="text-lg font-bold text-slate-900 mb-4 flex items-center gap-2">
              <Code2 class="w-5 h-5 text-orange-500" /> Skills
            </h3>
            <div class="flex flex-wrap gap-2">
              <span
                v-for="skill in currentCandidateProfile.skills"
                :key="skill"
                class="px-4 py-2 bg-slate-50 text-slate-700 font-bold border border-slate-200 rounded-xl"
              >
                {{ skill }}
              </span>
              <span v-if="!currentCandidateProfile.skills?.length" class="text-slate-400 italic"
                >No skills listed.</span
              >
            </div>
          </div>
        </div>

        <div class="space-y-6">
          <div class="bg-slate-900 text-white rounded-[2rem] p-8 shadow-lg">
            <h3 class="text-lg font-bold mb-6 flex items-center gap-2">
              <Globe class="w-5 h-5 text-orange-500" /> Social Links
            </h3>
            <div class="space-y-4">
              <a
                v-if="currentCandidateProfile.linkedin_url"
                :href="currentCandidateProfile.linkedin_url"
                target="_blank"
                class="flex items-center justify-between p-4 bg-white/10 rounded-xl hover:bg-white/20 transition-colors group"
              >
                <span class="font-bold flex items-center gap-2"
                  ><Linkedin class="w-4 h-4" /> LinkedIn</span
                >
                <ExternalLink class="w-4 h-4 opacity-50 group-hover:opacity-100" />
              </a>
              <a
                v-if="currentCandidateProfile.github_url"
                :href="currentCandidateProfile.github_url"
                target="_blank"
                class="flex items-center justify-between p-4 bg-white/10 rounded-xl hover:bg-white/20 transition-colors group"
              >
                <span class="font-bold flex items-center gap-2"
                  ><Github class="w-4 h-4" /> GitHub</span
                >
                <ExternalLink class="w-4 h-4 opacity-50 group-hover:opacity-100" />
              </a>
              <a
                v-if="currentCandidateProfile.portfolio_url"
                :href="currentCandidateProfile.portfolio_url"
                target="_blank"
                class="flex items-center justify-between p-4 bg-white/10 rounded-xl hover:bg-white/20 transition-colors group"
              >
                <span class="font-bold flex items-center gap-2"
                  ><Briefcase class="w-4 h-4" /> Portfolio</span
                >
                <ExternalLink class="w-4 h-4 opacity-50 group-hover:opacity-100" />
              </a>

              <div
                v-if="
                  !currentCandidateProfile.linkedin_url &&
                  !currentCandidateProfile.github_url &&
                  !currentCandidateProfile.portfolio_url
                "
                class="text-slate-400 italic text-sm"
              >
                No social links provided.
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
