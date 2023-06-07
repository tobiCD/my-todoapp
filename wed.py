import streamlit as st
import fuctions

todos=fuctions.toto()
def addfuction():
    todo=st.session_state["new_todo"]+"\n"
    todos.append(todo)
    fuctions.write(todos)


st.title("My Home TODOAPP")
st.subheader("this is my todo app")
st.write("this app is to increase your productivity")


for index,todo in enumerate(todos):
    checkbox= st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        fuctions.write(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Enter TO do ..." , on_change=addfuction, key='new_todo')

