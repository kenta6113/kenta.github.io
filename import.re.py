import re

text = '''  キリンは大昔から_複数名詞_の興味の対象でした。
キリンは_複数名詞_の中で一番背が高いですが、科学者たちはそのような長い_体の一部  _をどうやって獲得したのか説明できません。キリンの身長は_数値__単位_近くあり、その高さはほとんど足と_体の一部_によるものです。'''


def mad_libs(mls):

  '''
  :param mls:文字列で、ユーザーに入力してもらいたい単語（＝ヒント）の部分は後を2つのアンダースコアで挟んでくださいヒントの単語にはアンダースコアを含めないでください。__hint_hint__はだめです。__hint__はOKです。
  '''

  hints =re.findall('_.*?_',mls)
  if hints is not None:
      for word in hints:
        q = '{}を入力:'.format(word)
        new = input(q)
        mls = mls.replace(word,new,1)
      print('\n')
      mls = mls.replace('\n','')
      print(mls)
  else:
      print('引数mlsが無効です')
mad_libs(text)
