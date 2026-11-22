"""云璜（YUNHUANG）算子骨架单测：名帖完整、桩位齐整、只增不覆盖。"""
import unittest

from yunhuang import Yunhuang


class TestYunhuang(unittest.TestCase):
    def setUp(self):
        self.op = Yunhuang()

    def test_describe(self):
        d = self.op.describe()
        self.assertEqual(d["repo"], "yunhuang")
        self.assertEqual(d["code"], "YUNHUANG")
        self.assertTrue(d["anchor"].startswith("Ω₀⊂⊙∞⊂Ω"))
        self.assertTrue(d["mingwen"])

    def test_publish_stub(self):
        with self.assertRaises(NotImplementedError):
            self.op.publish(None, None)

    def test_subscribe_stub(self):
        with self.assertRaises(NotImplementedError):
            self.op.subscribe(None, None)


if __name__ == "__main__":
    unittest.main()
