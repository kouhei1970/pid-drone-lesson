#!/usr/bin/env python3
"""TTS 読み辞書（この教材用）
edge-tts 合成前に apply_dictionary(text) を適用し、誤読しやすい語の読みを修正する。

ルール:
  - 読みは「カタカナ」で書く。ひらがなの「は/へ」は TTS が助詞（ワ/エ）と誤解しやすい。
    例: 正弦波 を「せいげんは」とすると末尾が助詞「わ」に化けるため、必ず「セイゲンハ」。
  - 過剰なかな化は抑揚を損なうので、誤読する語だけ最小限に。
  - 長い語から先に置換して部分一致の誤爆を防ぐ（apply 内でソート）。
"""

REPLACEMENTS = [
    ("正弦波", "セイゲンハ"),       # 「波」は は行のハ（×せいげんワ）
    ("余弦波", "ヨゲンハ"),
    ("共役複素数", "キョウヤクフクソスウ"),
    ("共役", "キョウヤク"),         # ×こうやく/きょうえき
    ("純虚数", "ジュンキョスウ"),
]


def apply_dictionary(text: str) -> str:
    for src, dst in sorted(REPLACEMENTS, key=lambda kv: -len(kv[0])):
        text = text.replace(src, dst)
    return text


if __name__ == "__main__":
    import sys
    print(apply_dictionary(sys.stdin.read()))
