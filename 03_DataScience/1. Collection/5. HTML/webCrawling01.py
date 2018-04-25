from bs4 import BeautifulSoup
html="""
<td class='title'>
<div class='tit3'>
<a href='/movie/bi/mi/basic.nhn?code=158191' title='1987'>
1987
</a>
</div>
</td>
"""
soup=BeautifulSoup(html,'html.parser')  #하나씩 주석 풀면서 볼 것
# print(soup)
# tag=soup.td
# print(tag)
# tag=soup.div
# print(tag)
# tag=soup.a
# print(tag)
# print(tag.name)
# print(tag.attrs)  # 태그<tag @@ @@>안에있는 태그속성이 보여짐
# print(type(tag.string))   # 태그가 열고 닫히는 사이<> @ </> 에있는 스트링이 출력됨 , 타입 bs4.element.NavigableString'
# print(type(tag.text))    #string 과같음  , 타입 = str
