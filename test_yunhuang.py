"""云璜（YUNHUANG）算子单测：名帖完整、行为达标、只增不覆盖。"""
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

    def test_pubsub(self):
        seen = []
        sid = self.op.subscribe("题一", seen.append)
        out = self.op.publish("题一", "讯")
        self.assertEqual(out["delivered"], 1)
        self.assertEqual(seen, ["讯"])
        self.assertEqual(self.op.publish("题二", "x")["delivered"], 0)
        with self.assertRaises(ValueError):
            self.op.subscribe("题三", "非 callable")


if __name__ == "__main__":
    unittest.main()
