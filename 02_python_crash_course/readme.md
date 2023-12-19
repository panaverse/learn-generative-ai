# Learn Modern Python with Type Hints As Fast as Possible From Scratch For GenAI App and API Development

We will learn Modern Python from this text book: 

[Python Crash Course - Third Edition Chapters 1-10](https://www.amazon.com/Python-Crash-Course-Eric-Matthes/dp/1718502702)

There is only one issue with the book, it has been recentely published but doesnot cover type hints, we have enhanced the source code for the book with type hints.

To learn type hints you may refer to this Typing Cheat Sheet while reading the book:

[Typing Cheat Sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)

[Python Cheat Sheet for Beginners](https://www.datacamp.com/cheat-sheet/getting-started-with-python-cheat-sheet)


### Type Hints should be used by Professional Developers

Type hints are the biggest change in the history of Python since the unification of types and classes in Python 2.2, released in 2001. However, type hints do not benefit all Python users equally. That’s why they should always be optional.

The goal of Type Hints is to help developer tools find bugs in Python codebases via static analysis, i.e., without actually running the code through tests. The main beneficiaries are professional software engineers using IDEs (Integrated Development Environments) and CI (Continuous Integration). The cost-benefit analysis that makes type hints attractive to this group does not apply to all users of Python. However, we are professional developers, therefore it is beneficial for us to adopt type hints. This Modern Python course uses Type Hints extensively. 


# Installation

[Install Anaconda with Python 3.12](https://www.anaconda.com/download) 

[Install VS Code](https://code.visualstudio.com/)

[Install Python Plugin](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

[Install mypy](https://mypy.readthedocs.io/en/stable/getting_started.html)

[Install mypy VS Code Extension](https://marketplace.visualstudio.com/items?itemName=matangover.mypy)

### Commands to Upgrade to Latest Python 3.12 in Anaconda

First Check if you have Python 3.12 installed by default after installing Anaconda:

    python --version

If you do not have Python 3.12 or higher create a new envirnoment and check again:

    conda create --name myenv3_12 python=3.12
    conda env list
    conda activate myenv3_12
    python --version



## Tools for Teaching and Learning

We will using the following tools for teaching in our classes:

### AI-assisted application development

https://cloud.google.com/duet-ai?hl=en

### Zoom

https://zoom.us/

### Goolge Class Room

https://classroom.google.com/

### Google Colaboratory

https://colab.google/ 

Colab, or ‘Colaboratory’, allows you to write and execute Python in your browser, with:

1. Zero configuration required
2. Access to GPUs free of charge
3. Easy sharing

[Implementing Google Colab into your Google Classroom](https://katiesylvia.medium.com/implementing-google-colab-into-your-google-classroom-88cf22841176)

[Watch](https://www.youtube.com/watch?v=inN8seMm7UI)

Alternatives:

https://deepnote.com/blog/best-colab-alternatives


### Live Share Classroom Lab Lectures

When instructors are teaching a lesson, they can use Live Share to share their project with students, instead of simply presenting their screen. This allows the entire class to follow along with the teacher, while being able to interact with the project on their own. Additionally, the teacher can ask individual students to assist in solving a particular portion of the lesson (e.g. "Which method should we call here?"), which can help in the social aspects of the class, without requiring students to walk up to the front of the room, or even be physically present in the same room (e.g. online courses).

To aid in classroom settings, Live Share enables sharing in read-only mode. Instructors can use read-only mode to enable them to share their projects with students without having to worry about unnecessary or accidental edits being made.

Additionally, Live Share has support to enable up to 30 guests joining into a collaboration session. This way, instructors can have their whole class join into a session and view code together.

To enable this feature:

VS Code: Add "liveshare.increasedGuestLimit":"true" to settings.json.
VS: Set Tools > Options > Live Share > Increased guest limit to "True"

[What is Visual Studio Live Share?](https://learn.microsoft.com/en-gb/visualstudio/liveshare/)

[Collaborate with Live Share](https://code.visualstudio.com/learn/collaboration/live-share)

### Online Whiteboarding App: Jamboard

We will be using Google’s Jamboard during my sessions, as it’s free and integrates nicely with the rest of the Google suite. It doesn’t offer unlimited canvas but divides your drawings up into slides similar to Powerpoint. I’ve found this works well to provide your student with reference slides they can use to study. 

https://jamboard.google.com/

Note: We can using the Apple iPad with the Apple Pencil with the Jamboard app, which works very well. 
