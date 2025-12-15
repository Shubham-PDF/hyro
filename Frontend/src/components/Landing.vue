<script setup>
import { Check, Search, Lightbulb, Shield, Eye, Rocket, Menu } from 'lucide-vue-next'

// Navigation Links
const navLinks = [
  { name: 'Find Jobs', href: '#' },
  { name: 'For Recruiters', href: '#' },
  { name: 'Pricing', href: '#' },
  { name: 'Resources', href: '#' },
]
</script>

<template>
  <div
    class="min-h-screen bg-white font-sans text-slate-900 selection:bg-purple-100 selection:text-purple-900"
  >
    <nav class="fixed top-6 left-0 right-0 z-50 flex justify-center px-4">
      <div
        class="flex items-center justify-between w-full max-w-5xl bg-white/90 backdrop-blur-md border border-slate-200 rounded-full shadow-lg shadow-slate-200/50 px-6 py-3"
      >
        <div class="flex items-center gap-2">
          <span class="text-xl font-extrabold tracking-tight">Hyro</span>
        </div>

        <ul class="hidden md:flex items-center gap-8">
          <li v-for="link in navLinks" :key="link.name">
            <a
              :href="link.href"
              class="text-sm font-medium text-slate-600 hover:text-black transition-colors"
            >
              {{ link.name }}
            </a>
          </li>
        </ul>

        <div class="flex items-center gap-4">
          <button class="hidden sm:block text-sm font-semibold text-slate-600 hover:text-black">
            Sign in
          </button>
          <button
            class="bg-black hover:bg-slate-800 text-white text-sm font-semibold px-5 py-2.5 rounded-full transition-all active:scale-95"
          >
            Post a Job
          </button>
          <button class="md:hidden text-slate-600">
            <Menu class="w-6 h-6" />
          </button>
        </div>
      </div>
    </nav>

    <main class="pt-32 pb-20 px-4 flex flex-col items-center overflow-hidden">
      <div class="relative w-full max-w-[800px] h-[350px] md:h-[450px] mb-8 md:mb-4">
        <svg class="absolute inset-0 w-full h-full pointer-events-none z-0" viewBox="0 0 800 450">
          <line x1="400" y1="225" x2="200" y2="120" stroke="#E2E8F0" stroke-width="2" />
          <line x1="400" y1="225" x2="220" y2="330" stroke="#E2E8F0" stroke-width="2" />
          <line x1="400" y1="225" x2="100" y2="225" stroke="#E2E8F0" stroke-width="2" />

          <line x1="400" y1="225" x2="600" y2="120" stroke="#E2E8F0" stroke-width="2" />
          <line x1="400" y1="225" x2="620" y2="300" stroke="#E2E8F0" stroke-width="2" />
          <line x1="400" y1="225" x2="700" y2="200" stroke="#E2E8F0" stroke-width="2" />
        </svg>

        <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 z-20">
          <div
            class="w-24 h-24 md:w-32 md:h-32 bg-gradient-to-br from-purple-400 to-purple-600 rounded-3xl shadow-2xl shadow-purple-500/40 flex items-center justify-center animate-float-center"
          >
            <div class="bg-white/20 p-3 rounded-full backdrop-blur-sm">
              <Check class="w-10 h-10 text-white" stroke-width="3" />
            </div>
          </div>
        </div>

        <div class="absolute top-[15%] left-[20%] z-10 animate-float-slow">
          <div
            class="w-14 h-14 bg-yellow-300 rounded-2xl shadow-lg flex items-center justify-center transform -rotate-6 transition hover:rotate-0 hover:scale-110 duration-300"
          >
            <Lightbulb class="w-7 h-7 text-yellow-800" />
          </div>
        </div>

        <div class="absolute top-[65%] left-[22%] z-10 animate-float-fast">
          <div
            class="w-16 h-16 bg-sky-400 rounded-2xl shadow-lg shadow-sky-400/20 flex items-center justify-center transform rotate-3 transition hover:rotate-0 hover:scale-110 duration-300"
          >
            <Search class="w-8 h-8 text-white" />
          </div>
        </div>

        <div class="absolute top-[40%] left-[5%] md:left-[10%] z-10 animate-float-medium">
          <div
            class="w-16 h-16 md:w-20 md:h-20 bg-white p-1 rounded-3xl shadow-xl transform -rotate-3 transition hover:scale-110 duration-300"
          >
            <img
              src="https://i.pravatar.cc/150?img=33"
              alt="Applicant"
              class="w-full h-full object-cover rounded-2xl"
            />
          </div>
        </div>

        <div class="absolute top-[15%] right-[20%] z-10 animate-float-medium">
          <div
            class="w-16 h-16 bg-red-400 rounded-2xl shadow-lg shadow-red-400/20 flex items-center justify-center transform rotate-6 transition hover:rotate-0 hover:scale-110 duration-300"
          >
            <Shield class="w-8 h-8 text-white" />
          </div>
        </div>

        <div class="absolute top-[35%] right-[5%] md:right-[10%] z-10 animate-float-slow">
          <div
            class="w-20 h-20 bg-white rounded-3xl shadow-xl border border-slate-100 flex items-center justify-center transform rotate-3 transition hover:rotate-0 hover:scale-110 duration-300"
          >
            <Eye class="w-8 h-8 text-slate-700" />
          </div>
        </div>

        <div class="absolute top-[60%] right-[18%] z-10 animate-float-fast">
          <div
            class="w-14 h-14 bg-white p-1 rounded-2xl shadow-lg transform -rotate-6 transition hover:scale-110 duration-300"
          >
            <img
              src="https://i.pravatar.cc/150?img=5"
              alt="Recruiter"
              class="w-full h-full object-cover rounded-xl"
            />
          </div>
        </div>
      </div>

      <div class="text-center max-w-2xl relative z-30 mt-[-20px] md:mt-0">
        <h1
          class="text-5xl md:text-6xl font-extrabold text-slate-900 tracking-tight leading-[1.1] mb-6"
        >
          All-in-one HR <br />
          <span class="text-black">platform</span>
        </h1>

        <p class="text-lg md:text-xl text-slate-500 mb-10 leading-relaxed max-w-lg mx-auto">
          Hyro is a modern, all-in-one HR platform designed to perfectly fit your business needs and
          connect you with top talent.
        </p>

        <button
          class="bg-[#FF6B4A] hover:bg-[#ff5530] text-white text-lg font-bold py-4 px-10 rounded-2xl shadow-xl shadow-orange-500/20 transform transition hover:-translate-y-1 hover:shadow-2xl active:translate-y-0"
        >
          Request a Demo
        </button>
      </div>
    </main>
  </div>
</template>

<style scoped>
/* Custom Animations for the "Floating" effect 
  Tailwind supports animate-bounce, but we want something smoother and subtler.
*/
@keyframes float {
  0% {
    transform: translateY(0px);
  }
  50% {
    transform: translateY(-10px);
  }
  100% {
    transform: translateY(0px);
  }
}

.animate-float-slow {
  animation: float 6s ease-in-out infinite;
}
.animate-float-medium {
  animation: float 5s ease-in-out infinite;
}
.animate-float-fast {
  animation: float 4s ease-in-out infinite;
}
/* Center moves slightly differently to create depth */
.animate-float-center {
  animation: float 7s ease-in-out infinite;
}
</style>
