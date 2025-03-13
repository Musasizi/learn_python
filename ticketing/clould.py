from wordcloud import WordCloud
import matplotlib.pyplot as plt

# List of words/phrases from the Words of Wisdom
words_of_wisdom = """
One thing at a time Think before you speak Everything happens for a reason 
Whatever you do, do hastily but don't rush Always be grateful to God 
One word for a wise is enough Our God is not limited 
You are enough, and you have all it takes to be who you want to be 
With God, all things are possible Friends are important 
Take money where it's supposed to be quickly Believe you can, and you are halfway there 
Service to others is the rent we pay for the room we have here on earth 
Time heals every wound Let Go and Let God Pride comes before a fall 
Truth is absolute Be kind and compassionate 
True knowledge exists in knowing that you know nothing Be humble 
Meditate and aim high Don't be anxious, God is in control 
You are very stupid if you don't want to be corrected 
Love your enemies as God loves you Rely on God, and he will direct your paths 
Don't be deceived, you reap what you sow Don't give up on your dreams 
You don't have to pour into every cup Take time for self-care 
Silence is the best answer Looks can be deceptive 
Be slow to speak Don't let a fool make you foolish Hard work pays 
Be open to being loved If you want to go fast, go alone, but if you want to go far, don't go alone 
Treat others the way you want to be treated
"""

# Generate a high-resolution word cloud
wordcloud = WordCloud(width=1600, height=800, background_color="white", colormap="viridis").generate(words_of_wisdom)

# Display the high-resolution word cloud
plt.figure(figsize=(16, 8))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
