#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
 FILE* ptr1 = fopen("card.raw","r");
 FILE* ptr2= fopen("card.raw","w");


uint8_t *buffer= malloc(520 );



while(!(fread(&buffer,520,1,ptr1)==NULL))
    {
            if(fread(&buffer,520,1,ptr1)== (0xff && 0xd8 && 0xff));
        {
            fwrite(&buffer, 520,1,ptr2)
        }
    }
    free(buffer);
    fclose(ptr1);
    fclose (ptr2);
}