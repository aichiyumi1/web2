"'我的主页'"

import streamlit as st
from PIL import Image

page=st.sidebar.radio("首页",["历史","安利音乐","处理图片","词典"])

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

def page1():
    "'历史'"
    st.image("李晨曦_503d269759ee3d6d1ea768c94c166d224f4ade4b.webp")
    st.write("这是秦始皇，统一六国，创立中央集权，功不可没。可他却是从质子出身，有两个爹,一个嬴异人，一个嫪毐（假）。一生堪称爽文男主，死后却被唾弃，背各种各样的锅，后世称为满级背锅侠。在西安有人扮演秦始皇和兵马俑跳科目三，冲上热搜。他可太难了")

def page2():
    "'安利音乐'"
    pass

def page3():
    "'处理图片'"
    st.write(":green[图片处理工具]:full_moon_with_face:")
    uploaded_file=st.file_uploader("上传图片",type=["png","jpeg","jpg","web"])
    if uploaded_file:
        file_name=uploaded_file.name
        file_type=uploaded_file.type
        file_size=uploaded_file.size
        img=Image.open(uploaded_file)
        st.image(img)
        t1,t2,t3,t4=st.tabs(["原图","s1","s2","s3"])
        with t1:
            st.image(img)
        with t2:
            st.image(img_change(img,1,0,2))
        with t3:
            st.image(img_change(img,2,0,1))
        with t4:
            st.image(img_change(img,0,2,1))

def page4():
    "词典"
    st.write("英汉词典")
    with open("words_space.txt","r",encoding='utf-8') as f:
        words_list=f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i]=words_list[i].split("#")
    words_dict={}
    for i in words_list:
        words_dict[i[1]]=[int(i[0]),i[2]]
    word=st.text_input('请输入要查询的单词')
    if word in words_dict:
        st.write(words_dict[word])
        if word=='Python':
            st.code('''print(你干嘛哈哈哎呦)''')
        if word=="snow":
            st.snow()
        if word=="birthday":
            st.balloons()
        if word=="chicken":
            st.code("你干嘛哈哈哎呦")
        if word=="basketball":
            st.code("唱跳RAP打篮球")
        if word=="pain":
            st.code("哼哼哼啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊嗷嗷啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊")
        if word=="delicious":
            st.code("艾玛太香了")
        if word=="toliet":
            st.code("嗨嗨嗨来了奥")
        if word=="shit":
            st.code("我敢吃三斤")
        if word=="walk":
            st.code("教主")
        if word=="gluten":
            st.code("让你吃到真正的石灰")
            st.image("屏幕截图 2024-02-03 181851.png")
        if word=="name":
            st.code("我是超威蓝猫！")
        if word=="walker":
            st.image("李晨曦_Alan-Walker-JustMusic.fr_.jpg")
        if word=="banana":
            st.image("屏幕截图 2024-02-03 181033.png")
        if word=="manure":
            st.image("屏幕截图 2024-02-03 181446.png")
        if word=="stop":
            st.code("砸瓦鲁多")
            
        
if page=="历史":
    page1()
elif page =="安利音乐":
    page2()
elif page=="处理图片":
    page3()
elif page=="词典":
    page4()


