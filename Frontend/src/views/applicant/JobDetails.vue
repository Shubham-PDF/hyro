<script setup>
  import { onMounted, ref } from 'vue'
  import { useRoute, useRouter } from 'vue-router'
  import { useJobs } from '@/composables/useJobs'
  import api from '@/api/axios'
  import {
    ArrowLeft,
    MapPin,
    Banknote,
    Briefcase,
    Clock,
    Users,
    CheckCircle,
    UploadCloud,
    X,
    FileText,
    Ban // 🆕 Imported Ban icon for closed state
  } from 'lucide-vue-next'
  
  const route = useRoute()
  const router = useRouter()
  const { currentJob, fetchJobById, loading } = useJobs()
  
  // ---  MODAL & APPLICATION STATE ---
  const isApplyModalOpen = ref(false)
  const selectedFile = ref(null)
  const isSubmitting = ref(false)
  const uploadStatus = ref(null) // null | 'success' | 'error'
  
  // Fetch Data on Load
  onMounted(() => {
    fetchJobById(route.params.id)
  })
  
  // --- HELPERS ---
  // 🆕 Changed from timeAgo to explicit Date format
  const formatDate = (dateString) => {
    if (!dateString) return 'Recently'
    return new Date(dateString).toLocaleDateString('en-US', {
      month: 'short',
      day: 'numeric',
      year: 'numeric'
    })
  }
  
  const formatSalary = (min, max) => {
    if (!min || !max) return 'Competitive'
    return `₹${(min / 1000).toFixed(0)}k - ₹${(max / 1000).toFixed(0)}k`
  }
  
  // --- FOR FILE HANDLING ---
  const handleFileChange = (event) => {
    const file = event.target.files[0]
    if (file && file.type === 'application/pdf') {
      selectedFile.value = file
    } else {
      alert('Please upload a PDF file.')
    }
  }
  
  // --- SUBMIT APPLICATION ---
  const submitApplication = async () => {
    if (!selectedFile.value || !currentJob.value) return
  
    isSubmitting.value = true
    uploadStatus.value = null
  
    try {
      const formData = new FormData()
      formData.append('resume', selectedFile.value)
  
      // POST /applications/<job_id>/apply/
      await api.post(`/applications/${currentJob.value.job_id}/apply/`, formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      })
  
      uploadStatus.value = 'success'
  
      // Auto-close after 2.5 seconds
      setTimeout(() => {
        isApplyModalOpen.value = false
        uploadStatus.value = null
        selectedFile.value = null
      }, 2500)
    } catch (error) {
      console.error('Application failed', error)
      uploadStatus.value = 'error'
    } finally {
      isSubmitting.value = false
    }
  }
  </script>
  
  <template>
    <div class="relative min-h-screen pb-24 md:pb-12">
      <div v-if="loading" class="flex items-center justify-center h-[60vh]">
        <div
          class="animate-spin w-12 h-12 border-4 border-orange-500 border-t-transparent rounded-full"
        ></div>
      </div>
  
      <div v-else-if="currentJob" class="max-w-6xl mx-auto px-4">
        <button
          @click="router.back()"
          class="mb-6 flex items-center gap-2 text-slate-500 hover:text-slate-900 font-bold transition-colors mt-6"
        >
          <ArrowLeft class="w-5 h-5" /> Back to Jobs
        </button>
  
        <div
          class="bg-white rounded-[2rem] border border-slate-200 p-8 md:p-10 shadow-sm mb-8 relative overflow-hidden"
        >
          <div
            class="absolute top-0 right-0 w-64 h-64 bg-orange-50 rounded-full blur-3xl -mr-16 -mt-16 pointer-events-none"
          ></div>
  
          <div class="relative z-10 flex flex-col md:flex-row justify-between gap-6 items-start">
            <div>
              <div class="flex items-center gap-4 mb-5">
                <div
                  class="w-16 h-16 bg-slate-900 text-white rounded-2xl flex items-center justify-center text-2xl font-bold shadow-lg"
                >
                  {{ currentJob.company_name.charAt(0) }}
                </div>
                <div>
                  <h1
                    class="text-3xl md:text-4xl font-extrabold text-slate-900 tracking-tight leading-tight"
                  >
                    {{ currentJob.title }}
                  </h1>
                  <p class="text-lg text-slate-500 font-medium">{{ currentJob.company_name }}</p>
                </div>
              </div>
  
              <div class="flex flex-wrap gap-3">
                <span
                  class="inline-flex items-center gap-1.5 px-4 py-2 rounded-xl text-sm font-bold bg-slate-50 text-slate-700 border border-slate-100"
                >
                  <MapPin class="w-4 h-4 text-slate-400" /> {{ currentJob.location }}
                </span>
                <span
                  class="inline-flex items-center gap-1.5 px-4 py-2 rounded-xl text-sm font-bold bg-emerald-50 text-emerald-700 border border-emerald-100"
                >
                  <Banknote class="w-4 h-4 text-emerald-500" />
                  {{ formatSalary(currentJob.salary_min, currentJob.salary_max) }}
                </span>
                <span
                  class="inline-flex items-center gap-1.5 px-4 py-2 rounded-xl text-sm font-bold bg-blue-50 text-blue-700 border border-blue-100"
                >
                  <Briefcase class="w-4 h-4 text-blue-500" /> {{ currentJob.experience_required }}+
                  Years Experience
                </span>
              </div>
            </div>
  
            <button
              @click="isApplyModalOpen = true"
              :disabled="!currentJob.is_active"
              class="hidden md:flex text-white px-8 py-4 rounded-xl font-bold text-lg shadow-xl transition-all active:scale-95 items-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed disabled:shadow-none"
              :class="currentJob.is_active 
                ? 'bg-slate-900 hover:bg-slate-800 shadow-slate-900/20' 
                : 'bg-slate-400'"
            >
              {{ currentJob.is_active ? 'Apply Now' : 'Applications Closed' }}
              <component :is="currentJob.is_active ? CheckCircle : Ban" class="w-5 h-5" />
            </button>
          </div>
        </div>
  
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
          <div class="lg:col-span-2 space-y-8">
            <div class="bg-white rounded-[2rem] border border-slate-200 p-8 shadow-sm">
              <h3
                class="text-xl font-bold text-slate-900 mb-6 border-b border-slate-100 pb-4 flex items-center gap-2"
              >
                <FileText class="w-5 h-5 text-orange-500" /> About the Role
              </h3>
              <div
                class="prose prose-slate max-w-none text-slate-600 leading-relaxed whitespace-pre-line"
              >
                {{ currentJob.description }}
              </div>
            </div>
  
            <div class="bg-white rounded-[2rem] border border-slate-200 p-8 shadow-sm">
              <h3
                class="text-xl font-bold text-slate-900 mb-6 border-b border-slate-100 pb-4 flex items-center gap-2"
              >
                <CheckCircle class="w-5 h-5 text-orange-500" /> Nice to Have
              </h3>
              <div
                class="prose prose-slate max-w-none text-slate-600 leading-relaxed whitespace-pre-line"
              >
                {{ currentJob.requirements }}
              </div>
            </div>
          </div>
  
          <div class="space-y-6">
            <div class="bg-white rounded-[2rem] border border-slate-200 p-6 shadow-sm sticky top-6">
              <h3 class="text-lg font-bold text-slate-900 mb-6">Job Overview</h3>
  
              <div class="space-y-6">
                <div class="flex items-center gap-4">
                  <div class="p-3 bg-slate-50 rounded-xl text-slate-500">
                    <Clock class="w-6 h-6" />
                  </div>
                  <div>
                    <p class="text-xs font-bold text-slate-400 uppercase tracking-wide">Posted</p>
                    <p class="text-slate-900 font-bold">{{ formatDate(currentJob.created_at) }}</p>
                  </div>
                </div>
  
                <div class="flex items-center gap-4">
                  <div class="p-3 bg-slate-50 rounded-xl text-slate-500">
                    <Users class="w-6 h-6" />
                  </div>
                  <div>
                    <p class="text-xs font-bold text-slate-400 uppercase tracking-wide">Applicants</p>
                    <p class="text-slate-900 font-bold">
                      {{ currentJob.applicant_count }} people applied
                    </p>
                  </div>
                </div>
  
                <div class="flex items-center gap-4">
                  <div class="p-3 bg-slate-50 rounded-xl text-slate-500">
                    <CheckCircle class="w-6 h-6" />
                  </div>
                  <div>
                    <p class="text-xs font-bold text-slate-400 uppercase tracking-wide">Status</p>
                    <span
                      class="inline-block mt-1 px-2.5 py-1 rounded-md text-xs font-extrabold uppercase tracking-wide"
                      :class="
                        currentJob.is_active
                          ? 'bg-emerald-100 text-emerald-700'
                          : 'bg-red-100 text-red-700'
                      "
                    >
                      {{ currentJob.is_active ? 'Active' : 'Closed' }}
                    </span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
  
      <div
        class="fixed bottom-0 left-0 right-0 p-4 bg-white border-t border-slate-200 md:hidden z-30 shadow-[0_-4px_6px_-1px_rgba(0,0,0,0.05)]"
      >
        <button
          @click="isApplyModalOpen = true"
          :disabled="!currentJob?.is_active"
          class="w-full text-white font-bold py-4 rounded-xl shadow-lg flex justify-center items-center gap-2 transition-transform disabled:opacity-60 disabled:cursor-not-allowed"
          :class="currentJob?.is_active 
            ? 'bg-slate-900 active:scale-95' 
            : 'bg-slate-400'"
        >
          {{ currentJob?.is_active ? 'Apply Now' : 'Applications Closed' }}
        </button>
      </div>
  
      <Teleport to="body">
        <div v-if="isApplyModalOpen" class="fixed inset-0 z-50 flex items-center justify-center p-4">
          <div
            class="absolute inset-0 bg-slate-900/60 backdrop-blur-sm transition-opacity"
            @click="isApplyModalOpen = false"
          ></div>
  
          <div
            class="relative w-full max-w-lg bg-white rounded-[2rem] shadow-2xl p-8 transform transition-all animate-float-fast overflow-hidden"
          >
            <button
              @click="isApplyModalOpen = false"
              class="absolute top-6 right-6 text-slate-400 hover:text-slate-900 transition-colors"
            >
              <X class="w-6 h-6" />
            </button>
  
            <div v-if="uploadStatus === 'success'" class="text-center py-10">
              <div
                class="w-24 h-24 bg-emerald-100 text-emerald-600 rounded-full flex items-center justify-center mx-auto mb-6 animate-bounce"
              >
                <CheckCircle class="w-12 h-12" />
              </div>
              <h2 class="text-3xl font-bold text-slate-900 mb-2">Application Sent!</h2>
              <p class="text-slate-500 font-medium">Your resume has been sent to the recruiter.</p>
            </div>
  
            <div v-else-if="uploadStatus === 'error'" class="text-center py-10">
              <div
                class="w-20 h-20 bg-red-100 text-red-600 rounded-full flex items-center justify-center mx-auto mb-6"
              >
                <X class="w-10 h-10" />
              </div>
              <h2 class="text-2xl font-bold text-slate-900 mb-2">Upload Failed</h2>
              <p class="text-slate-500 mb-6">Something went wrong. Please try again.</p>
              <button @click="uploadStatus = null" class="text-slate-900 font-bold underline">
                Try Again
              </button>
            </div>
  
            <div v-else>
              <h2 class="text-2xl font-bold text-slate-900 mb-2">
                Apply for {{ currentJob?.title }}
              </h2>
              <p class="text-slate-500 mb-8 font-medium">Upload your resume to continue.</p>
  
              <div class="mb-8">
                <label
                  class="flex flex-col items-center justify-center w-full h-52 border-2 border-dashed border-slate-300 rounded-2xl cursor-pointer hover:border-orange-500 hover:bg-orange-50/30 transition-all group relative"
                  :class="{ 'border-emerald-500 bg-emerald-50/30': selectedFile }"
                >
                  <div class="flex flex-col items-center justify-center pt-5 pb-6 text-center px-4">
                    <div
                      class="p-4 bg-slate-50 rounded-full mb-3 group-hover:scale-110 transition-transform shadow-sm"
                    >
                      <UploadCloud
                        class="w-8 h-8 text-slate-400 group-hover:text-orange-500"
                        :class="{ 'text-emerald-500': selectedFile }"
                      />
                    </div>
  
                    <p class="mb-2 text-sm text-slate-600 font-medium">
                      <span v-if="selectedFile" class="text-slate-900 font-bold block text-lg">{{
                        selectedFile.name
                      }}</span>
                      <span v-else
                        ><span class="font-bold text-orange-600">Click to upload</span> or drag and
                        drop</span
                      >
                    </p>
                    <p v-if="!selectedFile" class="text-xs text-slate-400 font-medium">
                      PDF only (Max 5MB)
                    </p>
                  </div>
                  <input
                    type="file"
                    class="hidden"
                    accept="application/pdf"
                    @change="handleFileChange"
                  />
                </label>
              </div>
  
              <div class="flex gap-4">
                <button
                  @click="isApplyModalOpen = false"
                  class="flex-1 py-4 font-bold text-slate-600 hover:bg-slate-50 rounded-xl transition-colors"
                >
                  Cancel
                </button>
                <button
                  @click="submitApplication"
                  :disabled="!selectedFile || isSubmitting"
                  class="flex-1 py-4 bg-slate-900 text-white font-bold rounded-xl shadow-lg hover:bg-slate-800 disabled:opacity-50 disabled:cursor-not-allowed transition-all flex justify-center items-center gap-2"
                >
                  <span v-if="isSubmitting" class="animate-pulse">Sending...</span>
                  <span v-else>Submit Application</span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </Teleport>
    </div>
  </template>