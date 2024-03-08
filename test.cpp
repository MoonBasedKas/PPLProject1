#include <stdio.h>

class test {
    public:
        int x = 2;
        int z = 1;
};

int main(){
    test z;
    printf("%d", z.z);
}