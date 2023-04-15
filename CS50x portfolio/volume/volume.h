
#include <stdio.h>

#include <stdint.h>


int main( int argc, char* argv[]) {

if (argc > 4 || argc < 4)
    {
        printf("No more than three line arguments and must be at least three line arguments\n")
        return 1;
    }
else
    {
        return true;
    }

        FILE* soundwaves = fopen("input.wav","r");
        int volume;
        char ch;

        while ((ch =fgetc(soundwaves))!= EOF)
        {

            printf("%c",ch);
        }

        


}

