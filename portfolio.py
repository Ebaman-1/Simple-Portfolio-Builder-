import streamlit as st

# --- APP TITLE ---
st.set_page_config(page_title="Portfolio Builder", layout="centered")
st.title("💼 Simple Portfolio Builder")

st.write("Fill out the form below to generate your portfolio site 👇")

# --- FORM SECTION ---
with st.form("portfolio_form"):
    name = st.text_input("Your Name")
    title = st.text_input("Your Title (e.g., Data Scientist, Web Developer)")
    bio = st.text_area("Short Bio")
    skills = st.text_area("Your Skills (comma separated)")
    
    st.subheader("Projects")
    project1 = st.text_input("Project 1 Title")
    project1_desc = st.text_area("Project 1 Description")
    project1_link = st.text_input("Project 1 Link (optional)")

    project2 = st.text_input("Project 2 Title")
    project2_desc = st.text_area("Project 2 Description")
    project2_link = st.text_input("Project 2 Link (optional)")

    email = st.text_input("Your Email")
    linkedin = st.text_input("LinkedIn Profile URL")
    github = st.text_input("GitHub Profile URL")

    submitted = st.form_submit_button("Generate Portfolio")

# --- PORTFOLIO PREVIEW ---
if submitted:
    st.success("✅ Portfolio Generated Below")

    st.markdown(f"# {name}")
    st.markdown(f"### {title}")
    st.write(bio)

    st.subheader("🔧 Skills")
    skill_list = [s.strip() for s in skills.split(",")]
    st.write(", ".join(skill_list))

    st.subheader("📂 Projects")
    if project1:
        st.markdown(f"**{project1}**")
        st.write(project1_desc)
        if project1_link:
            st.markdown(f"[View Project]({project1_link})")
    if project2:
        st.markdown(f"**{project2}**")
        st.write(project2_desc)
        if project2_link:
            st.markdown(f"[View Project]({project2_link})")

    st.subheader("📬 Contact")
    if email:
        st.markdown(f"📧 {email}")
    if linkedin:
        st.markdown(f"[LinkedIn]({linkedin})")
    if github:
        st.markdown(f"[GitHub]({github})")
