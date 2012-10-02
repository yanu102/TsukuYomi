#!/usr/bin/env python
# coding: utf-8

class TsukuYomi:
    """
    よみをつくるクラス
    """

    def __init__(self, st=u''):
        """
        コンストラクタ
        """
        self.st = st

        self.dakusei = {
            u'が':u'か',
            u'ぎ':u'き',
            u'ぐ':u'く',
            u'げ':u'け',
            u'ご':u'こ',
            u'ざ':u'さ',
            u'じ':u'し',
            u'ず':u'す',
            u'ぜ':u'せ',
            u'ぞ':u'そ',
            u'だ':u'た',
            u'ぢ':u'ち',
            u'づ':u'つ', 
            u'で':u'て',
            u'ど':u'と',
            u'ば':u'は',
            u'び':u'ひ',
            u'ぶ':u'ふ',
            u'べ':u'へ',
            u'ぼ':u'ほ',
            u'ぱ':u'は',
            u'ぴ':u'ひ',
            u'ぷ':u'ふ',
            u'ぺ':u'へ',
            u'ぽ':u'ほ',
            u'ヴ':u'ふ',
            }

        # 音引き変換
        self.onbiki = {
            u'あ':u'あ',
            u'い':u'い',
            u'う':u'う',
            u'え':u'え',
            u'お':u'お',
            u'か':u'あ',
            u'き':u'い',
            u'く':u'う',
            u'け':u'え',
            u'こ':u'お',
            u'が':u'あ',
            u'ぎ':u'い',
            u'ぐ':u'う',
            u'げ':u'え',
            u'ご':u'お',
            u'さ':u'あ',
            u'し':u'い',
            u'す':u'う',
            u'せ':u'え',
            u'そ':u'お',
            u'ざ':u'あ',
            u'じ':u'い',
            u'ず':u'う',
            u'ぜ':u'え',
            u'ぞ':u'お',
            u'た':u'あ',
            u'ち':u'い',
            u'つ':u'う',
            u'て':u'え',
            u'と':u'お',
            u'だ':u'あ',
            u'ぢ':u'い',
            u'づ':u'う',
            u'で':u'え',
            u'ど':u'お',
            u'な':u'あ',
            u'に':u'い',
            u'ぬ':u'う',
            u'ね':u'え',
            u'の':u'お',
            u'は':u'あ',
            u'ひ':u'い',
            u'ふ':u'う',
            u'へ':u'え',
            u'ほ':u'お',
            u'ば':u'あ',
            u'び':u'い',
            u'ぶ':u'う',
            u'べ':u'え',
            u'ぼ':u'お',
            u'ぱ':u'あ',
            u'ぴ':u'い',
            u'ぷ':u'う',
            u'ぺ':u'え',
            u'ぽ':u'お',
            u'ま':u'あ',
            u'み':u'い',
            u'む':u'う',
            u'め':u'え',
            u'も':u'お',
            u'や':u'あ',
            u'ゆ':u'う',
            u'よ':u'お',
            u'ら':u'あ',
            u'り':u'い',
            u'る':u'う',
            u'れ':u'え',
            u'ろ':u'お',
            u'わ':u'あ',
            u'ぁ':u'あ',
            u'ぃ':u'い',
            u'ぅ':u'う',
            u'ぇ':u'え',
            u'ぉ':u'お',
            u'ゃ':u'あ',
            u'ゅ':u'う',
            u'ょ':u'お',
            u'ゎ':u'あ',
            u'ヴ':u'う',
            u'ん':u'ん',
            }
        self.onbikiLittle = {
            u'あ':u'ぁ',
            u'い':u'ぃ',
            u'う':u'ぅ',
            u'え':u'ぇ',
            u'お':u'ぉ',
            u'か':u'ぁ',
            u'き':u'ぃ',
            u'く':u'ぅ',
            u'け':u'ぇ',
            u'こ':u'ぉ',
            u'が':u'ぁ',
            u'ぎ':u'ぃ',
            u'ぐ':u'ぅ',
            u'げ':u'ぇ',
            u'ご':u'ぉ',
            u'さ':u'ぁ',
            u'し':u'ぃ',
            u'す':u'ぅ',
            u'せ':u'ぇ',
            u'そ':u'ぉ',
            u'ざ':u'ぁ',
            u'じ':u'ぃ',
            u'ず':u'ぅ',
            u'ぜ':u'ぇ',
            u'ぞ':u'ぉ',
            u'た':u'ぁ',
            u'ち':u'ぃ',
            u'つ':u'ぅ',
            u'て':u'ぇ',
            u'と':u'ぉ',
            u'だ':u'ぁ',
            u'ぢ':u'ぃ',
            u'づ':u'ぅ',
            u'で':u'ぇ',
            u'ど':u'ぉ',
            u'な':u'ぁ',
            u'に':u'ぃ',
            u'ぬ':u'ぅ',
            u'ね':u'ぇ',
            u'の':u'ぉ',
            u'は':u'ぁ',
            u'ひ':u'ぃ',
            u'ふ':u'ぅ',
            u'へ':u'ぇ',
            u'ほ':u'ぉ',
            u'ば':u'ぁ',
            u'び':u'ぃ',
            u'ぶ':u'ぅ',
            u'べ':u'ぇ',
            u'ぼ':u'ぉ',
            u'ぱ':u'ぁ',
            u'ぴ':u'ぃ',
            u'ぷ':u'ぅ',
            u'ぺ':u'ぇ',
            u'ぽ':u'ぉ',
            u'ま':u'ぁ',
            u'み':u'ぃ',
            u'む':u'ぅ',
            u'め':u'ぇ',
            u'も':u'ぉ',
            u'や':u'ぁ',
            u'ゆ':u'ぅ',
            u'よ':u'ぉ',
            u'ら':u'ぁ',
            u'り':u'ぃ',
            u'る':u'ぅ',
            u'れ':u'ぇ',
            u'ろ':u'ぉ',
            u'わ':u'ぁ',
            u'ぁ':u'ぁ',
            u'ぃ':u'ぃ',
            u'ぅ':u'ぅ',
            u'ぇ':u'ぇ',
            u'ぉ':u'ぉ',
            u'ゃ':u'ぁ',
            u'ゅ':u'ぅ',
            u'ょ':u'ぉ',
            u'ゎ':u'ぁ',
            u'ヴ':u'ぅ',
            u'ん':u'ん',
            }

        self.coding = 'utf-8'

    def __str__(self):
        """
        self.codingでエンコードして出力
        """
        return self.st.encode(self.coding)

    def set(self, st):
        """
        文字列登録
        """
        self.st = st
        return self

    def get(self):
        """
        文字列取得
        """
        return self.st

    def setCoding(self, coding):
        """
        エンコード設定
        """
        self.coding = coding
        return self

    def dakuon2seion(self):
        """
        濁音を清音に変換
        """
        out = u''
        for ch in self.st:
            if ch in self.dakusei:
                out += self.dakusei[ch]
            else:
                out += ch
        self.st = out
        return self

    def onbiki2shiin(self, little=False):
        """
        音引きを子音に変換
        """
        out = u''
        if little:
            onbikilist = self.onbikiLittle
        else:
            onbikilist = self.onbiki
        chp = u''
        for ch in self.st:
            if ch == u'ー' and chp != u'' and chp in onbikilist:
                out += onbikilist[chp]
                chp = onbikilist[chp]
            else:
                out += ch
                chp = ch
        self.st = out
        return self
