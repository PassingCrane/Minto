#!/user/bin/env python
#pythonプログラムであることを示している

# -*- coding: utf-8 -*-
"""
このプログラムはPythonを書く際のテンプレとなっています。これをコピペしてコーディングを行なってください。
なお字下げしないこと!!
"""

__author_ = 'Maruta Yuzuha'
__version_ = '1.0.0'
__date__ = '2021/12/14'

import csv
import json
from xml.etree import ElementTree




def main():
    """
    Android appのパーミッション確認
    """
    
    openPreset()
    getPermission()
    #compareWithPreset()
    return 0

def getPermission():
    tree = ElementTree.parse('AndroidManifest.xml')
    root = tree.getroot()

    for child in root:
        if child.tag == 'uses-permission':
            at = str(child.attrib)
            #print(str(child.tag)+' and '+ str(child.attrib))
            s = ' \''
            indx = at.find(s)
            r =at[indx+2:]
            sin = r.find('\'')
            r_2 = r[:sin]
            #print(r)
            print(r_2)


def compareWithPreset():
    return 0

def openPreset():
    with open('Android_app_permission_presets.csv', newline='', encoding='utf-8-sig') as csvfile:# encoding='utf-8-sig'はApp 前の文字列削除用
        reader = csv.DictReader(csvfile)
        preset =[row for row in reader]
        #print(preset[0]['CAMERA'])

if __name__ == '__main__':
    #上記のifの記述によってこのスクリプトファイルが起動された時だけ実行する部分になる。
    #ちなみにスクリプトが "モジュールとして"インポートされた時には実行されない、

    #単体テスト:モジュールのdocstring(ドキュメンテーション文字列)に記載された全ての対話実行例が書かれている通りに動作するかを確認
    #python ファイル名 -v
    import doctest
    doctest.testmod()

    #実際にmain()を呼び出して、結果を得て、その結果でPythonシステムを終える
    import sys
    sys.exit(main())



