import unittest
import monilogger
import monilogger._monilogger as mnlg

class MyOtherEvent:
    pass

class MainTest(unittest.TestCase):

    def setUp(self):
        self.result = 0

    def test_undefined_event(self):
        @monilogger.register("MyEvent")
        def test_monilogger(ctx):
            self.result = self.result + 1

        mnlg.register_base_event("MyEvent")
        mnlg.emit_event("MyEvent", mnlg.MoniLoggerExecutionContext())

        self.assertEqual(self.result, 1)

    def test_class_event(self):
        mnlg.register_base_event("MyOtherEvent")

        @monilogger.register(MyOtherEvent)
        def test_monilogger(ctx):
            self.result = self.result + 1

        mnlg.emit_event("MyOtherEvent", mnlg.MoniLoggerExecutionContext())

        self.assertEqual(self.result, 1)

    def test_composite_event(self):
        mnlg.register_base_event("MyEvent")
        mnlg.register_base_event("MyOtherEvent")
        monilogger.define_event("MyCompositeEvent", ["MyEvent", "MyOtherEvent"])

        @monilogger.register("MyCompositeEvent")
        def test_monilogger(ctx):
            self.result = self.result + 1

        mnlg.emit_event("MyCompositeEvent", mnlg.MoniLoggerExecutionContext())
        
        self.assertEqual(self.result, 1)

if __name__ == '__main__':
    unittest.main()
