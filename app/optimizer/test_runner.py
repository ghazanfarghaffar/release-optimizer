import time

class TestRunner:
    def __init__(self, services):
        self.services = services

    def run_tests(self):
        print("Starting tests...")
        for service in self.services:
            print(f"[TEST START] {service}...")
            time.sleep(1)
            print(f"[TEST DONE] {service} passed")
        print("All tests completed.\n")
