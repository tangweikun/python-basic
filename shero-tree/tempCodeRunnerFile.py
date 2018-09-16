dur = float(time.perf_counter - start)
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur), end='')
    time.sleep(0.1)
print("\n"+"执行结束".center(scale//2, '-'))
