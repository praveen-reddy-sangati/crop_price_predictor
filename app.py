import streamlit as st
import pandas as pd

# Load the CSV file
@st.cache_data
def load_data():
    df = pd.read_csv(r'LSTM-Predicted-2027.csv')  # Ensure this path is correct
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    return df

df = load_data()

# Title of the web app
st.title("Crop Price Prediction Results")

# Dropdown for Centre Name
centre_name = st.selectbox("Select Centre Name:", df["Centre_Name"].unique())

# Dropdown for Commodity Name
commodity_name = st.selectbox("Select Commodity Name:", df["Commodity_Name"].unique())

# Dropdown for Season
season = st.selectbox("Select Season:", df["Season"].unique())

# Filter data based on the selected options
filtered_data = df[(df["Centre_Name"] == centre_name) &
                   (df["Commodity_Name"] == commodity_name) &
                   (df["Season"] == season)]

# Dropdown for Year
year = st.selectbox("Select Year:", [str(col) for col in filtered_data.columns if col not in ["Centre_Name", "Commodity_Name", "Season"]])

# Display the result
if st.button("Predict Price"):
    # Display the result only when the button is clicked
    if not filtered_data.empty:
        price = filtered_data[year].values[0]
        st.write(f"The predicted price for {commodity_name} in {centre_name} during {season} in {year} is: *{price}*")
        st.line_chart(filtered_data.drop(columns=["Centre_Name", "Commodity_Name", "Season"]).T)
    else:
        st.write("No data available for the selected options.")

# Add a line chart for the selected commodity over all years
