#include <cs50.h>
#include <stdio.h>


void printhashes(int n);
void printpoints (int j);


int main(void)
{
int t;

do{
   t= get_int ("How tall must the pyramid be:");
}
while (t<0||t>8);

   int n= 1;
   int m= t;
   int l=t;
for (int j=0; j<t; j++)
{

   printpoints(m);
   printhashes (n);
   printf("\n");
   

   n++;
   m--;

   }
 }


void printhashes (int n){

   for (int i=0; i<n; i++){
      printf("#");
   }
}

void printpoints (int m){
   for (int d=m; d>0; d--){
 printf (" ");
}
}










