import streamlit as st 
import pandas as pd
df = pd.read_csv('processed_book_data.csv')
books = list(df['Title'])
summary_df = pd.read_csv('Final_Summary.csv')
smry = summary_df['Summary']
sentiment_df = pd.read_csv('Sentiments.csv')
sents = sentiment_df['Sentiment']


def getindex(str):
    for i in range(len(df)):
        if df['Title'][i] == str:
            return i

def main():
    st.title("Summarizer and Sentimental Analyzer")
    activity1 = ["From Saved Books","New Raw Text"]
    choice = st.sidebar.selectbox("Summarize Content",activity1)
    if choice == 'From Saved Books':
        st.subheader('Summarizer')
        summary_choice = st.selectbox('Choose One',books)
        index = getindex(summary_choice)
        if st.button('Get Summary and Sentiments'):
            st.markdown('### Summary:')
            st.markdown(f'{smry.loc[index]}')
            st.write(f'### Dominant Sentiment: {sents.loc[index]}')        


if __name__ == '__main__':
	main()
