#!/usr/bin/env python3
"""TTS 読み辞書（この教材用・最小）
edge-tts 合成前に apply_dictionary(text) を適用し、誤読しやすい語の読みを修正する。
ナレーション本文は基本的に音読しやすい話し言葉で書いてあるため、ここでは
ニューラルTTSが特に間違えやすい語のみを最小限で補正する（過剰なかな化は
かえって抑揚を損なうため避ける）。長い語から先に置換して部分一致の誤爆を防ぐ。
"""

REPLACEMENTS = [
    ("共役複素数", "きょうやくふくそすう"),
    ("共役", "きょうやく"),   # 「こうやく/きょうえき」等の誤読を防ぐ
    ("余弦波", "よげんは"),
    ("正弦波", "せいげんは"),
    ("純虚数", "じゅんきょすう"),
]


def apply_dictionary(text: str) -> str:
    for src, dst in sorted(REPLACEMENTS, key=lambda kv: -len(kv[0])):
        text = text.replace(src, dst)
    return text


if __name__ == "__main__":
    import sys
    print(apply_dictionary(sys.stdin.read()))
