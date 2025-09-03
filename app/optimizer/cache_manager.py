import time

class CacheManager:
    def __init__(self, services):
        self.services = services
        self.cache = {}

    def clear_cache(self):
        print("Clearing cache for all services...")
        for service in self.services:
            if service in self.cache:
                del self.cache[service]
                print(f"[CACHE CLEARED] {service}")
            else:
                print(f"[CACHE EMPTY] {service}")
        print("Cache clearing done.\n")
