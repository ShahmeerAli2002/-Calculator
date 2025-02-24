import streamlit as st
import pandas as pd


# Set page configuration
st.set_page_config(
    page_title="Advanced BMI Calculator",
    page_icon="🏋️‍♂️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.streamlit.io/community',
        'Report a bug': 'https://github.com/streamlit/streamlit/issues',
        'About': 'Advanced BMI Calculator - A health monitoring tool'
    }
)

# Enhanced Custom CSS
st.markdown("""
<style>
body {
    font-family: 'Helvetica', sans-serif;
    background-color: #f0f2f6;
}
.main {

    padding: 2.5rem;
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
}
.stButton>button {
    background: linear-gradient(45deg, #2196F3, #00BCD4);
    color: white;
    border: none;

    padding: 15px 30px;
    text-align: center;
    text-decoration: none;
    display: inline-block;


    font-size: 20px;
    border-radius: 30px;
    cursor: pointer;


    box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    transition: all 0.4s ease;
}
.stButton>button:hover {


    transform: translateY(-3px) scale(1.05);
    box-shadow: 0 8px 15px rgba(0,0,0,0.25);
    background: linear-gradient(45deg, #1976D2, #0097A7);
}
.stNumberInput {
    background: white;



    padding: 15px;
    border-radius: 15px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.08);
    transition: all 0.3s ease;
}
.stNumberInput:focus {
    transform: translateY(-2px);
    box-shadow: 0 6px 12px rgba(0,0,0,0.12);
}
.result-box {





    padding: 25px;
    border-radius: 20px;
    margin: 25px 0;
    background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
    box-shadow: 0 8px 16px rgba(0,0,0,0.12);
    border: 1px solid rgba(255,255,255,0.3);
    backdrop-filter: blur(10px);
}
@keyframes meter-animation {


    0% { transform: scale(0.92); }
    50% { transform: scale(1.08); }
    100% { transform: scale(1); }
}
.animated-meter {

    animation: meter-animation 2.5s infinite;
    display: inline-block;
    font-size: 24px;
}
.analog-meter {


    width: 250px;
    height: 125px;
    background: linear-gradient(to right, #4CAF50, #FFC107, #F44336);

    border-radius: 125px 125px 0 0;
    position: relative;

    margin: 30px auto;
    overflow: hidden;

    box-shadow: 0 0 20px rgba(0,0,0,0.25);
    border: 3px solid #fff;
}
.meter-needle {


    width: 5px;
    height: 100px;
    background: #333;
    position: absolute;
    bottom: 0;
    left: 50%;
    transform-origin: bottom center;
    transform: rotate(0deg);

    transition: transform 1.2s cubic-bezier(0.68, -0.55, 0.265, 1.55);
}
.meter-scale {
    position: absolute;

    bottom: 15px;
    width: 100%;
    display: flex;
    justify-content: space-around;
    color: white;
    font-weight: bold;

    text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    font-size: 16px;
}
.meter-value {
    position: absolute;

    bottom: -35px;
    width: 100%;
    text-align: center;

    font-size: 24px;
    font-weight: bold;
    color: #333;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
}
.stSelectbox {
    background: white;
    border-radius: 15px;
    padding: 10px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.08);
}
h1 {
    color: #1a237e;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    font-size: 3em;
    text-align: center;
    margin-bottom: 30px;
}
h3 {
    color: #283593;
    border-bottom: 2px solid #3f51b5;
    padding-bottom: 10px;
    margin-top: 25px;
}
.tip-card {
    background: linear-gradient(135deg, #fff 0%, #f8f9fa 100%);
    padding: 15px;
    border-radius: 15px;
    margin: 10px 0;
    box-shadow: 0 4px 8px rgba(0,0,0,0.08);
    transition: all 0.3s ease;
}
.tip-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 12px rgba(0,0,0,0.12);
}
table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    border-radius: 15px;
    overflow: hidden;
    box-shadow: 0 4px 8px rgba(0,0,0,0.08);
}
th {
    background: linear-gradient(45deg, #1976D2, #2196F3);
    color: white;
    padding: 15px;
    text-align: left;
}
td {
    padding: 12px 15px;
    background: white;
    border-bottom: 1px solid #eee;
}
tr:last-child td {
    border-bottom: none;
}
.disclaimer {
    background: linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%);
    padding: 20px;
    border-radius: 15px;
    margin-top: 30px;
    border: 1px solid #ef9a9a;
    font-style: italic;
    color: #c62828;
}
</style>
""", unsafe_allow_html=True)

# Title with emoji
st.title("🏋️‍♂️ Advanced BMI Calculator 📊")

# Age and Gender inputs
age = st.number_input("Age:", min_value=2, max_value=120, value=22)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])

# Create two columns
col1, col2 = st.columns(2)

with col1:
    # Weight input with unit selection
    weight_unit = st.selectbox("Weight Unit", ["Kilograms", "Pounds"])
    weight = st.number_input(f"Enter your weight in {weight_unit.lower()}:", min_value=0.0, step=0.1)

