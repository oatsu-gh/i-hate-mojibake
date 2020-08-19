#!python
# coding: utf-8
# Copyright (c) oatsu
"""
指定された拡張子のファイルの文字コードを変換する。
Shift JIS を UTF-8 にする。
"""
from glob import glob
from pprint import pprint
import os

def utf8_to_sjis(path_in, path_out):
    """
    ファイルを読み取ってすぐ出力する
    フォルダくらいは変えようかなあ
    """
    with open(path_in, mode='r', encoding='sjis') as f:
        s = f.read()
    with open(path_out, mode='w', encoding='utf-8') as f:
        f.write(s)


def main():
    """
    ファイルのパスを取得して変換に投げる
    """

    path_inputdir = input('変換したいファイルがあるフォルダ: ').strip('"')
    target_ext = input('変換したいファイルの拡張子      : ')
    l = glob(f'{path_inputdir}/*{target_ext}')
    print('対象ファイル:')
    pprint(l)
    print('')
    input('Enterを押すと変換開始します')
    # 出力用フォルダを作成
    os.makedirs(f'{path_inputdir}/utf8', exist_ok=True)
    for path_in in l:
        print(f'  {path_in}')
        path_out = os.path.dirname(path_in) + '/utf8/' + os.path.basename(path_in)
        utf8_to_sjis(path_in, path_out)
        print(f'  {path_out}')

if __name__ == '__main__':
    print('_____ξ・ヮ・) < sjis_to_utf8 v0.0.1 ________')
    print('Copyright (c) 2001-2020 Python Software Foundation')
    print('Copyright (c) 2020 oatsu\n')
    main()
    input('Press Enter to exit.')
