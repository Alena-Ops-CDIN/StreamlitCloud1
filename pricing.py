import streamlit as st

# Sample pricing data (Note: these are hypothetical prices!)
PRICING_DATA = {
    'AWS': {
        't2.micro': 0.01,
        't2.medium': 0.05,
        't2.large': 0.10
    },
    'Azure': {
        'B1S': 0.02,
        'B2S': 0.07,
        'B4MS': 0.14
    },
    'GCP': {
        'f1-micro': 0.007,
        'g1-small': 0.03,
        'n1-standard-1': 0.09
    }
}

# App main function
def main():
    st.title("Cloud Pricing Calculator")

    # Select cloud provider
    cloud_provider = st.selectbox("Select a Cloud Provider", list(PRICING_DATA.keys()))
    instance_type = st.selectbox("Select an Instance Type", list(PRICING_DATA[cloud_provider].keys()))

    # Calculate and display cost
    hours = st.slider("Number of hours", 1, 720, 24)
    cost = PRICING_DATA[cloud_provider][instance_type] * hours
    st.write(f"Estimated cost for {hours} hours of running {instance_type} on {cloud_provider}: ${cost:.2f}")

if __name__ == "__main__":
    main()
