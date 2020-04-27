Reddit Flare Detector
======

A web interface use for detecting the flair_name of a reddit post.  (<https://flairdetector13.herokuapp.com/>).

## Final.ipnyb

This is a script to detect the flare of a reddit post.

### Usage

For Detecting the flair_name of a reddit post by giving input url of a post : (<https://flairdetector13.herokuapp.com/>)

The endpoint for automated_testing : (<https://flairdetector13.herokuapp.com/automated_testing>)

This endpoint will be used for testing performance of our classifier. User will send an automated POST request to
the end point with a .txt file which contains a link of a r/india post in every line. Response of the
request will be a json file in which key is the link to the post and value of predicted flare.

### Install

1. Assuming the repository is on Windows
2. Clone the github repository

    ```shell
   git clone https://github.com/paras213/Flair-Detector
   cd Flair-detector
    ```

3. Install Python 3 and required Python 3 packages:

    ```shell
    pip install -r requirements.txt
    ```


### Local Usage

Execute with Python 3:

for script run : 

```shell
jupyter notebook
```

for web application :

```shell
python manage.py runserver
```