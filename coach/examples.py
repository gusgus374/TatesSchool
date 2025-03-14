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

# Show code for Example 1
with st.expander("📝 See the code for loading and displaying data"):
    st.code('''
# Import libraries
import streamlit as st
import pandas as pd
import altair as alt

# Load the data from a CSV file
data = pd.read_csv("data/Tates_data.csv")

# Display the data as an interactive table
st.dataframe(data)
''')

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

# Show code for Example 2
with st.expander("📝 See the code for player selection and stats"):
    st.code('''
# Create a dropdown to select a player
player_name = st.selectbox("Choose a player:", data["Player Name"].unique())

# Filter the data for just that player
player_data = data[data["Player Name"] == player_name]

# Add a button to show stats
if st.button("Show Player Stats"):
    st.write(f"Stats for {player_name}:")
    st.metric("Average Distance (km)", f"{player_data['Distance (km)'].mean():.2f}")
    st.metric("Top Speed (m/s)", f"{player_data['Top Speed (m/s)'].max():.2f}")
''')

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

# Show code for Example 3
with st.expander("📝 See the code for the interactive chart"):
    st.code('''
# Create two columns for our controls
col1, col2 = st.columns(2)

# Add dropdown selectors in each column
with col1:
    x_axis = st.selectbox("Pick X-axis:", ["Distance (km)", "Top Speed (m/s)", "Sprint Distance (m)"])
with col2:
    y_axis = st.selectbox("Pick Y-axis:", ["Sprint Distance (m)", "Distance (km)", "Top Speed (m/s)"])

# Create an interactive chart using Altair
chart = alt.Chart(data).mark_circle().encode(
    x=x_axis,
    y=y_axis,
    color="Player Name",
    tooltip=["Player Name", x_axis, y_axis]
).interactive()

# Display the chart
st.altair_chart(chart, use_container_width=True)
''')

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

# Show code for Example 4
with st.expander("📝 See the code for finding team records"):
    st.code('''
# Create a button to show team records
if st.button("Show Team Records"):
    # Find the player with the highest top speed
    fastest_player = data.loc[data["Top Speed (m/s)"].idxmax()]
    
    # Find the player who covered the longest distance
    longest_distance = data.loc[data["Distance (km)"].idxmax()]
    
    # Display the results with success messages
    st.success(f"🏃‍♂️ Fastest Player: {fastest_player['Player Name']} with {fastest_player['Top Speed (m/s)']:.2f} m/s")
    st.success(f"🏃‍♂️ Longest Distance: {longest_distance['Player Name']} with {longest_distance['Distance (km)']:.2f} km")
''')

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

# Show code for Example 5
with st.expander("📝 See the code for filtering Tates sessions"):
    st.code('''
# Create a toggle button
show_tates = st.toggle("Show Tates Sessions Only")

if show_tates:
    # Filter the data to only show rows with "Tates" in the Session Title
    # The case=False means it will find "Tates", "TATES", or "tates"
    tates_data = data[data["Session Title"].str.contains("Tates", case=False)]
    
    # Show the filtered data
    st.write("Here are all your Tates sessions:")
    st.dataframe(tates_data)
    
    # Create two columns for stats
    col1, col2 = st.columns(2)
    
    # Add stats in the first column
    with col1:
        st.metric("Number of Sessions", len(tates_data["Session Title"].unique()))
        st.metric("Total Distance Covered (km)", f"{tates_data['Distance (km)'].sum():.1f}")
    
    # Add stats in the second column
    with col2:
        st.metric("Highest Speed (m/s)", f"{tates_data['Top Speed (m/s)'].max():.1f}")
        st.metric("Average Distance per Session (km)", f"{tates_data['Distance (km)'].mean():.1f}")
    
    # Create and display a chart
    st.write("📈 Your Progress in Tates Sessions:")
    tates_chart = alt.Chart(tates_data).mark_line(point=True).encode(
        x="Session Title",
        y="Distance (km)",
        color="Player Name",
        tooltip=["Player Name", "Session Title", "Distance (km)", "Top Speed (m/s)"]
    ).interactive()
    st.altair_chart(tates_chart, use_container_width=True)
''')

# Example 6: Your Turn!
st.header("6️⃣ Your Turn to Explore!")
coach_message = st.chat_message(name="Coach Gus", avatar="./media/profile_coachGus.JPG")
with coach_message:
    st.write("Now it's your turn! Try these challenges:")
    st.write("1. Find your highest speed in any session")
    st.write("2. Compare your distance with your teammates")
    st.write("3. Look for patterns in your performance")
    st.write("Remember: There's no wrong way to explore data - just have fun with it! 🌟")

# Add starter code for students
with st.expander("📝 Starter code for your own explorations"):
    st.code('''
# Try your own code here!

# For example, to find your highest speed:
my_name = "Your Name"  # Change this to your name
my_data = data[data["Player Name"] == my_name]
fastest_session = my_data.loc[my_data["Top Speed (m/s)"].idxmax()]
st.write(f"My highest speed was {fastest_session['Top Speed (m/s)']:.2f} m/s in {fastest_session['Session Title']}")

# Or to compare distances between players:
player_distances = data.groupby("Player Name")["Distance (km)"].mean().reset_index()
player_distances = player_distances.sort_values("Distance (km)", ascending=False)
st.bar_chart(player_distances.set_index("Player Name"))
''')