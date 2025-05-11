import streamlit as st
import pandas as pd

# Loading startup ideas from csv data
df = pd.read_csv("data/startup_idea_generator.csv")

df.columns = ["Name", "Industry", "Short", "Full", "Audience", "Model"] # Reanming columns for clarity

# App title message
st.title("🚀 Startup Idea Generator")

# Filter widgets -- Exclude column name from dropdown
industries = st.multiselect(
    "Select Industry (Please choose one option)",
    df["Industry"].dropna().unique()[df["Industry"].dropna().unique() != "Industry"]
)
audiences = st.multiselect(
    "Select Audience (Please choose one option)",
    df["Audience"].dropna().unique()[df["Audience"].dropna().unique() != "Audience"]
)

# Filters
filtered = df.copy()

# Inspire Me button 
reroll = st.button("🎲 Inspire Me (Random idea)")

# Filter options
if reroll:
    # Ignore filters, get random idea
    selected = filtered.sample(1)
else:
    selected = (
        df[df["Industry"].isin(industries)] if industries else df
    )
    selected = (
        selected[selected["Audience"].isin(audiences)] if audiences else selected
    )
    selected = selected.sample(1) if not selected.empty else pd.DataFrame()


user_interacted =  reroll or industries or audiences

# Display logic
def display_ideas(data, user_interacted=False):
    if data.empty:
        if user_interacted:
            st.warning("⚠️ No matching ideas found. Try adjusting the filters.")
        return

    row = data.iloc[0]
    st.markdown(f"### 💡 {row['Name']}")
    st.write(row["Short"])

    # Expnadable full description
    with st.expander("📄 Read Full Description"):
        st.write(row["Full"])

    # Display remaining info
    st.markdown(
        f"""
        **Industry:** {row['Industry']}

        **Audeince:** {row['Audience']}
        
        **Model:** {row['Model']}
        """
    )
    st.markdown("---")

display_ideas(selected, user_interacted)