#include "helpers.h"
#include <math.h>


// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i=0; i< height; i++)
    {
        for (int j=0; j< width; j++)
        {

           uint8_t average = (uint8_t)(round(((float)image[i][j].rgbtBlue + (float)image[i][j].rgbtGreen + (float)image[i][j].rgbtRed) /3));


                image[i][j].rgbtBlue= average;
                image[i][j].rgbtGreen= average;
                image[i][j].rgbtRed= average;
        }
    }

    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
     for (int i=0; i< height; i++)
    {
        for (int j=0; j< width; j++)
        {
           int sepiaRed = round(.393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue);
           int sepiaGreen = round(.349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue);
           int sepiaBlue = round(.272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue);


        if (sepiaRed>= 255){
                image[i][j].rgbtRed = 255;
            }
                else {
                    image[i][j].rgbtRed= (uint8_t)sepiaRed;
                }

                                                                                  // do three if statements aking if each type of colour is greater or equal to 255.
            if (sepiaGreen>= 255){
                image[i][j].rgbtGreen = 255;
            }
                else {
                    image[i][j].rgbtGreen= (uint8_t)sepiaGreen;
                }
                                                                               // if so, let that colour be that maximum value.
       if (sepiaBlue >= 255) {
            image[i][j].rgbtBlue = 255;
           }
            else {
                    image[i][j].rgbtBlue= (uint8_t)sepiaBlue;
             }

        }
    }

    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
const int width_minus = width - 1;
    for (int i=0; i< height; i++)
        {
            for(int j=0; j<width/2; j++)
            {
            
                uint8_t rgbtBlue = image[i][j].rgbtBlue;
                image[i][j].rgbtBlue = image[i][width_minus-j].rgbtBlue;
                image[i][width_minus-j].rgbtBlue= rgbtBlue;

                uint8_t rgbtGreen = image[i][j].rgbtGreen;
                image[i][j].rgbtGreen = image[i][width_minus-j].rgbtGreen;
                image[i][width_minus-j].rgbtGreen= rgbtGreen;
                uint8_t rgbtRed= image[i][j].rgbtRed;
               image[i][j].rgbtRed = image[i][width_minus-j].rgbtRed;
               image[i][width_minus-j].rgbtRed= rgbtRed;


            }
        }

    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{

int counter=0;
int siuumBlue=0;
int siuumGreen=0;
int siuumRed=0;
RGBTRIPLE tmp [height][width];
uint8_t siuumBlue2;
uint8_t siuumGreen2;
uint8_t siuumRed2;

for (int f=0; f< height; f++)
    {
        for (int c=0; c< width; c++)
           {
                tmp [f][c]= image [f][c];
            }
    }


    for (int i=0; i< height; i++)
    {
        for (int j=0; j<width; j++)
        {


            for (int l=i-1; l<i+2; l++)
            {
                for (int m= j-1; m<j+2; m++)
                {
                    if( l<0 || m>= width || l>= height)
                    {
                        break;
                    }
                    if (m < 0)
                    {
                        m+=1;
                    }
                     siuumBlue += (int) tmp[l][m].rgbtBlue;
                     siuumGreen +=(int) tmp[l][m].rgbtGreen;
                     siuumRed +=  (int) tmp[l][m].rgbtRed;
                    counter++;

                }

            }

            siuumBlue2= round((float)(siuumBlue)/(counter ));
            siuumGreen2= round((float)(siuumGreen)/(counter));
            siuumRed2= round((float)(siuumRed)/(counter ));

            counter=0;
            siuumBlue=0;
            siuumGreen=0;
            siuumRed=0;


        image[i][j].rgbtBlue = siuumBlue2;
        image[i][j].rgbtGreen = siuumGreen2;
        image[i][j].rgbtRed = siuumRed2;

        }

    }

    return;
}
