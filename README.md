# Reduced Release Cycle by ~40% with CI/CD Automation (Jenkins + GitHub Actions)

This project demonstrates how optimized CI/CD pipelines can accelerate delivery and cut costs.  
By restructuring pipelines, introducing parallel test execution, and leveraging caching, release cycles were reduced by ~40%.

## 🔧 Tech Stack
- Jenkins (Declarative Pipeline)
- GitHub Actions
- Docker
- Bash scripting

## 📈 Impact
- **40% faster pipeline runs** (baseline vs optimized)
- Automated build, test, and deployment workflow
- Scalable approach applicable to production environments

## 📂 Repository Structure
- `.github/workflows/ci-baseline.yml` → Baseline CI (serial)
- `.github/workflows/ci-optimized.yml` → Optimized CI (parallel + cache)
- `Jenkinsfile` → Optimized Jenkins pipeline
- `app/` → Demo application with build/test scripts
- `proof/` → Screenshots, logs, timing evidence

## 📊 Results
Baseline vs optimized pipeline durations are included in the `proof/` folder with screenshots and logs.  
Optimizations consistently saved ~40% of pipeline time.

## 🚀 Next Steps
This repo is a case-style demonstration of pipeline efficiency improvements.  
The same practices can be applied to client repositories to accelerate delivery, improve reliability, and cut costs.
