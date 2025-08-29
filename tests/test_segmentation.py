from src.core.segmentation import segment_by_delta


def test_segment_by_delta():
    pts = [(0, 1.0), (60, 1.2), (120, 3.2), (200, 3.3)]
    segs = segment_by_delta(pts, delta=1.0, min_len=50)
    assert len(segs) == 2
    assert segs[0].pk_from == 0 and segs[0].pk_to == 120
    assert segs[1].pk_from == 120 and segs[1].pk_to == 200
