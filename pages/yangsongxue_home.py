"""我的首页"""
import streamlit as st
from PIL import Image

page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智慧词典', '我的留言区'])

def page1():
    '''我的兴趣推荐'''
    with open('yangsongxue_霞光.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
    st.image('yangsongxue_nene.jpg')
    st.write('一.游戏推荐')
    st.text('1.原神')
    st.image('yangsongxue_原神.jpg')
    st.text('懂得都懂，下一个')
    st.write(' ')
    st.text('2.崩坏:星穹铁道')
    st.image('yangsongxue_崩铁.jpg')
    st.text('出了不到一年就拿奖就已经证明了它的实力')
    st.write(' ')
    st.text('3.重返未来1999')
    st.image('yangsongxue_1999.jpg')
    st.text('画面精美，风格吸引，战斗不复杂，不骗氪，抽卡几率大')
    st.write(' ')
    st.text('4.偶像梦幻祭')
    st.image('yangsongxue_es.jpg')
    st.text('"这里有偶像的一切!"49位偶像任君挑选')
    st.write(' ')
    st.text('5.食物语')
    st.image('yangsongxue_食物语.jpg')
    st.text('美食化灵，是玩养成的')
    st.text('天杀的百田，食物语沒了拉你陪葬(bushi)')
    st.write(' ')
    st.text('6.世界计划')
    st.image('yangsongxue_初音.jpg')
    st.text('沒有国服，但打歌手感好爽')
    st.write(' ')
    st.text('7.以闪亮之名')
    st.image('yangsongxue_以闪.jpg')
    st.text('换裝游戏，能捏脸，能自己做衣服') 
    st.write('-----------------------')
    st.write('二.漫画推荐')
    st.text('1.某天成为公主')
    st.image('yangsongxue_公主.jpg')
    st.text('画风超绝的，剧情也很棒')
    st.write(' ')
    st.text('2.我的同学都很奇怪')
    st.image('yangsongxue_同学.jpg')
    st.text('搞笑日常番')
    st.write(' ')
    st.text('3.超赞同梦会')
    st.image('yangsongxue_同梦会.jpg')
    st.text('明明挺好看的，但沒什么人看')
    st.write(' ')
    st.text('4.萌师在上')
    st.image('yangsongxue_萌师.jpg')
    st.text('主角超可爱的') 
    st.write(' ')
    st.text('5.星梦偶像计划')
    st.image('yangsongxue_星梦.jpg')
    st.text('画风好，剧情棒，就是美人哥哥出场少') 
def page2():
    '''我的图片处理工具'''
    st.write(":volcano:图片換色小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        tab1, tab2, tab3, tab4 = st.tabs(["原图", "改色1", "改色2", "改色3"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img, 0, 2, 1))
        with tab3:
            st.image(img_change(img, 1, 2, 0))
        with tab4:
            st.image(img_change(img, 1, 0, 2))

def page3():
    '''我的智慧词典'''
    st.write(':blue智慧词典')
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    word = st.text_input('请输入要查询的单词')

    if word in words_dict:
        st.write(words_dict[word])
        if word=='python':
            st.code('''print('hello world')''')
        if word == 'snow':
            st.snow()
        if word == 'birthday':
            st.balloons()

def page4():
    '''我的留言区'''
    pass

def img_change(img, rc, gc, bc):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img

if page == '我的兴趣推荐':
    page1()
elif page == '我的图片处理工具':
    page2()
elif page == '我的智慧词典':
    page3()
elif page == '我的留言区':
    page4()
    