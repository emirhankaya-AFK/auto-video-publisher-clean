"""Run credential-free regressions. Forbid outbound socket connections during tests."""

import importlib
import inspect
import socket
import sys
import unittest

def block_network(*_args, **_kwargs):
    raise RuntimeError("Offline CI forbids network connections")

# Patch the process before discovering/importing tests. This does not configure
# production credentials and is not a replacement for platform/API smoke tests.
socket.socket.connect = block_network
socket.socket.connect_ex = block_network
socket.create_connection = block_network

suite = unittest.defaultTestLoader.discover(".", pattern="test*.py")
result = unittest.TextTestRunner(verbosity=2).run(suite)
if not result.wasSuccessful():
    sys.exit(1)

count = 0
for module_name in ("test_analytics_sheets", "test_stats_reporter"):
    module = importlib.import_module(module_name)
    for name in dir(module):
        obj = getattr(module, name)
        if not name.startswith("test_") or not inspect.isfunction(obj):
            continue
        if len(inspect.signature(obj).parameters):
            continue
        print(f"Running offline assertion: {module_name}.{name}", flush=True)
        obj()
        count += 1

print(f"Offline tests passed: unittest={result.testsRun}, functions={count}")
