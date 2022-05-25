kernel
void
ArrayMultReduce( global const float *dA, global const float *dB, local float *prods, global float *dC)
{
	int gid = get_global_id( 0 );
    int numItems = get_local_size(0);
    int threadNum = get_local_id(0);
    int workingGroupNum = get_group_id(0);
    
    prods[threadNum] = dA[gid]*dB[gid];

    for(int offset = 1; offset < numItems; offset *= 2) {
        int mask = 2*offset - 1;
        barrier(CLK_LOCAL_MEM_FENCE);
        if((threadNum & mask) == 0)
            prods[threadNum] += prods[threadNum + offset];
    }

    barrier(CLK_LOCAL_MEM_FENCE);
    if(threadNum == 0)
        dC[workingGroupNum] = prods[0];

}