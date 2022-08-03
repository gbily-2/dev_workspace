#include <iostream>
#include <stdlib.h>
#include <sys/socket.h>

int main(int argc, char ** argv)
{
    if (argc < 2)
    {
        std::cout << "Usage: " << argv[0] << "<port number>" << std::endl;
    }
    int port = atoi(argv[1]);
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in address;
    
    
}
