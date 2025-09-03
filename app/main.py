from optimizer.build_optimizer import BuildOptimizer
from optimizer.cache_manager import CacheManager
from optimizer.test_runner import TestRunner

def main():
    # List of services to simulate CI/CD pipeline
    services = ["auth", "payment", "notifications", "analytics"]

    print("=== Starting CI/CD Simulation ===\n")

    # Step 1: Run builds
    build_optimizer = BuildOptimizer(services)
    build_optimizer.run_builds()
    print()

    # Step 2: Clear cache
    cache_manager = CacheManager(services)
    cache_manager.clear_cache()
    print()

    # Step 3: Run tests
    test_runner = TestRunner(services)
    test_runner.run_tests()
    print("\n=== CI/CD Simulation Completed ===")

if __name__ == "__main__":
    main()
