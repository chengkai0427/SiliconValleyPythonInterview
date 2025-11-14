'''
This program takes a list of strings representing the start and end times of N processes and returns a list of integers representing the total execution time of each process.

The input is a list of strings where each string has the format "process_id:start/end:timestamp". The "start" and "end" strings indicate whether the process started or ended, and the "timestamp" is the time at which the event occurred.

The output is a list of integers where the i-th integer represents the total execution time of the i-th process.

Here's the code:
'''
def exe_time(run_log:list[str],N:int)->list[int]:
    timestamps = []
    for line in run_log:
        l = line.split(":")
        timestamps.append((int(l[0]), l[1], int(l[2])))
    result=[0]*N
    stk=[]
    for t in timestamps:
        if t[1]=="start":
            stk.append(t)
        else:
            duration=t[2]-stk.pop()[2]+1
            result[t[0]]+=duration
            if stk:
                result[stk[-1][0]]-=duration
    return result
if __name__=="__main__":
    run_log = [
        "0:start:0",
        "1:start:2",
        "1:end:5",
        "0:end:6",
        "2:start:7",
        "1:start:8",
        "1:end:10",
        "0:start:11",
        "0:end:12",
        "2:end:13"
        ]
    print(exe_time(run_log,3))