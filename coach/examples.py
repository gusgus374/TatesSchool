import streamlit as st
import pandas as pd
import altair as alt

st.title("🎮 Fun with Soccer Data!")

coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
with coach_message:
    st.write("Welcome to our data playground! Here we'll learn how to work with real soccer data in fun and easy ways. 🚀")
    st.write("Let's start by loading our data file and exploring what's inside!")

# Load the data
data = pd.read_csv("data/Tates_data.csv")

# Example 1: Basic Data Display
st.header("1️⃣ Let's Look at Our Data!")
coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
with coach_message:
    st.write("First, let's see what our data looks like in a table. You can sort by clicking column headers!")

st.dataframe(data)

# Example 2: Player Selector
st.header("2️⃣ Pick Your Player!")
coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
with coach_message:
    st.write("Let's create a dropdown menu to select a player and see their stats!")

player_name = st.selectbox("Choose a player:", data["Player Name"].unique())
player_data = data[data["Player Name"] == player_name]

if st.button("Show Player Stats"):
    st.write(f"Stats for {player_name}:")
    st.metric("Average Distance (km)", f"{player_data['Distance (km)'].mean():.2f}")
    st.metric("Top Speed (m/s)", f"{player_data['Top Speed (m/s)'].max():.2f}")

# Example 3: Interactive Chart
st.header("3️⃣ Make Your Own Chart!")
coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
with coach_message:
    st.write("Now let's create an interactive chart! You can pick what you want to measure.")
    st.write("Try comparing different measurements to see how they relate to each other!")

col1, col2 = st.columns(2)
with col1:
    x_axis = st.selectbox("Pick X-axis:", ["Distance (km)", "Top Speed (m/s)", "Sprint Distance (m)"])
with col2:
    y_axis = st.selectbox("Pick Y-axis:", ["Sprint Distance (m)", "Distance (km)", "Top Speed (m/s)"])

chart = alt.Chart(data).mark_circle().encode(
    x=x_axis,
    y=y_axis,
    color="Player Name",
    tooltip=["Player Name", x_axis, y_axis]
).interactive()

st.altair_chart(chart, use_container_width=True)

# Example 4: Fun Stats Challenge
st.header("4️⃣ Stats Challenge!")
coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
with coach_message:
    st.write("Let's find some interesting facts about our team!")

if st.button("Show Team Records"):
    fastest_player = data.loc[data["Top Speed (m/s)"].idxmax()]
    longest_distance = data.loc[data["Distance (km)"].idxmax()]
    
    st.success(f"🏃‍♂️ Fastest Player: {fastest_player['Player Name']} with {fastest_player['Top Speed (m/s)']:.2f} m/s")
    st.success(f"🏃‍♂️ Longest Distance: {longest_distance['Player Name']} with {longest_distance['Distance (km)']:.2f} km")

# NEW EXAMPLE: Tates Sessions Filter
st.header("5️⃣ Tates Sessions Only!")
coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
with coach_message:
    st.write("Want to see just your Tates School sessions? Let's use some magic to filter the data! 🎩✨")
    st.write("Quick note about `case=False`: This means our search isn't picky about capital or lowercase letters.")
    st.write("For example, it will find:")
    st.write("- 'TATES' ✅")
    st.write("- 'Tates' ✅")
    st.write("- 'tates' ✅")
    st.write("Just like when you're searching on Google, it doesn't matter if you use capital letters or not - it finds what you need! 🔍")

# Create a toggle for showing Tates sessions
show_tates = st.toggle("Show Tates Sessions Only")

if show_tates:
    # Filter for sessions with "Tates" in the title
    tates_data = data[data["Session Title"].str.contains("Tates", case=False)]
    st.write("Here are all your Tates sessions:")
    st.dataframe(tates_data)
    
    # Show some fun stats about Tates sessions
    st.write("📊 Quick Stats from Tates Sessions:")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Number of Sessions", len(tates_data["Session Title"].unique()))
        st.metric("Total Distance Covered (km)", f"{tates_data['Distance (km)'].sum():.1f}")
    with col2:
        st.metric("Highest Speed (m/s)", f"{tates_data['Top Speed (m/s)'].max():.1f}")
        st.metric("Average Distance per Session (km)", f"{tates_data['Distance (km)'].mean():.1f}")

    # Show a fun chart of Tates sessions
    st.write("📈 Your Progress in Tates Sessions:")
    tates_chart = alt.Chart(tates_data).mark_line(point=True).encode(
        x="Session Title",
        y="Distance (km)",
        color="Player Name",
        tooltip=["Player Name", "Session Title", "Distance (km)", "Top Speed (m/s)"]
    ).interactive()
    st.altair_chart(tates_chart, use_container_width=True)

# Example 6: Your Turn!
st.header("6️⃣ Your Turn to Explore!")
coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
with coach_message:
    st.write("Now it's your turn! Try these challenges:")
    st.write("1. Find your highest speed in any session")
    st.write("2. Compare your distance with your teammates")
    st.write("3. Look for patterns in your performance")
    st.write("Remember: There's no wrong way to explore data - just have fun with it! 🌟")

# Add code expander for learning
with st.expander("👀 Want to see how this works? Click here!"):
    st.code('''
# Here's how we filter for Tates sessions:
tates_data = data[data["Session Title"].str.contains("Tates", case=False)]

# Here's how we made the player selector:
player_name = st.selectbox("Choose a player:", data["Player Name"].unique())
player_data = data[data["Player Name"] == player_name]

# And here's how we made the interactive chart:
            
col1, col2 = st.columns(2)
with col1:
    x_axis = st.selectbox("Pick X-axis:", ["Distance (km)", "Top Speed (m/s)", "Sprint Distance (m)"])
with col2:
    y_axis = st.selectbox("Pick Y-axis:", ["Sprint Distance (m)", "Distance (km)", "Top Speed (m/s)"])
chart = alt.Chart(data).mark_circle().encode(
    x=x_axis,
    y=y_axis,
    color="Player Name",
    tooltip=["Player Name", x_axis, y_axis]
).interactive()
    ''')
