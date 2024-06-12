# UI and API tasks from SQA Assignment
Solution for UI and API tasks from SQA Assignment built on Python, Selenium WebDriver, using page object model and requests library. UI task focuses on getting to "Philosophy" article at English Wikipedia by clicking first valid link in each article. API tasks are about NASA media library, printing to console information on 5 photographs and printing to console link to every video file for 5 obtained videos. There are also few assertions performed in API tasks.\
Following steps describe actions needed to run tests in PyCharm on Windows operating system. The steps are mostly described briefly so they don't cover all possible issues though some specific actions are described in more detail.

## Python installation
- Go to https://www.python.org/downloads/.
- Under „Download the latest version for Windows“ click button „Download Python \<version number\>“ and save the file.
- Run downloaded .exe file. It is OK to select „Install Now“ without any further configuration.

## Getting repository content
GitHub repository content can be downloaded in 2 ways:
1) By cloning the repository:
   - In desired folder run command "git clone https://github.com/OMGitH/SQA-Assignment.git".
   - Note: A Git has to be installed on local computer. Can be downloaded from https://git-scm.com/. It is OK to leave all settings default during installation.
2) As a zip file:
   - Click green "\<\> Code" button.
   - Select "Download ZIP" and save it to desired folder.
   - Unzip downloaded .zip file.

## PyCharm installation
- Go to https://www.jetbrains.com/pycharm/download/#section=windows.
- Click „Download“ button under „PyCharm Community Edition“ and save the file.
- Run downloaded .exe file and install PyCharm. There is no need to change anything during installation.

## PyCharm configuration
- Run PyCharm. At „Import PyCharm Settings“ dialog, choose whether you want to import settings or not.
- At „Data Sharing“ choose whether you want to share data or not.
- At „Welcome to PyCharm“, click „Open“ button, go to location where „SQA-Assignment“ folder is located. Select „SQA-Assignment“ folder and click „OK“. If there is a question about trust, click „Trust Project“.
- If there is a message about Java options environment variables displayed, it is OK to close it.
- If there is a message about Invalid VCS root mapping, it is OK to close it.
- Click hamburger menu in top left corner, go to „File“ – „Settings“ – „Project: SQA-Assignment“ – „Python Interpreter“ and click „Add Interpreter“ – „Add Local Interpreter...“. In following window in field „Base interpreter“ there shall be prefilled path to installled Python. If not, select it there. Click „OK“ button, virtual environment will be created. In „Python Interpreter“ field there is now path to Python in virtual environment displayed. Close window by clicking „OK“ button and wait for the project to get updated.
- Click hamburger menu in top left corner, go to „File“ – „Settings“ – „Tools“ – „Python Integrated Tools“:
   - In field „Package requirements file“ select „requirements.txt“ file that is in „SQA-Assignment“ folder.
   - Click „Apply“ button and close window by „OK“ button.
- In project navigator go to „SQA-Assignment\ui_task“ and open file „ui_task.py“. Once file is opened, at the top of the screen there is shown message saying that package requirements are not satisfied. In the message click „Install requirements“, in displayed window leave all packages ticked, click „Install“ button and wait for the packages to get installed.

## Execution
- In PyCharm in project navigator open file „api_task.py“ that is in „SQA-Assignment\api_task“ for running API task or file „ui_task.py“ that is in „SQA-Assignment\ui_task“ for running UI task.
- Once desired file is opened, right click into the code and select „Run 'api_task'“ or „Run 'ui_task'“ to run API task or UI task.
- Note: First run of UI task may take longer to start as webdrivers are downloaded.