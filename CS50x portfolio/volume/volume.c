// Modifies the volume of an audio file

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Number of bytes in .wav header
const int HEADER_SIZE = 44;

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 4)
    {
        printf("Usage: ./volume input.wav output.wav factor\n");
        return 1;
    }

    // Open files and determine scaling factor
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    float factor = atof(argv[3]);
    uint8_t header_arr[44];
   // fread (header_arr, HEADER_SIZE, 1, input);
    //fwrite (header_arr, HEADER_SIZE, 1, output);
    fread (header_arr, sizeof(uint8_t),44, input);
    fwrite(header_arr, sizeof(uint8_t),44, output);

    // TODO: Copy header from input file to output file

   // int16_t *samples_arr= malloc(sizeof(int16_t)*(sizeof(input)-44));
   int16_t samples_arr;
   int16_t samples;

    while(fread (&samples_arr, sizeof(int16_t),1, input)== 1)
    {

        samples = samples_arr * factor;
        //samples_arr *= factor;

        fwrite(&samples, sizeof(int16_t),1, output);
    }

    // TODO: Read samples from input file and write updated data to output file

    // Close files
   // free(samples_arr);
    fclose(input);
    fclose(output);
}
