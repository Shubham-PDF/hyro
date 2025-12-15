<script setup>
  import { reactive, ref, onMounted, computed, watch } from 'vue'
  import { useRouter, useRoute } from 'vue-router'
  import { useJobs } from '@/composables/useJobs'
  import api from '@/api/axios'
  import { ArrowLeft, CheckCircle, AlertTriangle, X, Sparkles, Info } from 'lucide-vue-next'
  
  const router = useRouter()
  const route = useRoute()
  const { createJob, updateJob, fetchJobById, currentJob } = useJobs()
  
  const isSubmitting = ref(false)
  const errorMessage = ref('')
  const isGeneratingKeywords = ref(false)
  const keywordError = ref('')
  const hasGeneratedKeywords = ref(false)
  const showSuccessToast = ref(false)
  const showErrorToast = ref(false)
  
  //to check are we editng
  const isEditMode = computed(() => !!route.params.id)
  
  const form = reactive({
    title: '',
    company_name: '',
    location: '',
    description: '',
    requirements: '',
    salary_min: null,
    salary_max: null,
    experience_required: null,
    keywords: '',
  })

  
  const resetForm = () => {
    Object.assign(form, {
      title: '',
      company_name: '',
      location: '',
      description: '',
      requirements: '',
      salary_min: null,
      salary_max: null,
      experience_required: null,
      keywords: ''
    })
    hasGeneratedKeywords.value = false
    keywordError.value = ''
  }

  // Populate Form (reusable) 
  const populateForm = async (id) => {
    await fetchJobById(id)
    if (currentJob.value) {
      Object.assign(form, {
        title: currentJob.value.title,
        company_name: currentJob.value.company_name,
        location: currentJob.value.location,
        description: currentJob.value.description,
        requirements: currentJob.value.requirements,
        salary_min: currentJob.value.salary_min,
        salary_max: currentJob.value.salary_max,
        experience_required: currentJob.value.experience_required,
        keywords: Array.isArray(currentJob.value.keywords) 
          ? currentJob.value.keywords.join(', ') 
          : (currentJob.value.keywords || '')
      })
    }
  }
  
  //  On Mount: Check logic
  onMounted(async () => {
    if (isEditMode.value) {
      await populateForm(route.params.id)
    } else {
      resetForm() // Ensure clean slate on fresh load
    }
  })

  // Detects switching between "Create" and "Edit" without reloading
  watch(
    () => route.params.id,
    async (newId) => {
      if (newId) {
        
        await populateForm(newId)
      } else {
        
        resetForm()
      }
    }
  )
  
  const generateKeywords = async () => {
    if (hasGeneratedKeywords.value || !form.description.trim() || form.keywords.trim()) {
      return
    }
    keywordError.value = ''
    isGeneratingKeywords.value = true
    try {
      const res = await api.post('/ai/job-keywords/', { description: form.description })
      form.keywords = res.data.keywords.join(', ')
      hasGeneratedKeywords.value = true
    } catch (error) {
      console.error(error)
      keywordError.value = 'Failed to auto-generate keywords.'
    } finally {
      isGeneratingKeywords.value = false
    }
  }
  
  const handleSubmit = async () => {
    isSubmitting.value = true
    errorMessage.value = ''
    showSuccessToast.value = false
    showErrorToast.value = false
  
    try {
      const payload = {
        ...form,
        salary_min: Number(form.salary_min) || 0,
        salary_max: Number(form.salary_max) || 0,
        experience_required: Number(form.experience_required) || 0,
        keywords: form.keywords.split(',').map((k) => k.trim()).filter((k) => k),
      }
  
      if (isEditMode.value) {
        await updateJob(route.params.id, payload)
      } else {
        await createJob(payload)
      }
  
      showSuccessToast.value = true
      setTimeout(() => {
        router.push('/recruiter/jobs')
      }, 2000)
  
    } catch (error) {
      console.error(error)
      errorMessage.value = error.response?.data?.message || 'Failed to save job.'
      showErrorToast.value = true
      setTimeout(() => { showErrorToast.value = false }, 5000)
    } finally {
      if (showErrorToast.value) isSubmitting.value = false
    }
  }
