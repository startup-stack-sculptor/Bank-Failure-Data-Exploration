import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./data/banklist.csv', encoding='latin-1')
df = pd.DataFrame(data)
selected_columns = ['Bank Name']
df[selected_columns].head()
df.columns.to_list

def main():
    st.title("Bank Failure Visualization")

    # Group data by state and count the number of failures
    state_counts = df['State'].value_counts()

    # Plot the number of bank failures by state
    st.subheader('Number of Bank failures by State')
    fig, ax = plt.subplots()
    state_counts.plot(kind='bar', ax=ax)
    ax.set_xlabel('State')
    ax.set_ylabel('Number of failures')
    st.pyplot(fig)

if __name__ == '__main__':
    main()