with col2:
    # Height input with unit selection
    height_unit = st.selectbox("Height Unit", ["Meters", "Centimeters", "Feet"])
    if height_unit == "Meters":
        st.markdown('<div class="animated-meter">📏</div>', unsafe_allow_html=True)
        height = st.number_input("Enter your height in meters:", min_value=0.0, step=0.01)
    elif height_unit == "Centimeters":
        height_cm = st.number_input("Enter your height in centimeters:", min_value=0.0, step=1.0)
        height = height_cm / 100
    else:
        feet = st.number_input("Feet:", min_value=0, step=1, value=5)
        inches = st.number_input("Inches:", min_value=0, max_value=11, step=1, value=10)
        height = (feet * 0.3048) + (inches * 0.0254)

# Convert weight if needed
if weight_unit == "Pounds":
    weight = weight * 0.453592

if st.button("Calculate BMI 🔍"):
    try:
        if weight <= 0 or height <= 0:
            st.error("⚠️ Please enter valid weight and height values.")
        else:
            bmi = round(weight / (height * height), 2)
            
            # Create analog meter display
            rotation = min(max((bmi - 15) * 6, 0), 180)  # Convert BMI to degrees (15-45 BMI range)
            st.markdown(f"""
            <div class='analog-meter'>
                <div class='meter-needle' style='transform: rotate({rotation}deg);'></div>
                <div class='meter-scale'>
                    <span>15</span>
                    <span>25</span>
                    <span>35</span>
                    <span>45</span>
                </div>
                <div class='meter-value'>BMI: {bmi:.1f}</div>
            </div>
            """, unsafe_allow_html=True)
            
            # Create a colorful box for results
            st.markdown("""

            <div class='result-box'>
            """, unsafe_allow_html=True)
            
            st.markdown(f"### Your BMI is: **{bmi:.2f}**")
            

            # BMI Category with color coding and specific health tips
            if bmi < 18.5:
                st.markdown("🔵 **Category:** Underweight")
                st.warning("You are underweight. Consider consulting a nutritionist for a healthy weight gain plan.")
                st.markdown("### 💡 Health Tips for Underweight")
                tips = [
                    "🍽️ Eat more frequently throughout the day",
                    "🥜 Include healthy calorie-dense foods like nuts and avocados",
                    "🥩 Increase protein intake with lean meats and legumes",
                    "🥛 Add healthy smoothies and protein shakes to your diet",
                    "💪 Focus on strength training exercises"
                ]
            elif 18.5 <= bmi < 25:
                st.markdown("🟢 **Category:** Healthy Weight")
                st.success("Congratulations! You are in a healthy weight range.")
                st.markdown("### 💡 Health Tips for Maintaining Healthy Weight")
                tips = [
                    "🏃‍♂️ Continue regular physical activity",
                    "🥗 Maintain your balanced diet",
                    "💧 Stay hydrated with 8 glasses of water daily",
                    "😴 Get 7-8 hours of sleep",
                    "🧘‍♀️ Practice stress management"
                ]
            elif 25 <= bmi < 30:
                st.markdown("🟡 **Category:** Overweight")
                st.warning("You are overweight. Consider adopting a balanced diet and regular exercise routine.")
                st.markdown("### 💡 Health Tips for Overweight")
                tips = [
                    "🚶‍♂️ Start with 30 minutes daily walking",
                    "🥗 Reduce portion sizes and eat more vegetables",
                    "🍎 Choose whole foods over processed foods",
                    "📱 Track your daily calorie intake",
                    "💪 Combine cardio with strength training"
                ]
            else:
                st.markdown("🔴 **Category:** Obese")
                st.error("You are in the obese range. Please consult a healthcare professional for guidance.")
                st.markdown("### 💡 Health Tips for Obesity")
                tips = [
                    "👨‍⚕️ Consult with healthcare professionals",
                    "📝 Keep a food and exercise journal",
                    "🥦 Focus on nutrient-rich, low-calorie foods",
                    "💧 Increase water intake before meals",
                    "🚶‍♂️ Start with low-impact exercises like swimming or walking"
                ]
            
            # Display tips with enhanced styling
            for tip in tips:

                st.markdown(f"""
                <div class="tip-card">
                    {tip}
                </div>
                """, unsafe_allow_html=True)
            
            # BMI Chart
            st.markdown("### BMI Categories Reference:")
            bmi_data = {
                'Category': ['Underweight', 'Normal weight', 'Overweight', 'Obese'],
                'BMI Range': ['< 18.5', '18.5 - 24.9', '25 - 29.9', '≥ 30']
            }
            st.table(pd.DataFrame(bmi_data))
    except:
        st.error("⚠️ Error in calculation. Please check your input values.")

# Disclaimer
st.markdown("---")
st.markdown("""


<div class="disclaimer">
    ⚠️ Disclaimer: This calculator provides a general estimate of BMI. For personalized health advice, please consult with healthcare professionals.
</div>
""", unsafe_allow_html=True)