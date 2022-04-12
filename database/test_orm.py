
# TODO
class TestDatabase:
    def test_maybe_skipped(self):
        if not external_resource_available():
            self.skipTest("External resource not available")
        # test code that depends on the external resource
        pass
