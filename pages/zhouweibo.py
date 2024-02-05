import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt

page = st.sidebar.radio('我的首页', ['eee', '我的图片处理工具', '我的智慧词典', '我的留言区'])

def page_1():
    '''eee'''
    with open('霞光.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
    st.image('e.png')
    st.image("双面龟.png")
    

def page_2():
    '''我的图片处理工具'''
    st.write(":sunglasses:图片处理小程序:sunglasses:")
    uploaded_file=st.file_uploader("上传图片",type=["png","jpeg","jpg"])
    if uploaded_file:
        file_name=uploaded_file.name
        file_type=uploaded_file.type
        file_size=uploaded_file.size
        img=Image.open(uploaded_file)
        #st.image(img)
        #st.image(img_change(img,0,2,1))

    tab1,tab2,tab3,tab4=st.tabs(["原图","改色1","改色2","改色3"])
    with tab1:
        st.image(img)
    with tab2:
        st.image(img_change(img,0,2,1))
    with tab3:
        st.image(img_change(img,1,2,0))
    with tab4:
        st.image(img_change(img,1,0,2))
    
def page_3():
    '''词典'''
    st.write(':biue智能词典')
    with open("words_space.txt","r",encoding='utf-8') as f:
        words_list=f.read().split("\n")
    for i in range(len(words_list)):
        words_list[i]=words_list[i].split("#")

    words_dict={}
    for i in words_list:
        words_dict[i[1]]=['''int(i[0])''',i[2]]
        
    word=st.text_input("请输入要查询的单词:")
    if word in words_dict:
        st.write(words_dict[word])
        if word=="python":
            st.code('''print('hello world')''')

        if word=="snow":
            st.snow()
        if word=="birthday":
            st.balloons()
        if word=="coke":
            st.image("coke.jpeg")
def page_4():
    '''我的留言区'''
    pass

def img_change(img,rc,gc,bc):
    width,height=img.size
    img_array=img.load()
    for x in range(width):
        for y in range(height):
            r=img_array[x,y][rc]
            g=img_array[x,y][gc]
            b=img_array[x,y][bc]
            img_array[x,y]=(r,g,b)
    return img

if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智慧词典':
    page_3()
elif page == '我的留言区':
    page_4()