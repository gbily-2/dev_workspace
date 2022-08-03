#include <iostream>
#include <queue>
#include <thread>

class ThreadPool
{
    public:
        std::queue<std::thread> poolThread;
        int maximum;
    private:
        ThreadPool(){};
        void create_new_thread(std::thread newThread);
        void terminate_thread(std::thread threadToTerminate);
};

ThreadPool::ThreadPool()
{
    maximum = 4;
}
void ThreadPool::create_new_thread(std::thread newThread)
{
    poolThread.push(newThread);
}

void ThreadPool::terminate_thread(std::thread threadToTerminate)
{
    threadToTerminate.join();
}

