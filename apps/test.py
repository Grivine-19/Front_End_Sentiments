import streamlit as st
import streamlit.components.v1 as stc

"""# Background Image
page_bg_img = '''
    <style>
    body {
    background-image: url("https://unsplash.com/photos/k0KRNtqcjfw");
    background-size: cover;
    }
    </style>
    '''

#st.markdown(page_bg_img, unsafe_allow_html=True)
stc.html(page_bg_img)
"""
import base64


@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str

    st.markdown(page_bg_img, unsafe_allow_html=True)
    return


stc.set_png_as_page_bg("covid.png")


'''
#Word cloud Generator
#

import matplotlib.pyplot as plt
import matplotlib #Or matplotlib.use('TkAgg') to solve the matplotlib user warning error
matplotlib.use('TkAgg')
#from IPython.display import Image #has different image utilities compared to PIL

def plot_wordcloud(text, mask=None, max_words=500, max_font_size=100, figure_size=(14.0,6.0), color = 'white',
                   title = None, title_size=40, image_color=False):
            stopwords = set(STOPWORDS)
            more_stopwords = {'sasa', "wa", 'wa', 'sana', 'hadi', 'na', 'huyu', 'ni',
                      'za', 'enga', 'mtoto'}
            stopwords = stopwords.union(more_stopwords)

            wordcloud = WordCloud(background_color=color,
                    stopwords = stopwords,
                    max_words = max_words,
                    max_font_size = max_font_size, 
                    random_state = 42,
                    width=400, 
                    height=200,
                    mask = mask)
            wordcloud.generate(str(text))
            plt.figure(figsize=(8, 8), facecolor=None)

            plt.imshow(wordcloud)
            plt.axis("off")
            plt.tight_layout(pad = 0)
            plt.savefig('foo.png', bbox_inches='tight')
            
            
        d = "images/"
        
        pos_mask = np.array(Image.open(d + "upvote.png"))
        plot_wordcloud(str(covid_data.text_without_stopwords), mask=pos_mask,
                 color='white', max_font_size=300, title_size=30, title="Most Common Tweets")
        #st.write(plt.show())

'''
