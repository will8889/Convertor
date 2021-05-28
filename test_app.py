from app import video_is_supported

def test_video_is_supported():
    assert video_is_supported("test.mp4") == True