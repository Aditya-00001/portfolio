from flask import Flask, render_template, redirect, url_for
from wtforms import StringField, SubmitField, IntegerField, TextAreaField
from wtforms.fields import EmailField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap5
import os
from dotenv import load_dotenv
from smtplib import SMTP
load_dotenv()


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('csrf')
# ckeditor = CKEditor(app)
Bootstrap5(app)


class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired()])
    contact = IntegerField("Contact Number", validators=[DataRequired()])
    msg = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route('/')
def index():
    return render_template('index.html',skills=['Python','Machine Learning','HTML','CSS','Java','C++',
                                                'SQL','Python Pandas','Python Numpy','Gen AI'])


@app.route('/project')
def project():
    projects = [
        {
            'title': ' Robust biometric attendance system via content-based '
                     'feature extraction and classification of acknowledged sound',
            'description': 'Biometric attendance systems have simplified tracking but still present challenges, 
            such as users not being assured their attendance is recorded. A novel method using machine learning addresses
            this by analyzing thank-you sounds from biometric devices. The system applies signal processing techniques like 
            Mel-frequency cepstral coefficients (MFCC) and Mel spectrograms to distinguish genuine acknowledgments from noise. 
            This scalable and versatile solution integrates seamlessly with existing systems, automating attendance tracking
            while providing users with confirmation that their attendance has been recorded.',
            'link': None,  # This project has a link
            'image': url_for('static',filename='projects/attendance.png'),  # Replace with actual image URL
            'skills': ['Python', 'App Development','Machine Learning']  # Add skills related to the project
        },
        {
            'title': 'Instagram Automation',
            'description': 'n the dynamic world of social media, maintaining an active presence on platforms like '
                           'Instagram can be a daunting task. To address this challenge, I developed an Instagram '
                           'Automation Tool that leverages Python and Selenium to automate key interactions, '
                           'enabling users to focus on what truly matters—creating engaging content.',
            'link': 'https://github.com/Aditya-00001/Instagram-Automation',  # This project does not have a link
            'image': url_for('static',filename='projects/instabot.png'),  # Replace with actual image URL
            'skills': ['Python', 'Selenium', 'HTML', 'CSS']  # Add skills related to the project
        },
        {
            'title': 'Morse Code converter',
            'description': 'The Text to Morse Code Converter is a command-line interface (CLI) application designed to '
                           'facilitate the conversion of text into Morse code and vice versa. T'
                           'his project aims to provide users with an intuitive tool for encoding and decoding messages '
                           'using the universal language of Morse code.',
            'link': 'https://github.com/Aditya-00001/python-professional/blob/main/textToMorse.py',  # This project does not have a link
            'image': url_for('static', filename='projects/morse.png'),  # Replace with actual image URL
            'skills': ['Python']  # Add skills related to the project
        },
        # Add more projects as needed
    ]

    return render_template('project.html', projects=projects)


@app.route('/contact', methods=['Get','Post'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        cont = form.contact.data
        msg = form.msg.data
        my_email = os.getenv('my_send')
        password = os.getenv('pass')
        send = os.getenv('my_Email')
        with SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,to_addrs=send,
                                msg=f"Subject: Portfolio Message from {email}\n\n By- {email}\n phone - {cont}\nMessage:\n{msg}")
            connection.close()
        return render_template('contact.html',show_thank_you=True,form=form)
    return render_template('contact.html', form=form,show_thank_you=False)

if __name__ == "__main__":
    app.run(debug=True)
