#!/usr/bin/env python3

from ast import Num
from os import system


def main():
    # multiply csv
    multi_data = "multi_data.csv"
    with open(multi_data, "w") as f:
        f.write("NMB, LOCAL_SIZE, NUM_WORK_GROUPS,Performance (Giga)\n")
    
    # multiply and add csv
    multi_add_data = "multi_add_data.csv"
    with open(multi_add_data, "w") as f:
        f.write("NMB, LOCAL_SIZE, NUM_WORK_GROUPS,Performance (Giga)\n")
    
    # reduce csv
    mult_reduce_data = "mult_reduce_data.csv"
    with open(mult_reduce_data, "w") as f:
        f.write("NMB, LOCAL_SIZE, NUM_WORK_GROUPS,Performance (Giga)\n")
    
    #multiply and multiply add
    for local_size in list(range(8, 513, 24)):
        for nmb in list(range(1024, 8389633, 262144)):
            cmd = ("g++ -DLOCAL_SIZE={} -DNMB={} -o mult multiAndAdd.cpp "
                "CL/libOpenCL.so -lm -fopenmp").format(local_size, nmb)
            system(cmd)
            cmd = "./mult {} multiply.cl".format(multi_data)
            system(cmd)
            cmd = ("g++ -DLOCAL_SIZE={} -DNMB={} -o mult_add multiAndAdd.cpp "
                "CL/libOpenCL.so -lm -fopenmp").format(local_size, nmb)
            system(cmd)
            cmd = "./mult_add {} multiAndAdd.cl".format(multi_add_data)
            system(cmd)


    for local_size in list(range(32, 256, 32)):
        for nmb in list(range(1024, 20389633, 262144)):
            cmd = ("g++ -DLOCAL_SIZE={} -DNMB={} -o mult_reduce multiAndReduce.cpp "
                "CL/libOpenCL.so -lm -fopenmp").format(local_size, nmb)
            system(cmd)
            cmd = "./mult_reduce {} multiAndReduce.cl".format(mult_reduce_data)
            system(cmd)
    cmd = "rm -f mult mult_add mult_reduce"
    system(cmd)


if __name__ == "__main__":
    main()
