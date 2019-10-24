from timeit import default_timer as timer

class Timer:
    def __init__(self, name):
        self.start = 0
        self.stop = 0
        self.file_name = f"{name}.txt"
        self.benchmarks = []

    def start_timer(self):
        self.start = timer()
    
    def stop_timer(self):
        self.stop = timer()
        assert self.stop >= self.start, "Timer error"

    def show_benchmark(self):
        time_elapsed = self.stop - self.start
        self.add_benchmark(time_elapsed)
    
    def show_all_benchmarks(self):
        self.load_benchmarks()
        ctr = 1
        print("ALL benchmarks:")
        for benchmark in self.benchmarks:
            print(f"{ctr}. {benchmark}")
            ctr+=1

    def add_benchmark(self, benchmark):
        with open(self.file_name, "a+") as f:
            f.write(str(benchmark))
            f.write("\n")

    def load_benchmarks(self):
        with open(self.file_name, "r+") as f:
            self.benchmarks = f.readlines()
        self.benchmarks = [item.strip() for item in self.benchmarks]