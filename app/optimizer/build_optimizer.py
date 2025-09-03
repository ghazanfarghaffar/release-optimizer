import time
import random

class BuildOptimizer:
    def __init__(self, services):
        self.services = services
        self.build_cache = {}

    def run_build(self, module_name: str):
        """Simulate building a module, using cache if available."""
        if module_name in self.build_cache:
            print(f"[CACHE HIT] {module_name} build skipped.")
            return self.build_cache[module_name]

        print(f"[BUILD START] {module_name}...")
        build_time = random.randint(2, 5)
        time.sleep(build_time)
        result = f"{module_name}-build-success"
        self.build_cache[module_name] = result
        print(f"[BUILD DONE] {module_name} in {build_time}s")
        return result

    def run_builds(self):
        results = {}
        print("Starting parallel builds...")
        for m in self.services:
            results[m] = self.run_build(m)
        print("All builds completed.")
        return results
