#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void rotate( string text, int k);
int main(int argc, string argv[])
{

if (argc!=2)
{
   printf("caesar/ ./caesar insert key k:\n");
   return 1;
}
if (atoi(argv[1]) < 0)

 {
    printf ("k must be greater than 0\n");
    return 2;
 }

int k= atoi(argv[1]);
string text= get_string("Insert text here:");
printf("plain text: %s\n",text);

rotate (text, k);

printf("\n");
}


void rotate( string text, int k){

   for ( int i=0; i<strlen(text); i++)
{

 char ciphered_text= (text[i] -97 +k) % 26 + 97;
if ((ciphered_text>= 'A'&&  ciphered_text <= 'Z')|| (ciphered_text >= 'a' && ciphered_text<= 'z'))
   {  printf ("%c", ciphered_text);
     }
   else {
   printf( "%c", text[i]);
           }
  }
}


