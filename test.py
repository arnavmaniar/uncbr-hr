import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

# Load the CSV files
learning_session_df = pd.read_csv('learningsession.csv')
new_teammate_df = pd.read_csv('newteammate.csv')

# Clean Learning Session Data
learning_session_df.columns = ["Evaluation Area", "Excellent", "Good", "Fair", "N/A - No Answer", "Totals"]
learning_session_df = learning_session_df.drop(0)
learning_session_df = learning_session_df.reset_index(drop=True)
for col in ["Excellent", "Good", "Fair", "N/A - No Answer", "Totals"]:
    learning_session_df[col] = pd.to_numeric(learning_session_df[col], errors='coerce')

# Clean New Teammate Feedback Data
new_teammate_df.columns = ["Feedback Question", "Poor", "Fair", "Good", "Excellent", "N/A - No Answer"]
new_teammate_df = new_teammate_df.dropna(how='all')
new_teammate_df = new_teammate_df.reset_index(drop=True)
for col in ["Poor", "Fair", "Good", "Excellent", "N/A - No Answer"]:
    new_teammate_df[col] = pd.to_numeric(new_teammate_df[col], errors='coerce')

# Filter relevant feedback questions for visualization
relevant_questions = [
    "Please rate you experience with Human Resources during the application/employment process",
    "Please rate the Recruiter who worked with you during the interview process/Overall Communications",
    "Please rate the Recruiter who worked with you during the interview process/Instructions provided",
    "Please rate the Recruiter who worked with you during the interview process/Knew the job representing",
    "Please rate the Recruiter who worked with you during the interview process/Professionalism",
    "Please rate your experience in Employee Health Services/ Staff friendly and courteous",
    "Please rate your experience in Employee Health Services/ Understandable Clinical Information",
    "Please rate your experience in Employee Health Services/ Professionalism",
    "Please rate your experience in Employee Health Services/ Timely Service Rendered",
    "Please rate your experience in Employee Health Services/ Observed Handwashing Technique"
]

filtered_new_teammate_df = new_teammate_df[new_teammate_df['Feedback Question'].isin(relevant_questions)]

# Summary Statistics
learning_session_summary = learning_session_df.describe().transpose()
new_teammate_summary = filtered_new_teammate_df.describe().transpose()

# Visualize Learning Session Data with Matplotlib
fig, ax = plt.subplots(figsize=(12, 8))
learning_session_df.set_index('Evaluation Area')[['Excellent', 'Good', 'Fair', 'N/A - No Answer']].plot(kind='bar', stacked=True, ax=ax)
ax.set_title('Learning Session Evaluation Ratings')
ax.set_ylabel('Number of Ratings')
ax.set_xlabel('Evaluation Area')
plt.subplots_adjust(bottom=0.3)
plt.show()

# Visualize Learning Session Data with Plotly
fig1 = px.bar(learning_session_df, x='Evaluation Area', y=['Excellent', 'Good', 'Fair', 'N/A - No Answer'],
              title="Learning Session Evaluation Ratings", labels={'value':'Number of Ratings', 'variable':'Rating'})
fig1.update_layout(barmode='stack', xaxis_tickangle=-45)
fig1.show()

# Visualize Filtered New Teammate Feedback Data with Matplotlib
fig, ax = plt.subplots(figsize=(12, 8))
filtered_new_teammate_df.set_index('Feedback Question')[['Poor', 'Fair', 'Good', 'Excellent', 'N/A - No Answer']].plot(kind='bar', stacked=True, ax=ax)
ax.set_title('New Teammate Feedback Ratings')
ax.set_ylabel('Number of Ratings')
ax.set_xlabel('Feedback Question')
plt.subplots_adjust(bottom=0.4)
plt.show()

# Visualize Filtered New Teammate Feedback Data with Plotly
fig2 = px.bar(filtered_new_teammate_df, x='Feedback Question', y=['Poor', 'Fair', 'Good', 'Excellent', 'N/A - No Answer'],
              title="New Teammate Feedback Ratings", labels={'value':'Number of Ratings', 'variable':'Rating'})
fig2.update_layout(barmode='stack', xaxis_tickangle=-45)
fig2.show()

# Suggestions for Improvement
print("Learning Session Evaluation Suggestions:")
print("1. Target Areas with Lower 'Good' Ratings: Focus on improving the content or delivery methods in areas with higher 'Good' ratings to push them into the 'Excellent' category.")
print("2. Engagement and Clarity: Reduce the number of 'N/A' responses by ensuring that all content is clear and engaging.")
print("\nNew Teammate Feedback Suggestions:")
print("1. Focus on Detailed Feedback: Even though there are no 'Poor' ratings, analyzing written feedback or conducting follow-up interviews can provide insights into improving the 'Good' and 'Fair' ratings.")
print("2. Consistency in Excellent Ratings: Ensure consistency in the quality of the onboarding process to maintain high 'Excellent' ratings.")





### NEW

import pandas as pd
import plotly.express as px

# Load the CSV files
learning_session_df = pd.read_csv('learningsession.csv')
new_teammate_df = pd.read_csv('newteammate.csv')

# Clean Learning Session Data
learning_session_df.columns = ["Evaluation Area", "Excellent", "Good", "Fair", "N/A - No Answer", "Totals"]
learning_session_df = learning_session_df.drop(0)
learning_session_df = learning_session_df.reset_index(drop=True)

# Filter out rows with no data
learning_session_df = learning_session_df.dropna(subset=["Excellent", "Good", "Fair", "N/A - No Answer"], how='all')

