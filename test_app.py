#This python file will be used to test if the app.py work or not using pytest
from app import video_is_supported

#Check if the video_is_supported() from app.py function work properly or not in github action
def test_video_is_supported():
    assert video_is_supported("test.mp4") == True
