# BAbbLe-An-Interactive-Online-dictionary

INDIRA GANDHI DELHI TECHNICAL UNIVERSITY FOR WOMEN

IT WORKSHOP PROJECT SYNOPSIS

BAbbLe:An Interactive Online dictionary

Team: Group No.7 (B.Tech CSE- AI 2nd Semester)

01901172021 Shreya Mittal

02301172021 Anshu Roy

04201172021 Srishti Gupta
-- https://github.com/srishtig2412

Objectives of the project:

A Dictionary is the most important tool to understand the
vocabulary of any language because it has all the words that are
there in the vocabulary of a language listed in it. This Dictionary
is a GUI based dictionary, built using python and its various
modules. GUI is created using Tkinter.

Following are the functions in this Dictionary

1. To get the meaning of the word.

2. To provide word suggestions in case of misspelling.

3. To get antonym and synonym of the word.

4. By supplementing audio pronunciation at different pace as
per user’s comfort.

5. Vocabulary Enrichment - Improving user’s vocabulary by
teaching a new word every time the app is opened.


Terminal Setup:

In order to create this application, Concepts of Tkinter , gTTS(python
libraries),JSON, File Reading, Python Data Structure and difflib
module are being used.

1.Tkinter – A python framework that will enable us to create
GUI elements using its widgets found in the Tk toolkit.

2. JSON file: This contains vocabularies that will be checked against
giving meaning, antonym and synonym of words asked for. Vocabulary
enrichment feature is implemented by getting random objects from the
json file using random module.

3.difflib will help us compare various sequences and give us a list of
words which are close to what the user intended to search for.
(If we ask for the meaning of ‘wrd’, which could be a misspelling of —
[‘word’, ‘world’, ‘weird’] then the application will ask for selecting the
desired option and returning us the desired result.
And there it is, we created a Dictionary App which helps users even in case
of misspell or mistype.)

4.Google text to speech: An API created by google which is integrated
with a Python module called gtts.We will use the gTTS function to create
an object which will read the text and convert it to an audio object. We
can use many parameters with this function like reducing the speed of
the output using the slow argument.

5.Data Structures are fundamentals of any programming language
around which a program is built. Python helps to learn the fundamentals
of these data structures in a simpler way as compared to other
programming languages. It includes list, set, tuples, and dictionary.


Future Scope and Implementation:

1. Search using speech detection.

2. Translation to Hindi and other native languages.

3. Stating the origin of the word.

4. Showing how the word can be used in different ways by
different sentence formations .

5. Interactive quizzes and games to enrich v