for col in ["Excellent", "Good", "Fair", "N/A - No Answer", "Totals"]:
    learning_session_df[col] = pd.to_numeric(learning_session_df[col], errors='coerce')

# Clean New Teammate Feedback Data
new_teammate_df.columns = ["Feedback Question", "Poor", "Fair", "Good", "Excellent", "N/A - No Answer"]
new_teammate_df = new_teammate_df.dropna(how='all')
new_teammate_df = new_teammate_df.reset_index(drop=True)

# Filter out rows with no data
new_teammate_df = new_teammate_df.dropna(subset=["Poor", "Fair", "Good", "Excellent", "N/A - No Answer"], how='all')

for col in ["Poor", "Fair", "Good", "Excellent", "N/A - No Answer"]:
    new_teammate_df[col] = pd.to_numeric(new_teammate_df[col], errors='coerce')

# Filter relevant feedback questions for visualization
relevant_questions = [
    "Please rate you experience with Human Resources during the application/employment process",
    "Please rate the Recruiter who worked with you during the interview process/Overall Communications",
    "Please rate the Recruiter who worked with you during the interview process/Instructions provided",
    "Please rate the Recruiter who worked with you during the interview process/Knew the job representing",
    "Please rate the Recruiter who worked with you during the interview process/Professionalism",
    "Please rate your experience in Employee Health Services/ Staff friendly and courteous",
    "Please rate your experience in Employee Health Services/ Understandable Clinical Information",
    "Please rate your experience in Employee Health Services/ Professionalism",
    "Please rate your experience in Employee Health Services/ Timely Service Rendered",
    "Please rate your experience in Employee Health Services/ Observed Handwashing Technique"
]

# Create a mapping for shorter labels
short_labels = {
    "Please rate you experience with Human Resources during the application/employment process": "HR Experience",
    "Please rate the Recruiter who worked with you during the interview process/Overall Communications": "Recruiter Comm.",
    "Please rate the Recruiter who worked with you during the interview process/Instructions provided": "Recruiter Instr.",
    "Please rate the Recruiter who worked with you during the interview process/Knew the job representing": "Recruiter Knowledge",
    "Please rate the Recruiter who worked with you during the interview process/Professionalism": "Recruiter Prof.",
    "Please rate your experience in Employee Health Services/ Staff friendly and courteous": "Staff Friendliness",
    "Please rate your experience in Employee Health Services/ Understandable Clinical Information": "Clinical Info",
    "Please rate your experience in Employee Health Services/ Professionalism": "EHS Professionalism",
    "Please rate your experience in Employee Health Services/ Timely Service Rendered": "Timely Service",
    "Please rate your experience in Employee Health Services/ Observed Handwashing Technique": "Handwashing Technique"
}

filtered_new_teammate_df = new_teammate_df[new_teammate_df['Feedback Question'].isin(relevant_questions)]
filtered_new_teammate_df['Short Feedback Question'] = filtered_new_teammate_df['Feedback Question'].map(short_labels)

# Calculate satisfaction trends
learning_session_df['Positive'] = learning_session_df['Excellent'] + learning_session_df['Good']
learning_session_df['Negative'] = learning_session_df['Fair']

filtered_new_teammate_df['Positive'] = filtered_new_teammate_df['Excellent'] + filtered_new_teammate_df['Good']
filtered_new_teammate_df['Negative'] = filtered_new_teammate_df['Fair'] + filtered_new_teammate_df['Poor']

# Function to customize and show Plotly plot
def plot_plotly(df, x_col, y_cols, title, x_label_rotation=-45, legend_title='Rating'):
    fig = px.bar(df, x=x_col, y=y_cols, title=title, labels={'value':'Number of Ratings', 'variable':legend_title})
    fig.update_layout(barmode='stack', xaxis_tickangle=x_label_rotation)
    fig.show()

# Visualize Learning Session Data
plot_plotly(learning_session_df, 'Evaluation Area', ['Excellent', 'Good', 'Fair', 'N/A - No Answer'], 'Learning Session Evaluation Ratings', x_label_rotation=45)

# Visualize Filtered New Teammate Feedback Data with shortened labels
plot_plotly(filtered_new_teammate_df, 'Feedback Question', ['Poor', 'Fair', 'Good', 'Excellent', 'N/A - No Answer'], 'New Teammate Feedback Ratings', x_label_rotation=45)

# Visualize satisfaction trends in Learning Sessions
plot_plotly(learning_session_df, 'Evaluation Area', ['Positive', 'Negative'], 'Satisfaction Trends in Learning Sessions', x_label_rotation=45)

# Visualize satisfaction trends in New Teammate Feedback with shortened labels
plot_plotly(filtered_new_teammate_df, 'Feedback Question', ['Positive', 'Negative'], 'Satisfaction Trends in New Teammate Feedback', x_label_rotation=45)

# Suggestions for Improvement
print("Learning Session Evaluation Suggestions:")
print("1. Target Areas with Lower 'Good' Ratings: Focus on improving the content or delivery methods in areas with higher 'Good' ratings to push them into the 'Excellent' category.")
print("2. Engagement and Clarity: Reduce the number of 'N/A' responses by ensuring that all content is clear and engaging.")
print("\nNew Teammate Feedback Suggestions:")
print("1. Focus on Detailed Feedback: Even though there are no 'Poor' ratings, analyzing written feedback or conducting follow-up interviews can provide insights into improving the 'Good' and 'Fair' ratings.")
print("2. Consistency in Excellent Ratings: Ensure consistency in the quality of the onboarding process to maintain high 'Excellent' ratings.")
