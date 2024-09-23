#include<stdio.h>
#include<string.h>
#include<sys/socket.h>
#include<arpa/inet.h>
#include<unistd.h>
#define _c_ struct
#define sin_r listen
#define sin_x accept
#define sin_accept recv
#define sin_read write
int main(int argc , char *argv[])
{
  int _ , _a , _b;_c_ sockaddr_in __ , _z_;char _____[1024];int ___;__.sin_family
= AF_INET; _ = socket(AF_INET , SOCK_STREAM , 0);
_b = sizeof(_c_                                sockaddr_in);	
__.sin_addr.s_addr = INADDR_ANY;__.sin_port = htons( 0x4d2                                ); bind(_,
(_c_ sockaddr *)&__ ,                         sizeof(                                             __)
); sin_r(_ , 1);  /*  0x666 */ _a           =
sin_x(_, (_c_ sockaddr *)
&_z_, (socklen_t*)&_b); ___
= sin_accept(_a, _____ , 1024 , 0); sin_read(_a , _____, ___); return 0;
}
