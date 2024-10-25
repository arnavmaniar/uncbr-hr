#initialize
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns


def generate_wordcloud(words):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(" ".join(words))
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title('Connections WordCloud')
    plt.axis('off')
    plt.show()

words = ["Empathy", "Inclusiveness", "Compassion", "Growth", "Engagement", "Integrity", "Positivity", "Compliance"]
generate_wordcloud(words)

learningSessionDf = pd.read_csv('learningsession.csv')
newTeammateDf = pd.read_csv('newteammate.csv')
followupDf = pd.read_csv('followup.csv')


print(followupDf.head())
print(followupDf.columns)

#drop nodata/clean
learningSessionDf.columns = ["Evaluation Area", "Excellent", "Good", "Fair", "N/A - No Answer", "Totals"]
learningSessionDf = learningSessionDf.drop(0).reset_index(drop=True)

#drop nodata/clean
learningSessionDf = learningSessionDf.dropna(subset=["Excellent", "Good", "Fair", "N/A - No Answer"], how='all')
for col in ["Excellent", "Good", "Fair", "N/A - No Answer", "Totals"]:
    learningSessionDf[col] = pd.to_numeric(learningSessionDf[col], errors='coerce') #change datatypes to numeirc and turn anything non-numeric to NAN

#drop nodata stuff/clean data
newTeammateDf.columns = ["Feedback Question", "Poor", "Fair", "Good", "Excellent", "N/A - No Answer"]
newTeammateDf = newTeammateDf.dropna(how='all').reset_index(drop=True)

#drop nodata rows
newTeammateDf = newTeammateDf.dropna(subset=["Poor", "Fair", "Good", "Excellent", "N/A - No Answer"], how='all')
for col in ["Poor", "Fair", "Good", "Excellent", "N/A - No Answer"]:
    newTeammateDf[col] = pd.to_numeric(newTeammateDf[col], errors='coerce')

followupDf.columns = ["Department", "Onboarding Experience", "Suggestions"]

#count of ratings 
followupRatings = followupDf['Onboarding Experience'].value_counts().reset_index()
followupRatings.columns = ["Rating", "Count"]

#pivot table to match structure
followupPivot = followupRatings.pivot_table(index="Rating", values="Count", aggfunc='sum').reset_index()

#calculate satisffction/define what is positive/negative
learningSessionDf['Positive'] = learningSessionDf['Excellent'] + learningSessionDf['Good']
learningSessionDf['Negative'] = learningSessionDf['Fair'] + learningSessionDf['N/A - No Answer']
newTeammateDf['Positive'] = newTeammateDf['Excellent'] + newTeammateDf['Good']
newTeammateDf['Negative'] = newTeammateDf['Fair'] + newTeammateDf['Poor'] + learningSessionDf['N/A - No Answer']
followupPivot['Positive'] = followupPivot['Rating'].apply(lambda x: 'Positive' if x in ['Good', 'Excellent'] else 'Negative')
followupPivotSummary = followupPivot.groupby('Positive').sum().reset_index()

#customization for plotly graph
def plot_plotly(df, xCol, yCols, title, xLabelRotation=-45, legendTitle='Rating'):
    fig = px.bar(df, x=xCol, y=yCols, title=title, labels={'value':'Number of Ratings', 'variable':legendTitle})
    fig.update_layout(barmode='stack', xaxis_tickangle=xLabelRotation)
    fig.show()

#plot learning session
plot_plotly(learningSessionDf, 'Evaluation Area', ['Excellent', 'Fair', 'Good', 'N/A - No Answer'], 'Learning Session Evaluation Ratings', xLabelRotation=45)

#short labels for the graph 
shortLabels = {
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
filteredNewTeammateDf = newTeammateDf[newTeammateDf['Feedback Question'].isin(shortLabels.keys())]
filteredNewTeammateDf['Short Feedback Question'] = filteredNewTeammateDf['Feedback Question'].map(shortLabels)

plot_plotly(filteredNewTeammateDf, 'Short Feedback Question', ['Poor', 'Fair', 'Good', 'Excellent', 'N/A - No Answer'], 'New Teammate Feedback Ratings', xLabelRotation=45)

#follow up data plot
plot_plotly(followupPivot, 'Rating', ['Count'], 'Follow-up Feedback Ratings', xLabelRotation=45)

#satisfaction in learning session
plot_plotly(learningSessionDf, 'Evaluation Area', ['Positive', 'Negative'], 'Satisfaction Trends in Learning Sessions', xLabelRotation=45)

#satisfaction in new teammate
plot_plotly(filteredNewTeammateDf, 'Short Feedback Question', ['Positive', 'Negative'], 'Satisfaction Trends in New Teammate Feedback', xLabelRotation=45)

#satisfaction in follow-up
#plot_plotly(followupPivotSummary, 'Positive', ['Count'], 'Satisfaction Trends in Follow-up Feedback', xLabelRotation=45)


# Learning Session Evaluation Suggestions:
#1. Target Areas with Lower 'Good' Ratings: Focus on improving the content or delivery methods in areas with higher 'Good' ratings to push them into the 'Excellent' category.
#2. Engagement and Clarity: Reduce the number of 'N/A' responses by ensuring that all content is clear and engaging."
# New Teammate Feedback Suggestions:
#Focus on Detailed Feedback: Even though there are no 'Poor' ratings, analyzing written feedback or conducting follow-up interviews can provide insights into improving the 'Good' and 'Fair' ratings.
#Consistency in Excellent Ratings: Ensure consistency in the quality of the onboarding process to maintain high 'Excellent' ratings.
#Follow-up Feedback Suggestions:")
#1. Address any areas with lower 'Good' ratings to enhance follow-up experiences.
#2. Improve engagement and clarity to reduce the number of 'N/A' responses.
