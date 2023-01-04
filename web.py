import streamlit as st
import connection_sql

items = connection_sql.get_items()


def add_item():
    item = st.session_state["new_item"] + "\n"
    if item in items:
        st.info("Keine doppelten Einträge bitte, das gibt Ärger!!!")
    else:
        items.append(item)
        connection_sql.write_items(items)
        st.session_state["new_item"] = ""


def del_item():
    items_to_del = []
    for item in st.session_state:
        if item == "new_item":
            pass
        elif st.session_state[item]:
            items.remove(item)
            del st.session_state[item]
    connection_sql.write_items(items)


st.title("Meine Einkaufsliste")
st.subheader("Für Pauline und Demetrio")
st.write("Damit mein Schatz endlich eine Einkaufliste hat")

for index, item in enumerate(items):
    item = st.checkbox(label=item, key=str(item))


st.text_input(label=" ", placeholder="Gib ein neues Produkt ein", key='new_item')
st.button(label="Eintragen", on_click=add_item)
st.button(label="Löschen/Eingekauft", on_click=del_item)
