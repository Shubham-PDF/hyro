<script setup>
import { onMounted, reactive, watch } from 'vue'
import { useJobs } from '@/composables/useJobs'
import { Search, MapPin, Briefcase } from 'lucide-vue-next'
import JobViewCard from '@/views/applicant/JobViewCard.vue'
const { publicJobs, fetchPublicJobs, loading, currentPage, totalPages } = useJobs()
import { nextTick } from 'vue'

// Local State for Inputs
const filters = reactive({
  search: '',
  location: '',
})

// Debounce Timer
let debounceTimer = null

// 1. Fetch on Mount
onMounted(() => {
  fetchPublicJobs({ page: 1 }, false)
})

// 2. Debounced Search Logic
const performSearch = () => {
  clearTimeout(debounceTimer)

  debounceTimer = setTimeout(() => {
    fetchPublicJobs(
      {
        search: filters.search,
        location: filters.location,
        page: 1,
      },
      false,
    )
  }, 500)
}

// 3. Immediate Search
const forceSearch = () => {
  clearTimeout(debounceTimer)
  fetchPublicJobs(
    {
      search: filters.search,
      location: filters.location,
      page: 1,
    },
    false,
  )
}

// 4. Watch Filters
watch(filters, () => {
  performSearch()
})

// 5. Load More Handler
// const loadMore = () => {
//   const currentScroll = window.scrollY
//   if (currentPage.value < totalPages.value) {
//     const nextPage = currentPage.value + 1
//     fetchPublicJobs(
//       {
//         search: filters.search,
//         location: filters.location,
//         page: nextPage,
//       },
//       true, // append results
//     )
//     window.scrollTo({ top: currentScroll, behavior: 'instant' })
//   }
// }

const loadMore = async () => {
  // protect against double clicks
  if (loading.value) return

  // only proceed if there's another page
  if (currentPage.value >= totalPages.value) return

  const currentScroll = window.scrollY
  const nextPage = currentPage.value + 1

  try {
    // wait for the API and for your composable to append results
    await fetchPublicJobs(
      {
        search: filters.search,
        location: filters.location,
        page: nextPage,
      },
      true, // append results
    )

    // wait for Vue to update the DOM
    await nextTick()

    // tiny delay can help if images/fonts/layout still reflowing
    // await new Promise(res => setTimeout(res, 20))

    // restore scroll position
    window.scrollTo({ top: currentScroll, behavior: 'auto' })

    // remove focus from the button to avoid focus-caused scroll jitter
    if (document.activeElement instanceof HTMLElement) {
      document.activeElement.blur()
    }
  } catch (err) {
    console.error('Load more failed', err)
  }
}
</script>

<template>
  <div class="space-y-8 min-h-full block">
    <!-- PAGE HEADER -->
    <div class="space-y-6">
      <div>
        <h1 class="text-3xl font-bold text-slate-900 tracking-tight">Search Jobs</h1>
        <p class="text-slate-500 mt-1">Find the role that fits your life and career.</p>
      </div>

      <!-- SEARCH BAR -->
      <div
        class="bg-white p-2 rounded-2xl border border-slate-200 shadow-sm flex flex-col md:flex-row gap-2"
      >
        <!-- Search Input -->
        <div class="flex-1 relative group">
          <div
            class="absolute left-4 top-3.5 text-slate-400 group-focus-within:text-orange-500 transition-colors"
          >
            <Search class="w-5 h-5" />
          </div>

          <input
            v-model="filters.search"
            type="text"
            placeholder="Job title or keyword..."
            class="w-full pl-12 pr-4 py-3 rounded-xl bg-slate-50 border-none outline-none focus:bg-white focus:ring-2 focus:ring-orange-100 transition-all font-medium text-slate-900 placeholder:text-slate-400"
          />
        </div>

        <!-- Location Input -->
        <div class="flex-1 relative group">
          <div
            class="absolute left-4 top-3.5 text-slate-400 group-focus-within:text-orange-500 transition-colors"
          >
            <MapPin class="w-5 h-5" />
          </div>

          <input
            v-model="filters.location"
            type="text"
            placeholder="City or Remote..."
            class="w-full pl-12 pr-4 py-3 rounded-xl bg-slate-50 border-none outline-none focus:bg-white focus:ring-2 focus:ring-orange-100 transition-all font-medium text-slate-900 placeholder:text-slate-400"
          />
        </div>

        <button
          @click="forceSearch"
          class="bg-slate-900 text-white font-bold py-3 px-8 rounded-xl shadow-lg hover:bg-slate-800 transition-all active:scale-95 disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
        >
          Search
        </button>
      </div>
    </div>

    <!-- LOADING STATE -->
    <div v-if="loading" class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <div
        v-for="n in 4"
        :key="n"
        class="bg-white rounded-[2rem] p-8 border border-slate-100 h-64 animate-pulse flex flex-col justify-between"
      >
        <div class="space-y-4 flex flex-col items-center justify-center h-full">
          <div class="h-8 w-3/4 bg-slate-100 rounded-lg"></div>
          <div class="h-4 w-1/2 bg-slate-100 rounded-lg"></div>
        </div>
        <div class="flex justify-end">
          <div class="h-10 w-32 bg-slate-100 rounded-xl"></div>
        </div>
      </div>
    </div>

    <!-- EMPTY STATE -->
    <div
      v-else-if="publicJobs.length === 0"
      class="flex-1 flex flex-col items-center justify-center py-20 bg-white rounded-[2rem] border border-slate-100 border-dashed"
    >
      <div class="w-16 h-16 bg-slate-50 rounded-full flex items-center justify-center mb-4">
        <Briefcase class="w-8 h-8 text-slate-400" />
      </div>
      <h3 class="text-xl font-bold text-slate-900">No jobs found</h3>
      <p class="text-slate-500">Try changing your search terms.</p>
    </div>

    <!-- JOB LIST -->
    <div v-else class="space-y-8">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <!-- Using the reusable JobViewCard component -->
        <JobViewCard v-for="job in publicJobs" :key="job.job_id" :job="job" />
      </div>

      <!-- LOAD MORE BUTTON -->
      <!-- <h1>{{ totalPages }}</h1> -->
      <div v-if="currentPage < totalPages" class="flex justify-center py-8">
        <button
          @click="loadMore"
          :disabled="loading"
          class="bg-slate-900 text-white font-bold py-3 px-8 rounded-xl shadow-lg hover:bg-slate-800 transition-all active:scale-95 disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
        >
          <span
            v-if="loading"
            class="w-4 h-4 border-2 border-white/30 border-t-white rounded-full animate-spin"
          ></span>

          {{ loading ? 'Loading...' : 'Load More Jobs' }}
        </button>
      </div>
    </div>
  </div>
</template>
