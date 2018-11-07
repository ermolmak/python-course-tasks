import time


class Timer:
    def __enter__(self):
        self.start_time = time.process_time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop_time = time.process_time()
        print('This block has been working for '
              f'{self.stop_time - self.start_time} s')
        return exc_type is None


if __name__ == '__main__':
    def bubble_sort(a):
        for i in range(len(a) - 2, -1, -1):
            for j in range(i + 1):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]


    a = list(reversed(range(10)))
    with Timer():
        bubble_sort(a)

    a = list(reversed(range(100)))
    with Timer():
        bubble_sort(a)

    a = list(reversed(range(1_000)))
    t = Timer()
    with t:
        bubble_sort(a)

    a = list(reversed(range(10_000)))
    with t:
        bubble_sort(a)
