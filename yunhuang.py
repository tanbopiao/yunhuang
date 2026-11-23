"""云璜（YUNHUANG）· 消息通传总线

道统出处：元极恒一·道统构件定名册 V2 ｜ 第五批
体系锚：Ω₀⊂⊙∞⊂Ω｜DID-BR-000002

工程映射：消息通传总线。

边界：本件为算子 v1——骨架桩已按命名映射补齐实现；遵循元法第四条「只增不覆盖」，
方法只增不改名不删，行为变更走新版本；凭据不入档，宣称与事实分离。
"""

class Yunhuang:
    """云璜（YUNHUANG）算子 v1。"""

    ANCHOR = "Ω₀⊂⊙∞⊂Ω｜DID-BR-000002"
    CODE = "YUNHUANG"

    def __init__(self, config=None):
        self.config = dict(config or {})
        self.events = []  # 只增不覆盖：会话内事件留痕
        self.topics = {}
        self._seq = 0

    def describe(self):
        """构件名帖：名、代号、职责、铭文、体系锚。"""
        return {
            "repo": "yunhuang",
            "cn": "云璜",
            "code": self.CODE,
            "duty": "消息通传总线",
            "mingwen": "璜音传讯，总线无壅",
            "anchor": self.ANCHOR,
        }

    def publish(self, topic, message):
        """璜音传讯：按题广播。"""
        handlers = self.topics.get(topic, [])
        for h in handlers:
            h(message)
        self.events.append({"event": "publish", "topic": topic, "delivered": len(handlers)})
        return {"topic": topic, "delivered": len(handlers)}

    def subscribe(self, topic, handler):
        """总线无壅：订阅题讯。"""
        if not callable(handler):
            raise ValueError("订阅者须可调用")
        self._seq += 1
        sid = "YH-%04d" % self._seq
        self.topics.setdefault(topic, []).append(handler)
        self.events.append({"event": "subscribe", "topic": topic, "sid": sid})
        return sid
