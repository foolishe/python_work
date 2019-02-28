from collections import namedtuple
import queue
import random


Result = namedtuple('Result','count average')


# 子生成器

def averager():
    total = 0.0
    count = 0
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total/count
    return Result(count,average)


# 委派生成器

def grouper(results,key):
    while True:
        results[key] = yield from averager()
        print(results[key])


#客户端代码，调用方

def main(data):
    results = {}
    for key, values in data.items():
        group = grouper(results,key)
        print(next(group))
        for value in values:
            print(group.send(value))
        group.send(None)
    return results

def report(results):
    for key, result in sorted(results.items()):
        group,unit = key.split(';')
        print('{:2} {:5} averaging {:.2f}{}'.format(
            result.count,group,result.average,unit))

data = {
    'girls;kg':
        [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
    'girls;m':
        [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
    'boys;kg':
        [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
    'boys;m':
        [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46],
}

if __name__ == '__main__':
    report(main(data))

average1 = averager()
for i in range(4):
    print(next(average1))
    average1.send(1)

Event = namedtuple('Event','time proc_id action')




def taxi_process(ident,trips,start_time=0):

    time = yield Event(start_time,ident,'leave garage')

    for i in range(trips):
        time = yield Event(time,ident,'pick up passenger')
        time = yield Event(time,ident,'drop off passenger')

    yield Event(time,ident,'going home')

taxi = taxi_process(ident=13, trips=2, start_time=0)
print(next(taxi))
print(taxi.send(7))


class Simulator:

    def __init__(self, procs_map):
        self.events = queue.PriorityQueue()
        self.procs = dict(procs_map)

    def run(self,end_time):
        for _, proc in sorted(self.procs.items()):
            first_event = next(proc)
            self.events.put(first_event)

        sim_time = 0
        while sim_time < end_time:
            if self.events.empty():
                print('*** end of events ***')
                break

            current_event = self.events.get()
            sim_time, proc_id, previous_action = current_event
            print('taxi:',proc_id,proc_id * '  ', current_event)
            active_proc = self.procs[proc_id]
            next_time = sim_time + random.randrange(1,20)
            try:
                next_event = active_proc.send(next_time)
            except StopIteration:
                del self.procs[proc_id]
            else:
                self.events.put(next_event)
        else:
            msg = '*** end of simulation time: {} events pending ***'
            print(msg.format(self.events.qsize()))


taxis = {0: taxi_process(ident=0, trips=2, start_time=0),
         1: taxi_process(ident=1, trips=4, start_time=5),
         2: taxi_process(ident=2, trips=6, start_time=10)}
sim = Simulator(taxis)
sim.run(500)

# yield from

# RESULT = yield from (EXPR)

"""
_i = iter(EXPR)
try :
    _y = next(_i)
except StopIteration as _e:
    _r = _e.value
else:
    while 1:
        try:
            _s = yield _y
        except GeneratorExit as _e:
            try:
                _m = i.close
            except AttributeError:
                pass
            else:
                _m()
            raise _e

        except BaseException as _e:
            _x = sys.exc_info()
            try:
                _m = _i.throw
            except AttributeError:
                raise _e
            else:
                try:
                    _y = _m(*_x)
                except StopIteration as _e:
                    _r = _e.values
                    break
        else:
            try:
                if _s is None:
                    _y = next(_i)
                else:
                    _y = _i.send(_s)
            except StopIteration as _e:
                _r = _e.value
                break

    RESULT = _r

"""
