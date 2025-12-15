<script setup>
import { onMounted, reactive, ref } from 'vue'
import { useAuthStore } from '@/stores/auth'
import api from '@/api/axios'
import { User, Mail, Save, FileText, Linkedin, Github, Globe, Phone } from 'lucide-vue-next'

const authStore = useAuthStore()
const isSaving = ref(false)

// Form State
const profile = reactive({
  username: '',
  full_name: '',
  email: '',
  phone: '',
  about: '',
  skills: '',
  linkedin_url: '',
  github_url: '',
  portfolio_url: '',
})

// Load user data
onMounted(async () => {
  await authStore.fetchUser()
  const user = authStore.user

  if (user) {
    profile.username = user.username || ''
    profile.full_name = user.full_name || ''
    profile.email = user.email || ''
    profile.phone = user.phone || ''
    profile.about = user.about || ''
    profile.linkedin_url = user.linkedin_url || ''
    profile.github_url = user.github_url || ''
    profile.portfolio_url = user.portfolio_url || ''
    profile.skills = user.skills ? user.skills.join(', ') : ''
  }
})

// Save Profile
const handleSave = async () => {
  isSaving.value = true

  try {
    const skillsArray = profile.skills
      .split(',')
      .map((s) => s.trim())
      .filter(Boolean)

    const payload = {
      username: profile.username,
      full_name: profile.full_name,
      phone: profile.phone,
      about: profile.about,
      linkedin_url: profile.linkedin_url,
      github_url: profile.github_url,
      portfolio_url: profile.portfolio_url,
      skills: skillsArray,
    }

    await api.patch('/auth/me/update/', payload)
    await authStore.fetchUser()
    alert('Profile updated successfully!')
  } catch (err) {
    console.error(err)
    alert('Failed to update profile.')
  } finally {
    isSaving.value = false
  }
}
</script>

<template>
  <div class="max-w-4xl mx-auto space-y-10 pb-16">
    <!-- HEADER -->
    <div class="text-center md:text-left">
      <h1 class="text-4xl font-bold text-slate-900">Your Profile</h1>
      <p class="text-slate-500 mt-1 text-sm">
        Manage your personal details and showcase your professional identity.
      </p>
    </div>

    <!-- PROFILE CARD -->
    <div class="bg-white rounded-[2rem] border border-slate-200 shadow-lg overflow-hidden">
      <!-- Banner -->
      <div class="h-36 bg-gradient-to-r from-slate-900 to-slate-800 relative">
        <div class="absolute -bottom-14 left-8">
          <div class="w-28 h-28 bg-white rounded-2xl p-1.5 shadow-2xl">
            <div
              class="w-full h-full bg-slate-100 rounded-xl flex items-center justify-center text-4xl font-bold text-slate-500"
            >
              {{ profile.full_name ? profile.full_name.charAt(0).toUpperCase() : 'U' }}
            </div>
          </div>
        </div>
      </div>

      <div class="pt-20 px-8 pb-12">
        <form @submit.prevent="handleSave" class="space-y-10">
          <!-- BASIC INFO GRID -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            <!-- Full Name -->
            <div>
              <label class="font-semibold text-slate-700 text-sm mb-2 block">Full Name</label>
              <div class="relative">
                <User class="absolute left-4 top-3.5 w-5 h-5 text-slate-400" />
                <input
                  v-model="profile.full_name"
                  type="text"
                  class="w-full pl-12 pr-4 py-3 border border-slate-200 rounded-xl bg-white text-slate-900 focus:ring-2 outline-none transition-all"
                  placeholder="Shubham"
                />
              </div>
            </div>

            <!-- Email -->
            <div>
              <label class="font-semibold text-slate-700 text-sm mb-2 block">Email</label>
              <div class="relative">
                <Mail class="absolute left-4 top-3.5 w-5 h-5 text-slate-400" />
                <input
                  v-model="profile.email"
                  type="email"
                  class="w-full pl-12 pr-4 py-3 border border-slate-200 rounded-xl bg-white focus:ring-2 outline-none transition-all"
                />
              </div>
            </div>

            <!-- Phone -->
            <div>
              <label class="font-semibold text-slate-700 text-sm mb-2 block">Phone</label>
              <div class="relative">
                <Phone class="absolute left-4 top-3.5 w-5 h-5 text-slate-400" />
                <input
                  v-model="profile.phone"
                  type="text"
                  class="w-full pl-12 pr-4 py-3 border border-slate-200 rounded-xl bg-white focus:ring-2 outline-none transition-all"
                  placeholder="+91 9876543210"
                />
              </div>
            </div>
          </div>

          <!-- ABOUT -->
          <div>
            <label class="font-semibold text-slate-700 text-sm mb-2 block">About</label>
            <textarea
              v-model="profile.about"
              rows="3"
              class="w-full p-4 border border-slate-200 bg-white rounded-xl focus:ring-2 outline-none transition-all text-sm"
              placeholder="Write a short bio about yourself, your strengths, and goals..."
            ></textarea>
          </div>


          <!-- SAVE BUTTON -->
          <div class="pt-4 flex justify-end">
            <button
              type="submit"
              :disabled="isSaving"
              class="bg-slate-900 hover:bg-slate-800 text-white px-8 py-3.5 rounded-xl font-bold transition-all active:scale-95 flex items-center gap-2 shadow-lg shadow-slate-900/10 disabled:opacity-60"
            >
              <Save class="w-4 h-4" />
              {{ isSaving ? 'Saving...' : 'Save Changes' }}
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
