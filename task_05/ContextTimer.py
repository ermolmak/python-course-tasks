import time


class Timer:
    def __enter__(self):
        self.start_time = time.process_time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop_time = time.process_time()
        print('This block has been working for '
              f'{self.stop_time - self.start_time} s')
        return exc_type is None
