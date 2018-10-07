from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import mpld3

def wordCount(comments):
    frequencies = {}
    for comment in comments:
        for word in comment.split():
            if word not in frequencies:
                frequencies[word] = 1
            else:
                frequencies[word] += 1

    sorted_freq = sorted(frequencies.items(), key=lambda x: x[1])

    count = 0
    for i in sorted_freq[::-1]:
        print(i)
        count += 1
        if count == 5:
            break

def make_cloud(all_comments):
    fig1, ax1 = plt.subplots()
    ax1.set_title('Word Cloud')
    ax1.wordcloud = WordCloud(background_color="white").generate(str(all_comments))
    plt.imshow(ax1.wordcloud, interpolation='bilinear')
    plt.axis("off")
    print(mpld3.fig_to_html(fig1))