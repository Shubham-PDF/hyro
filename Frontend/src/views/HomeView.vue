<!-- <script setup>
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
</style> -->
<script setup>
import {
  Check,
  Search,
  Lightbulb,
  Shield,
  Eye,
  Users,
  Target,
  Zap,
  TrendingUp,
  Award,
  Clock,
  Briefcase,
  UserCheck,
  Building2,
  Mail,
  Linkedin,
  Twitter,
} from 'lucide-vue-next'
import { ref } from 'vue'

const mobileMenuOpen = ref(false)

const navLinks = [
  { name: 'Why Hyro', href: '#why-hyro' },
  { name: 'For Applicants', href: '#for-applicants' },
  { name: 'For Recruiters', href: '#for-recruiters' },
]

const whyHyroFeatures = [
  {
    icon: Zap,
    title: 'Lightning Fast',
    description:
      'Streamline your hiring process with automated workflows and instant candidate matching.',
  },
  {
    icon: Shield,
    title: 'Secure & Compliant',
    description: 'Enterprise-grade security with full GDPR compliance and data protection.',
  },
  {
    icon: Target,
    title: 'Smart Matching',
    description: 'AI-powered algorithms connect the right talent with the right opportunities.',
  },
  {
    icon: TrendingUp,
    title: 'Data-Driven Insights',
    description: 'Make informed decisions with comprehensive analytics and reporting tools.',
  },
]

const applicantFeatures = [
  {
    icon: Search,
    title: 'Easy Job Discovery',
    description: 'Browse thousands of opportunities tailored to your skills and preferences.',
  },
  {
    icon: UserCheck,
    title: 'Smart Profile',
    description: 'Create a standout profile that showcases your experience and achievements.',
  },
  {
    icon: Clock,
    title: 'Quick Applications',
    description: 'Apply to multiple jobs with one click using your saved profile.',
  },
  {
    icon: Award,
    title: 'Career Growth',
    description: 'Access resources, tips, and tools to accelerate your career journey.',
  },
]

const recruiterFeatures = [
  {
    icon: Users,
    title: 'Talent Pool Management',
    description: 'Build and manage your talent database with advanced filtering and search.',
  },
  {
    icon: Briefcase,
    title: 'Job Posting',
    description: 'Create and publish job listings across multiple platforms instantly.',
  },
  {
    icon: Target,
    title: 'Candidate Screening',
    description: 'Automated screening and ranking to find the best candidates faster.',
  },
  {
    icon: Building2,
    title: 'Team Collaboration',
    description: 'Collaborate seamlessly with hiring managers and team members.',
  },
]
</script>

