import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(book_id):
    response = requests.get('https://covers.openlibrary.org/b/isbn/{}-M.jpg'.format(book_id))
    print(response)
    return response


def recommend(book):
    book_index = books[books['Book_Title'] == book].index[0]
    distances = similarity[book_index]
    books_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:10]

    recommended_books = []
    recommended_books_posters = []

    for i in books_list:
        books_id = i[0]
        recommended_books.append(books.iloc[i[0]].Book_Title)
        # fetch poster from API
        recommended_books_posters.append(fetch_poster(books.iloc[i[0]].ISBN))
    return recommended_books, recommended_books_posters

books_dict = pickle.load(open('books_dict.pkl','rb'))
books = pd.DataFrame(books_dict)

similarity = pickle.load(open('books_similarity.pkl','rb'))

st.title('Recommender System')

selected_book_name = st.selectbox(
    'Your Choice !',
    books['Book_Title'].values)

if st.button('Recommend'):
    names, recommendations = recommend(selected_book_name)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg")
    with col2:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg")
    with col3:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg")