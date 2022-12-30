import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


def del_todo():
    todos_to_del = []
    for todo in st.session_state:
        if todo == "new_todo":
            pass
        elif st.session_state[todo]:
            todos.remove(todo)
            del st.session_state[todo]
    functions.write_todos(todos)


st.title("Meine Einkaufsliste")
st.subheader("Für Pauline und Demetrio")
st.write("Damit mein Schatz endlich eine Einkaufliste hat")

for index, todo in enumerate(todos):
    todo = st.checkbox(todo, key=todo)

st.text_input(label="", placeholder="Gib ein neues Produkt ein", key='new_todo')
st.button(label="Eintragen", on_click=add_todo)
st.button(label="Löschen/Eingekauft", on_click=del_todo)