<template>
  <div
    class="min-h-screen bg-white font-sans text-slate-900 selection:bg-purple-100 selection:text-purple-900"
  >
    <!-- Navigation -->
    <nav class="fixed top-6 left-0 right-0 z-50 flex justify-center px-4">
      <div
        class="flex items-center justify-between w-full max-w-6xl bg-white/90 backdrop-blur-md border border-slate-200 rounded-full shadow-lg shadow-slate-200/50 px-6 py-3"
      >
        <div class="flex items-center gap-2">
          <span
            class="text-xl font-extrabold tracking-tight bg-gradient-to-r from-orange-600 to-orange-400 bg-clip-text text-transparent"
            >Hyro</span
          >
        </div>

        <ul class="hidden md:flex items-center gap-8">
          <li v-for="link in navLinks" :key="link.name">
            <a
              :href="link.href"
              class="text-sm font-medium text-slate-600 hover:text-orange-600 transition-colors"
            >
              {{ link.name }}
            </a>
          </li>
        </ul>

        <div class="flex items-center gap-3">
          <router-link
            to="/login"
            class="hidden sm:block text-sm font-semibold text-slate-600 hover:text-orange-600 transition-colors"
          >
            Log In
          </router-link>
          <router-link
            to="/signup"
            class="bg-gradient-to-r from-orange-500 to-orange-600 hover:from-orange-600 hover:to-orange-700 text-white text-sm font-semibold px-5 py-2.5 rounded-full transition-all active:scale-95 shadow-lg shadow-orange-500/30"
          >
            Sign Up
          </router-link>
          <button @click="mobileMenuOpen = !mobileMenuOpen" class="md:hidden text-slate-600">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M4 6h16M4 12h16M4 18h16"
              />
            </svg>
          </button>
        </div>
      </div>
    </nav>

    <!-- Mobile Menu -->
    <div
      v-if="mobileMenuOpen"
      class="fixed inset-0 z-40 bg-black/20 backdrop-blur-sm md:hidden"
      @click="mobileMenuOpen = false"
    >
      <div class="fixed top-24 left-4 right-4 bg-white rounded-2xl shadow-2xl p-6" @click.stop>
        <ul class="space-y-4">
          <li v-for="link in navLinks" :key="link.name">
            <a
              :href="link.href"
              class="block text-lg font-medium text-slate-700 hover:text-purple-600"
              @click="mobileMenuOpen = false"
            >
              {{ link.name }}
            </a>
          </li>
          <li class="pt-4 border-t border-slate-200">
            <router-link
              to="/login"
              class="block text-lg font-medium text-slate-700 hover:text-orange-600"
              @click="mobileMenuOpen = false"
            >
              Log In
            </router-link>
          </li>
        </ul>
      </div>
    </div>

    <main class="pt-32 pb-20 px-4 flex flex-col items-center overflow-hidden">
      <!-- Hero Section -->
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
            class="w-24 h-24 md:w-32 md:h-32 bg-gradient-to-br from-orange-400 to-orange-600 rounded-3xl shadow-2xl shadow-orange-500/40 flex items-center justify-center animate-float-center"
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
          Connect Talent with <br />
          <span class="bg-gradient-to-r from-orange-500 to-orange-600 bg-clip-text text-transparent"
            >Opportunity</span
          >
        </h1>

        <p class="text-lg md:text-xl text-slate-500 mb-10 leading-relaxed max-w-lg mx-auto">
          Hyro is the modern HR platform that brings together talented professionals and
          forward-thinking companies in one seamless experience.
        </p>
      </div>
    </main>

    <!-- Why Hyro Section -->
    <section id="why-hyro" class="py-20 px-4 bg-gradient-to-b from-slate-50 to-white">
      <div class="max-w-6xl mx-auto">
        <div class="text-center mb-16">
          <div
            class="inline-flex items-center justify-center w-16 h-16 bg-gradient-to-br from-orange-400 to-red-400 rounded-2xl shadow-lg shadow-orange-400/30 mb-6"
          >
            <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"
              />
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
              />
            </svg>
          </div>
          <h2 class="text-4xl md:text-5xl font-extrabold text-slate-900 mb-4">Why Choose Hyro?</h2>
          <p class="text-lg text-slate-600 max-w-2xl mx-auto">
            Seamlessly integrate with your favorite tools and streamline your workflow
          </p>
        </div>

        <div class="relative max-w-5xl mx-auto">
          <div class="grid grid-cols-2 md:grid-cols-4 gap-6 md:gap-8">
            <div
              v-for="(feature, index) in whyHyroFeatures"
              :key="feature.title"
              class="group relative bg-gradient-to-br from-slate-50 to-slate-100/50 backdrop-blur-sm p-8 rounded-3xl border border-slate-200/60 hover:shadow-2xl hover:-translate-y-2 transition-all duration-500 cursor-pointer"
              :class="index === 2 ? 'md:mt-16' : ''"
            >
              <div class="flex flex-col items-center text-center h-full">
                <div
                  class="w-20 h-20 mb-6 flex items-center justify-center transform group-hover:scale-110 transition-transform duration-300"
                >
                  <component
                    :is="feature.icon"
                    class="w-16 h-16 text-orange-600 opacity-80"
                    stroke-width="1.5"
                  />
                </div>
                <h3 class="text-lg font-bold text-slate-900 mb-2">{{ feature.title }}</h3>
                <p class="text-sm text-slate-500">{{ feature.description }}</p>
              </div>

              <!-- Hover glow effect -->
              <div
                class="absolute inset-0 rounded-3xl bg-gradient-to-br from-orange-400/0 to-orange-600/0 group-hover:from-orange-400/10 group-hover:to-orange-600/10 transition-all duration-500 pointer-events-none"
              ></div>
            </div>
          </div>

          <!-- Connecting lines (desktop only) -->
          <svg
            class="hidden md:block absolute inset-0 w-full h-full pointer-events-none -z-10"
            style="top: 50%; transform: translateY(-50%)"
          >
            <line
              x1="20%"
              y1="50%"
              x2="40%"
              y2="50%"
              stroke="#E2E8F0"
              stroke-width="2"
              stroke-dasharray="5,5"
              opacity="0.5"
            />
            <line
              x1="60%"
              y1="50%"
              x2="80%"
              y2="50%"
              stroke="#E2E8F0"
              stroke-width="2"
              stroke-dasharray="5,5"
              opacity="0.5"
            />
          </svg>
        </div>
      </div>
    </section>

    <!-- For Applicants Section -->
    <section
      id="for-applicants"
      class="py-24 px-4 bg-gradient-to-br from-blue-50 via-white to-cyan-50 relative overflow-hidden"
    >
      <!-- Background decorative elements -->
      <div
        class="absolute top-0 right-0 w-96 h-96 bg-blue-100 rounded-full filter blur-3xl opacity-30 -translate-y-1/2 translate-x-1/2"
      ></div>
      <div
        class="absolute bottom-0 left-0 w-96 h-96 bg-cyan-100 rounded-full filter blur-3xl opacity-30 translate-y-1/2 -translate-x-1/2"
      ></div>

      <div class="max-w-6xl mx-auto relative z-10">
        <div class="grid md:grid-cols-2 gap-16 items-center mb-20">
          <div>
            <div class="inline-block mb-4">
              <span
                class="bg-blue-100 text-blue-700 text-xs font-bold px-4 py-2 rounded-full uppercase tracking-wider"
                >For Job Seekers</span
              >
            </div>
            <h2 class="text-4xl md:text-5xl font-extrabold text-slate-900 mb-6 leading-tight">
              Your Next Career Move Starts Here
            </h2>
            <p class="text-lg text-slate-600 leading-relaxed mb-8">
              Join thousands of professionals who've found their dream jobs through Hyro. Our
              intelligent matching system connects you with opportunities that align with your
              skills, experience, and career aspirations.
            </p>
            <div class="flex flex-wrap gap-4">
              <div class="flex items-center gap-2 text-sm text-slate-700">
                <div class="w-5 h-5 bg-blue-100 rounded-full flex items-center justify-center">
                  <Check class="w-3 h-3 text-blue-600" stroke-width="3" />
                </div>
                <span class="font-medium">10,000+ Active Jobs</span>
              </div>
              <div class="flex items-center gap-2 text-sm text-slate-700">
                <div class="w-5 h-5 bg-blue-100 rounded-full flex items-center justify-center">
                  <Check class="w-3 h-3 text-blue-600" stroke-width="3" />
                </div>
                <span class="font-medium">500+ Top Companies</span>
              </div>
              <div class="flex items-center gap-2 text-sm text-slate-700">
                <div class="w-5 h-5 bg-blue-100 rounded-full flex items-center justify-center">
                  <Check class="w-3 h-3 text-blue-600" stroke-width="3" />
                </div>
                <span class="font-medium">AI-Powered Matching</span>
              </div>
            </div>
          </div>

          <div class="relative">
            <div
              class="absolute inset-0 bg-gradient-to-br from-blue-200 to-cyan-200 rounded-3xl blur-2xl opacity-30"
            ></div>
            <div class="relative bg-white p-8 rounded-3xl shadow-2xl border border-slate-100">
              <div class="space-y-4">
                <div
                  class="flex items-center gap-4 p-4 bg-blue-50 rounded-2xl border border-blue-100"
                >
                  <div
                    class="w-12 h-12 bg-blue-500 rounded-xl flex items-center justify-center flex-shrink-0"
                  >
                    <Search class="w-6 h-6 text-white" />
                  </div>
                  <div>
                    <h4 class="font-bold text-slate-900 text-sm">Smart Job Search</h4>
                    <p class="text-xs text-slate-600">Find jobs that match your profile</p>
                  </div>
                </div>
                <div
                  class="flex items-center gap-4 p-4 bg-cyan-50 rounded-2xl border border-cyan-100"
                >
                  <div
                    class="w-12 h-12 bg-cyan-500 rounded-xl flex items-center justify-center flex-shrink-0"
                  >
                    <UserCheck class="w-6 h-6 text-white" />
                  </div>
                  <div>
                    <h4 class="font-bold text-slate-900 text-sm">One-Click Apply</h4>
                    <p class="text-xs text-slate-600">Apply to multiple jobs instantly</p>
                  </div>
                </div>
                <div
                  class="flex items-center gap-4 p-4 bg-indigo-50 rounded-2xl border border-indigo-100"
                >
                  <div
                    class="w-12 h-12 bg-indigo-500 rounded-xl flex items-center justify-center flex-shrink-0"
                  >
                    <TrendingUp class="w-6 h-6 text-white" />
                  </div>
                  <div>
                    <h4 class="font-bold text-slate-900 text-sm">Career Growth Tools</h4>
                    <p class="text-xs text-slate-600">Resources to boost your career</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="grid md:grid-cols-4 gap-6">
          <div
            v-for="feature in applicantFeatures"
            :key="feature.title"
            class="group bg-white/80 backdrop-blur-sm p-6 rounded-2xl border border-slate-200 hover:border-blue-300 hover:shadow-xl hover:-translate-y-1 transition-all duration-300"
          >
            <div
              class="w-12 h-12 bg-gradient-to-br from-blue-500 to-cyan-500 rounded-xl flex items-center justify-center mb-4 group-hover:scale-110 group-hover:rotate-3 transition-transform"
            >
              <component :is="feature.icon" class="w-6 h-6 text-white" />
            </div>
            <h3 class="text-base font-bold text-slate-900 mb-2">{{ feature.title }}</h3>
            <p class="text-sm text-slate-600 leading-relaxed">{{ feature.description }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- For Recruiters Section -->
    <section
      id="for-recruiters"
      class="py-24 px-4 bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 text-white relative overflow-hidden"
    >
      <!-- Background decorative elements -->
      <div
        class="absolute top-0 left-1/4 w-96 h-96 bg-orange-500 rounded-full filter blur-3xl opacity-10"
      ></div>
      <div
        class="absolute bottom-0 right-1/4 w-96 h-96 bg-amber-500 rounded-full filter blur-3xl opacity-10"
      ></div>

      <div class="max-w-6xl mx-auto relative z-10">
        <div class="grid md:grid-cols-2 gap-16 items-center mb-20">
          <div class="order-2 md:order-1 relative">
            <div
              class="absolute inset-0 bg-gradient-to-br from-orange-500 to-amber-500 rounded-3xl blur-2xl opacity-20"
            ></div>
            <div
              class="relative bg-slate-800/50 backdrop-blur-sm p-8 rounded-3xl border border-slate-700 shadow-2xl"
            >
              <div class="space-y-4">
                <div
                  class="flex items-center justify-between p-4 bg-slate-700/50 rounded-2xl border border-slate-600"
                >
                  <div class="flex items-center gap-3">
                    <div
                      class="w-10 h-10 bg-orange-500 rounded-lg flex items-center justify-center"
                    >
                      <Users class="w-5 h-5 text-white" />
                    </div>
                    <div>
                      <div class="text-xs text-slate-400">Talent Pool</div>
                      <div class="text-lg font-bold">2,547</div>
                    </div>
                  </div>
                  <div class="text-green-400 text-sm font-semibold">+23%</div>
                </div>
                <div
                  class="flex items-center justify-between p-4 bg-slate-700/50 rounded-2xl border border-slate-600"
                >
                  <div class="flex items-center gap-3">
                    <div class="w-10 h-10 bg-amber-500 rounded-lg flex items-center justify-center">
                      <Briefcase class="w-5 h-5 text-white" />
                    </div>
                    <div>
                      <div class="text-xs text-slate-400">Active Jobs</div>
                      <div class="text-lg font-bold">48</div>
                    </div>
                  </div>
                  <div class="text-green-400 text-sm font-semibold">+12%</div>
                </div>
                <div
                  class="flex items-center justify-between p-4 bg-slate-700/50 rounded-2xl border border-slate-600"
                >
                  <div class="flex items-center gap-3">
                    <div
                      class="w-10 h-10 bg-orange-600 rounded-lg flex items-center justify-center"
                    >
                      <Target class="w-5 h-5 text-white" />
                    </div>
                    <div>
                      <div class="text-xs text-slate-400">Avg. Time to Hire</div>
                      <div class="text-lg font-bold">12 days</div>
                    </div>
                  </div>
                  <div class="text-green-400 text-sm font-semibold">-18%</div>
                </div>
              </div>
            </div>
          </div>

          <div class="order-1 md:order-2">
            <div class="inline-block mb-4">
              <span
                class="bg-orange-500/20 text-orange-400 text-xs font-bold px-4 py-2 rounded-full uppercase tracking-wider border border-orange-500/30"
                >For Recruiters</span
              >
            </div>
            <h2 class="text-4xl md:text-5xl font-extrabold mb-6 leading-tight">
              Hire Smarter, Not Harder
            </h2>
            <p class="text-lg text-slate-300 leading-relaxed mb-8">
              Transform your recruitment process with AI-powered tools that help you find, engage,
              and hire top talent faster. Save time, reduce costs, and make better hiring decisions.
            </p>
            <div class="space-y-3">
              <div class="flex items-center gap-3 text-slate-300">
                <div
                  class="w-6 h-6 bg-orange-500/20 rounded-full flex items-center justify-center border border-orange-500/30"
                >
                  <Check class="w-4 h-4 text-orange-400" stroke-width="3" />
                </div>
                <span class="font-medium">Automated candidate screening & ranking</span>
              </div>
              <div class="flex items-center gap-3 text-slate-300">
                <div
                  class="w-6 h-6 bg-orange-500/20 rounded-full flex items-center justify-center border border-orange-500/30"
                >
                  <Check class="w-4 h-4 text-orange-400" stroke-width="3" />
                </div>
                <span class="font-medium">Multi-channel job posting</span>
              </div>
              <div class="flex items-center gap-3 text-slate-300">
                <div
                  class="w-6 h-6 bg-orange-500/20 rounded-full flex items-center justify-center border border-orange-500/30"
                >
                  <Check class="w-4 h-4 text-orange-400" stroke-width="3" />
                </div>
                <span class="font-medium">Real-time collaboration tools</span>
              </div>
            </div>
          </div>
        </div>

        <div class="grid md:grid-cols-4 gap-6">
          <div
            v-for="feature in recruiterFeatures"
            :key="feature.title"
            class="group bg-slate-800/50 backdrop-blur-sm p-6 rounded-2xl border border-slate-700 hover:border-orange-500/50 hover:bg-slate-800 hover:-translate-y-1 transition-all duration-300"
          >
            <div
              class="w-12 h-12 bg-gradient-to-br from-orange-500 to-amber-600 rounded-xl flex items-center justify-center mb-4 group-hover:scale-110 group-hover:rotate-3 transition-transform shadow-lg shadow-orange-500/20"
            >
              <component :is="feature.icon" class="w-6 h-6 text-white" />
            </div>
            <h3 class="text-base font-bold mb-2">{{ feature.title }}</h3>
            <p class="text-sm text-slate-400 leading-relaxed">{{ feature.description }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer class="bg-slate-900 text-slate-300 py-16 px-4">
      <div class="max-w-6xl mx-auto">
        <div class="grid md:grid-cols-4 gap-12 mb-12">
          <div class="md:col-span-1">
            <h3
              class="text-2xl font-extrabold bg-gradient-to-r from-orange-400 to-orange-300 bg-clip-text text-transparent mb-4"
            >
              Hyro
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed">
              Connecting talent with opportunity through innovation and excellence.
            </p>
          </div>

          <div>
            <h4 class="text-white font-semibold mb-4">Platform</h4>
            <ul class="space-y-2 text-sm">
              <li>
                <a href="#why-hyro" class="hover:text-orange-400 transition-colors">Why Hyro</a>
              </li>
              <li>
                <a href="#for-applicants" class="hover:text-orange-400 transition-colors"
                  >For Applicants</a
                >
              </li>
              <li>
                <a href="#for-recruiters" class="hover:text-orange-400 transition-colors"
                  >For Recruiters</a
                >
              </li>
              <li><a href="#" class="hover:text-orange-400 transition-colors">Pricing</a></li>
            </ul>
          </div>

          <div>
            <h4 class="text-white font-semibold mb-4">Company</h4>
            <ul class="space-y-2 text-sm">
              <li><a href="#" class="hover:text-orange-400 transition-colors">About Us</a></li>
              <li><a href="#" class="hover:text-orange-400 transition-colors">Careers</a></li>
              <li><a href="#" class="hover:text-orange-400 transition-colors">Blog</a></li>
              <li><a href="#" class="hover:text-orange-400 transition-colors">Contact</a></li>
            </ul>
          </div>

          <div>
            <h4 class="text-white font-semibold mb-4">Legal</h4>
            <ul class="space-y-2 text-sm">
              <li>
                <a href="#" class="hover:text-orange-400 transition-colors">Privacy Policy</a>
              </li>
              <li>
                <a href="#" class="hover:text-orange-400 transition-colors">Terms of Service</a>
              </li>
              <li><a href="#" class="hover:text-orange-400 transition-colors">Cookie Policy</a></li>
            </ul>
          </div>
        </div>

        <div
          class="border-t border-slate-800 pt-8 flex flex-col md:flex-row justify-between items-center gap-4"
        >
          <p class="text-sm text-slate-500">© 2025 Hyro. All rights reserved.</p>

          <div class="flex gap-6">
            <a
              href="#"
              class="w-10 h-10 bg-slate-800 rounded-full flex items-center justify-center hover:bg-orange-600 transition-colors"
            >
              <Twitter class="w-5 h-5" />
            </a>
            <a
              href="#"
              class="w-10 h-10 bg-slate-800 rounded-full flex items-center justify-center hover:bg-orange-600 transition-colors"
            >
              <Linkedin class="w-5 h-5" />
            </a>
            <a
              href="#"
              class="w-10 h-10 bg-slate-800 rounded-full flex items-center justify-center hover:bg-orange-600 transition-colors"
            >
              <Mail class="w-5 h-5" />
            </a>
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>

<style scoped>
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
.animate-float-center {
  animation: float 7s ease-in-out infinite;
}
</style>
