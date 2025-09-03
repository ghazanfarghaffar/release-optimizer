import pytest
from optimizer.build_optimizer import BuildOptimizer
from optimizer.test_runner import TestRunner

def test_build_optimizer():
    services = ["test_service"]
    optimizer = BuildOptimizer(services)
    results = optimizer.run_builds()
    assert all("success" in v for v in results.values())

def test_test_runner():
    services = ["test_service"]
    runner = TestRunner(services)
    runner.run_tests()  # just ensure it runs without error
