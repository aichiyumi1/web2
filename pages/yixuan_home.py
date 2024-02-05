'''我的主页'''
import streamlit as st
import PIL as Image

page = st.sidebar.radio("路西弗的书房", ["留言板", "路西弗的日常", "路西弗的推荐", "路西弗的文章"])

def img_change(img):
    width , height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x, y][0]
            g = img_array[x, y][1]
            b = img_array[x, y][2]
    return img

def page1():
    '''路西弗的推荐'''
    st.write(":brown[路西弗的电影推荐]")
    st.image("图片1.png")
    st.text("奥本海默  导演：克里斯托弗·诺兰 主演：基里安·墨菲")
    st.text("真的超级好看！叙事结构是诺兰常用的三段式手法，可能会看不懂，还有很多历史名人和物理学术语，但是真的超级好看！立意也很好，非常推荐大家静下心来去欣赏")
    st.write("(:clapper:来点Oppie~:clapper:)")
    st.image("图片3.png")
    st.write("-----------------------------------------")
    st.write("路西弗的书籍推荐")
    st.write("-----------------------------------------")
    st.write("路西弗的音乐推荐")
    st.write("-----------------------------------------")
    
def page2():
    '''路西弗的文章'''
    st.write(':blue智能词典')
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    word = st.text_input("请输入要查询的单词")
    if word in words_dict:
        st.write(words_dict[word])
        if word == 'python':
            st.code('''print('hello world')''')
        if word == 'snow':
            st.snow()
        if word == 'birthday':
            st.balloons()
    
def page3():
    '''路西弗的日常'''
    st.write(":crescent_moon:先来看点美图~~~:crescent_moon:")
    uploaded_file = st.file_uploader("上传图片", type = ['png', 'jpg', 'jpeg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = image_open(uploaded_file)
    tab1, tab2, tab3, tab4m = (["原图", "改图1", "改图2", "改图3"])
    with tab1:
        st.image(img)
    with tab2:
        st.image(img_change(img, 0, 2, 1))
    with tab3:
        st.image(img_change(img, 1, 2, 0))
    with tab4:
        st.image(img_change(img, 1, 0, 2))
    
def page4():
    '''留言板'''
    pass

def img_change(img, rc, gc, bc):
    width , height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img

if page == "路西弗的推荐":
    page1()
elif page == "路西弗的文章":
    page2()
elif page == "路西弗的日常":
    page3()
elif page == "留言板":
    page4()