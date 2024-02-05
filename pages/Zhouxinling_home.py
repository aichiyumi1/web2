'''我的主页'''
import streamlit as st
from PIL import Image, ImageFilter

page = st.sidebar.radio('我的首页',['兴趣推荐','图片换色工具','图片换滤镜工具','智慧词典','留言区'])

def page_1():
    '''兴趣推荐'''
    st.balloons()
    st.image("Zhouxinling_首页图片.jpg")
    st.write('电影推荐')
    st.text('''茜茜公主1讲述了美丽活泼的茜茜成长在巴伐利亚一个贵族家庭，父亲是一个无忧无虑的公爵，经常带着茜茜去山上打猎。茜茜母亲的姐姐、奥地利皇太后苏菲打算让儿子与茜茜的姐姐海伦公主订婚，于是邀请了她们一家人参加他的生日庆典。茜茜跟随母亲和姐姐来到奥地利，在一次偷溜出去钓鱼时邂逅了年轻的皇帝弗朗茨，两人一见钟情。虽然弗朗茨已经认不出自己的表妹，却深深被她的美丽开朗吸引着，但当茜茜听说弗朗茨将选姐姐为皇后的消息，便头也不回地跑了。在宴会上，弗朗茨才得知茜茜就是表妹伊丽莎白公主，他的脑子里再也装不下任何人了。舞会上，弗朗茨最终违背母亲的旨意，将一大束红玫瑰递到茜茜手中，并郑重宣布她为自己未来的皇后。茜茜又惊又喜，但她还没有准备好做一名皇后，尤其对于自己破坏了姐姐的幸福心中充满内疚,好在和茜茜姐妹情深的海伦公主不久就原谅了她，并祝愿妹妹能够得到幸福。同时，苏菲皇太后也对弗朗茨的选择非常不满，她不得不重新考虑要如何教育这位尚未成年的皇后。伴随着盛大婚礼的举行，茜茜成为了奥地利的皇后。''')
    st.write('书籍推荐')
    st.text('''海底两万里是法国作家儒勒·凡尔纳创作的长篇小说，是凡尔纳三部曲的第二部。主要讲述了1866年，海上发现了一只疑似为独角鲸的大怪物，阿龙纳斯教授及仆人康塞尔受邀参加追捕。在追捕过程中，他们与鱼叉手尼德·兰不幸落水，到了怪物的脊背上。他们发现这怪物并非是什么独角鲸，而是一艘构造奇妙的潜艇。潜艇是尼摩在大洋中的一座荒岛上秘密建造的，船身坚固，利用海水发电。尼摩船长邀请阿龙纳斯海底旅行。他们从太平洋出发，经过珊瑚岛、印度洋、红海、地中海、大西洋，看到海中许多罕见的动植物和奇异景象。途中还经历了搁浅、土著围攻、同鲨鱼搏斗、冰山封路、章鱼袭击等许多险情。最后，当潜艇到达挪威海岸时，三人不辞而别，回到了他们的家乡。''')
    st.write('音乐推荐')
    st.text('桃花诺')
    with open('Zhouxinling_桃花诺.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=160)
    st.text('大时代')
    with open('Zhouxinling_大时代.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=54)
    st.text('虞兮叹')
    with open('Zhouxinling_虞兮叹.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
    st.text('楼外楼')
    with open('Zhouxinling_楼外楼.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
    st.text('奔跑的青春')
    with open('Zhouxinling_奔跑的青春.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=136)
    st.write('舞蹈推荐')
    st.text('雨中花')
    st.video('Zhouxinling_雨中花.mp4')
    st.text('丽人行')
    st.video('Zhouxinling_杜甫.mp4')
    st.image("Zhouxinling_图片2.jpeg")
    st.image("Zhouxinling_图片5.jpeg")
    st.image("Zhouxinling_图片9.jpeg")
    
def page_2():
    '''图片换色工具'''
    st.write(":volcano:图片换色小程序:volcano:")
    uploaded_file = st.file_uploader("上传图片", type=['jpg','png','jpeg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        tab1, tab2, tab3, tab4 = st.tabs(["原图","改色1","改色2","改色3"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img, 0, 2, 1))
        with tab3:
            st.image(img_change(img, 1, 2, 0))
        with tab4:
            st.image(img_change(img, 1, 0, 2))

# def page_3():
#     '''图片换滤镜工具'''
#     uploaded_file = st.file_uploader("上传图片", type=['jpg','png','jpeg'])
#     if uploaded_file:
#         file_name = uploaded_file.name
#         file_type = uploaded_file.type
#         file_size = uploaded_file.size
#         img = Image.open(uploaded_file)
#     st.image(image1)
#     options = ['模糊滤镜', '轮廓滤镜', '边缘增强滤镜', '浮雕滤镜','锐化滤镜','平滑滤镜']
#     selected_option = st.selectbox('图片换滤镜工具', options)

def page_4():
    '''智慧词典'''
    st.write('智慧词典')
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    word = st.text_input('请输入查询的单词')
    # 显示查询内容
    if word in words_dict:
        st.write(words_dict[word])
        if word=='python':
            st.code('''#恭喜你触发彩蛋，这是一行python代码。
                    print('hello world')''')
        if word == 'snow' or word=='winter':
            st.snow()
        if word == 'birthday':
            st.balloons()
        
def page_5():
    '''留言区'''
    pass

def img_change(img, rc ,gc ,bc):
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

# def img_chg(image1):
#     filters = [
#     ImageFilter.BLUR,  # 模糊
#     ImageFilter.CONTOUR,  # 轮廓
#     ImageFilter.EDGE_ENHANCE,  # 边缘增强
#     ImageFilter.EMBOSS,  # 浮雕
#     ImageFilter.SHARPEN,  # 锐化
#     ImageFilter.SMOOTH,  # 平滑
#     ]
if page == '兴趣推荐':
    page_1()
elif page == '图片换色工具':
    page_2()
# elif page == '图片换滤镜工具':
#     page_3()
elif page == '智慧词典':
    page_4()
elif page == '留言区':
    page_5()