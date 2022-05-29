import psutil
import time
import matplotlib.dates
import matplotlib.pyplot as plt


def cpu_count():

    print('-----------------------------cpu information ------------------ ---------------------')
    print(u"Physical CPUs: %s" % psutil.cpu_count(logical=False))
    print(u"Total number of CPU cores: %s" % psutil.cpu_count())
    print('RAM memory % used:', psutil.virtual_memory()[2])
    cpu1 = psutil.cpu_percent(1)
    cpu = (str(cpu1)) + '%'
    sys = time.localtime(time.time())
    sys_time = time.strftime("%H:%M:%S", sys)
    print(u"cpu usage rate: %s" % cpu)
    cpu_list = ["cpu usage rate", cpu1, sys_time]
    plt.plot(cpu)
    plt.plot(cpu1)
    plt.plot(cpu_list) #afisare ussage rate
    return cpu_list


def a():
    while 1:
        yield cpu_count()


from win10toast import ToastNotifier
  if cpu_count()>1:
        toaster = ToastNotifier()

        toaster.show_toast("titlu", "text", duration=2)


if __name__ == '__main__':
    fig = plt.figure(figsize=(10, 5))
    plt.xlabel("time")
    plt.xticks(rotation=60)
    plt.ylim(0, 100)
    plt.yticks([a for a in range(101) if a % 5 == 0])
    plt.ylabel("data")
    plt.title("test")
    plt.grid(True)  #
    plt.ion()  # interactive mode on
    try:
        while 1:
            data = next(a())
            plt.plot(data[2], data[1], linewidth='1', label="cpu", marker='o') #comanda care ne pune pe grafic
            #nu am reusit sa pun in loc de data[...] cpu_list , si celelalte variabile pentru cpu ( cu date ).
            #le-am pus in functia cpu_count
            plt.pause(0.1)
    except Exception as e:
        plt.ioff()
    plt.show()

