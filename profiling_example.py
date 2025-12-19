import cProfile

def slow_sum():
    total = 0
    for i in range(1_000_000):
        total += i
    return total

def fast_sum():
    return sum(range(1_000_000))

if __name__ == "__main__":
    print("Profiling slow_sum()")
    cProfile.run("slow_sum()")

    print("\nProfiling fast_sum()")
    cProfile.run("fast_sum()")
