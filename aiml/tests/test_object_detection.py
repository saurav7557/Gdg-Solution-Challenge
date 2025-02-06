import pytest
from ai.object_detection import ObjectDetection

def test_detect_objects_in_video():
    object_detection = ObjectDetection(model_path='data/models/yolo_weights.onnx')
    object_detection.detect_objects_in_video('data/raw_videos/sample_video.mp4')
    assert True
