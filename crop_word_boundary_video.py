def load_features(arr, filename, use_boundary=False, augment=True):
    """Loads the specified video features.
    Args:
        arr (np.array): The loaded numpy feature.
        filename (str): The name of the mp4 file.
    Returns:
        FloatTensor: the visual features of the video as a tensor
         (length, n_features)"""

    if use_boundary:
        meta_path = filename.split('.')[0] + '.txt'
        with open(meta_path, 'r') as f:
            duration = math.ceil(float(f.readlines()[-1].split(' ')[1]) * 25)
            st = math.ceil(((30 - duration)/2))
            ed = math.floor((30 + duration)/2)
    else:
        st, ed = 0, 29
    return arr[st: ed]


链接：https://pan.baidu.com/s/111kBHBo7Oyb0dwjkzdVTOQ 密码：es9e
