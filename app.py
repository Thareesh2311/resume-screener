import streamlit as st
import pickle
import re
import nltk

nltk.download('punkt')
nltk.download('stopwords')

#loading the models
clf = pickle.load(open('model.pkl', 'rb'))
tfidf = pickle.load(open('tfidf.pkl', 'rb'))


def cleanResume(txt):
    cleanText = re.sub('http\S+\s*', ' ', txt)  # Remove URLs
    cleanText = re.sub('RT|cc', ' ', cleanText)  # Remove RT and cc
    cleanText = re.sub('#\S+', ' ', cleanText)  # Remove hashtags
    cleanText = re.sub('@\S+', ' ', cleanText)  # Remove mentions
    cleanText = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', cleanText)  # Remove punctuation
    cleanText = re.sub(r'[^\x00-\x7f]', ' ', cleanText)  # Remove non-ASCII characters
    cleanText = re.sub('\s+', ' ', cleanText)  # Replace multiple spaces with single space
    return cleanText.strip()  # Remove leading/trailing spaces


#WebApp
def main():
    st.title('Resume Screening App')
    uploaded_file = st.file_uploader('Upload Resume', type=['pdf', 'txt'])
    if uploaded_file is not None:
        try:
            resume_bytes = uploaded_file.read()
            resume_text = resume_bytes.decode('utf-8')

        except UnicodeDecodeError:
            resume_text = resume_bytes.decode('Latin-1')

        cleaned_Resume = cleanResume(resume_text)
        input_features = tfidf.transform([cleaned_Resume])
        prediction_id = clf.predict(input_features)[0]

        category_mapping = {
            15: "Java Developer",
            23: "Testing",
            8: "DevOps Engineer",
            20: "Python Developer",
            2: "Hadoop",
            7: "C++",
            3: "Python",
            18: "Ruby on Rails",
            3: "C",
            6: "Data Science",
            69:"Full Stack Developer"

        }
        category_name = category_mapping.get(prediction_id, "Unknown")
        st.write("Predicted Category:", category_name)
        st.write(prediction_id)

#python main
if __name__ == '__main__':
    main()
