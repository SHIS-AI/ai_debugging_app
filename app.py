import streamlit as st
from workking_api import generate_hints,generate_solution
from PIL import Image
#title
st.title("AI code debugging")
st.subheader("Upload your image code error")
st.markdown("left side ber option.")
st.markdown("Creator **SHIS**")
st.divider()


#sidebar
with st.sidebar:
    st.markdown("Upload")

    images = st.file_uploader(
        "Enter your screnshot of your code error",
        type=["jpg","png","jpeg"],
        accept_multiple_files=True
    )

    if images:
        if len(images) > 2:
            st.text("Max photo upload 2")
        else:
            col = st.columns(len(images))
            for i,img in enumerate(images):
                with col[i]:
                    st.image(img)
    select_option = st.selectbox(
        "Enter your options",
        ["Hints","Solution"],index=None
    )

    pressd = st.button("Debug Code",type="primary")


if pressd:
    if not images:
        st.error("Please upload your error code screenshot")
    if not select_option:
        st.error("Please select your options")

    if images and select_option:
            pil_images = [Image.open(img) for img in images]
        
            if select_option == "Hints":
                with st.container(border=True):
                    st.subheader("Hints of your code")
                    with st.spinner("Generating hints..."):
                        hints_generate = generate_hints(pil_images)
                        st.markdown(hints_generate)

            if select_option == "Solution":
                with st.container(border=True):
                    st.subheader("Solution your code")
                    with st.spinner("Generating solution..."):
                        solution_generate = generate_solution(pil_images)
                        st.markdown(solution_generate)