</script>
  
  <template>
    <div class="flex h-screen bg-gray-50">
      <main class="flex-1 overflow-y-auto bg-gray-50 relative p-6">
        <div class="fixed top-4 right-4 z-50 space-y-3">
          <div v-if="showSuccessToast" class="flex items-center p-4 bg-primary-orange text-white rounded-lg shadow-xl min-w-80 transition-opacity duration-300">
            <CheckCircle class="w-5 h-5 mr-2" />
            <span class="font-medium">Success! Job {{ isEditMode ? 'updated' : 'posted' }}. Redirecting...</span>
          </div>
          <div v-if="showErrorToast" class="flex items-center p-4 bg-red-600 text-white rounded-lg shadow-xl min-w-80 transition-opacity duration-300">
            <AlertTriangle class="w-5 h-5 mr-2" />
            <span class="font-medium">{{ errorMessage }}</span>
            <button @click="showErrorToast = false" class="ml-auto text-white/80 hover:text-white"><X class="w-4 h-4" /></button>
          </div>
        </div>
  
        <div class="max-w-4xl mx-auto">
          <div class="flex flex-col mb-8">
            <button @click="router.back()" class="text-gray-600 hover:text-primary-orange flex items-center gap-2 mb-6 transition-colors font-medium self-start">
              <ArrowLeft class="w-4 h-4" /> Back to Dashboard
            </button>
  
            <div class="flex justify-between items-center pb-4">
              <div>
                <h1 class="text-3xl font-bold text-gray-900 tracking-tight">
                  {{ isEditMode ? 'Edit Job Posting' : 'Post a New Job' }}
                </h1>
                <p class="text-gray-500 mt-1 text-base">
                  {{ isEditMode ? 'Update job details and requirements.' : 'Find your next great hire and expand your team.' }}
                </p>
              </div>
  
              <button
                type="submit"
                form="job-post-form"
                :disabled="isSubmitting"
                class="bg-primary-orange text-white px-6 py-2 rounded-lg font-semibold shadow-md shadow-orange-300/50 hover:bg-orange-700 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
              >
                {{ isSubmitting ? 'Saving...' : (isEditMode ? 'Update Job' : 'Publish Job') }}
              </button>
            </div>
          </div>
  
          <div class="bg-white p-8 rounded-xl border border-gray-200 shadow-lg space-y-6">
            <form id="job-post-form" @submit.prevent="handleSubmit" class="space-y-8">
              <div class="space-y-6">
                <h2 class="text-xl font-bold text-gray-800 border-b pb-3">Basic Information</h2>
  
                <div>
                  <label for="job-title" class="block text-sm font-semibold text-gray-700 mb-2">Job Title</label>
                  <input id="job-title" v-model="form.title" type="text" required placeholder="e.g., Senior Frontend Developer" class="w-full px-4 py-2.5 rounded-lg border border-gray-300 focus:border-primary-orange focus:ring-1 focus:ring-primary-orange outline-none transition-all" />
                </div>
  
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <div>
                    <label for="company-name" class="block text-sm font-semibold text-gray-700 mb-2">Company Name</label>
                    <input id="company-name" v-model="form.company_name" type="text" required placeholder="e.g., Innovatech Solutions" class="w-full px-4 py-2.5 rounded-lg border border-gray-300 focus:border-primary-orange focus:ring-1 focus:ring-primary-orange outline-none transition-all" />
                  </div>
                  <div>
                    <label for="location" class="block text-sm font-semibold text-gray-700 mb-2">Location</label>
                    <input id="location" v-model="form.location" type="text" required placeholder="e.g., Remote or New York, NY" class="w-full px-4 py-2.5 rounded-lg border border-gray-300 focus:border-primary-orange focus:ring-1 focus:ring-primary-orange outline-none transition-all" />
                  </div>
                </div>
              </div>
  
              <div class="space-y-6">
                <h2 class="text-xl font-bold text-gray-800 border-b pb-3 pt-4">Role Details</h2>
  
                <div>
                  <label for="job-description" class="block text-sm font-semibold text-gray-700 mb-1">Job Description</label>
                  <p class="text-xs text-gray-500 mb-2 font-normal">Add all the necessary must-have details, roles, and tech details over here</p>
                  <textarea id="job-description" v-model="form.description" rows="5" required @blur="generateKeywords" placeholder="Describe the role, responsibilities, and team." class="w-full px-4 py-2.5 rounded-lg border border-gray-300 focus:border-primary-orange focus:ring-1 focus:ring-primary-orange outline-none transition-all"></textarea>
                  <p v-if="keywordError" class="mt-2 text-sm text-red-500 font-medium">{{ keywordError }}</p>
                </div>
  
                <div>
                  <label for="requirements" class="block text-sm font-semibold text-gray-700 mb-2">Nice to have</label>
                  <textarea id="requirements" v-model="form.requirements" rows="3" required placeholder="List bonus skills and qualifications." class="w-full px-4 py-2.5 rounded-lg border border-gray-300 focus:border-primary-orange focus:ring-1 focus:ring-primary-orange outline-none transition-all"></textarea>
                </div>
  
                <div>
                  <label for="keywords" class="block text-sm font-semibold text-gray-700 mb-2">Keywords (Comma separated)</label>
                  
                  <div class="relative">
                     <input 
                        id="keywords" 
                        v-model="form.keywords" 
                        type="text" 
                        required 
                        placeholder="e.g., Vue.js, Tailwind CSS, Javascript, Agile" 
                        class="w-full px-4 py-2.5 rounded-lg border border-gray-300 focus:border-primary-orange focus:ring-1 focus:ring-primary-orange outline-none transition-all pr-10" 
                      />
                      
                      <div v-if="isGeneratingKeywords" class="absolute right-3 top-1/2 -translate-y-1/2 flex items-center gap-2 pointer-events-none">
                         <Sparkles class="w-5 h-5 text-primary-orange animate-pulse" />
                      </div>
                  </div>
  
                  <div class="mt-3 bg-amber-50 border border-amber-200 rounded-lg p-3 flex items-start gap-3">
                     <Info class="w-5 h-5 text-amber-600 shrink-0 mt-0.5" />
                     <p class="text-sm text-amber-800">
                        <strong>Note:</strong> These keywords are AI-generated based on your description. They might not be 100% accurate. 
                        Please <span class="underline decoration-amber-500/50">review and edit them</span> before submission, as they are critical for finding the best applicants.
                     </p>
                  </div>
                </div>
              </div>
  
              <div class="space-y-6">
                <h2 class="text-xl font-bold text-gray-800 border-b pb-3 pt-4">Compensation & Experience</h2>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                  <div>
                    <label for="salary-min" class="block text-sm font-semibold text-gray-700 mb-2">Salary Min</label>
                    <div class="relative">
                      <span class="absolute left-3 top-1/2 -translate-y-1/2 text-gray-500 font-bold">₹</span>
                      <input id="salary-min" v-model="form.salary_min" type="text" required placeholder="80000" class="w-full pl-7 pr-4 py-2.5 rounded-lg border border-gray-300 focus:border-primary-orange focus:ring-1 focus:ring-primary-orange outline-none transition-all" />
                    </div>
                  </div>
                  <div>
                    <label for="salary-max" class="block text-sm font-semibold text-gray-700 mb-2">Salary Max</label>
                    <div class="relative">
                      <span class="absolute left-3 top-1/2 -translate-y-1/2 text-gray-500 font-bold">₹</span>
                      <input id="salary-max" v-model="form.salary_max" type="text" required placeholder="120000" class="w-full pl-7 pr-4 py-2.5 rounded-lg border border-gray-300 focus:border-primary-orange focus:ring-1 focus:ring-primary-orange outline-none transition-all" />
                    </div>
                  </div>
                  <div>
                    <label for="experience" class="block text-sm font-semibold text-gray-700 mb-2">Experience (Years)</label>
                    <input id="experience" v-model="form.experience_required" type="text" required placeholder="3" class="w-full px-4 py-2.5 rounded-lg border border-gray-300 focus:border-primary-orange focus:ring-1 focus:ring-primary-orange outline-none transition-all" />
                  </div>
                </div>
              </div>
  
              <button type="submit" class="hidden"></button>
            </form>
          </div>
        </div>
      </main>
    </div>
  </template>
  
  <style scoped>
  .text-primary-orange { color: #f97316; }
  .focus\:border-primary-orange:focus { border-color: #f97316; }
  .focus\:ring-primary-orange:focus { --tw-ring-color: #fb923c; }
  .bg-primary-orange { background-color: #f97316; }
  .hover\:bg-orange-700:hover { background-color: #c2410c; }
  </style>