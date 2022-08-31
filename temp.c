#include <stdio.h>
#include <stdlib.h>

int main()
{
    int *ptr[2];
    for(int i=0;i<2;i++)
    {
        ptr[i]= (int*) malloc(2*sizeof(int));
    }

    if(ptr[1]==NULL)
    {
        printf("Insufficient memory\n");
        return 0;
    }

    for(int i=0;i<2;i++)
    {
        for(int j=0;j<2;j++)
        {
            printf("Element: ");
            scanf("%d",&ptr[i][j]);
        }
    }

    for(int i=0;i<2;i++)
    {
        for(int j=0;j<2;j++)
        {
            printf("%d ",ptr[i][j]);
        }
        printf("\n");
    }

    for(int i=0;i<2;i++)
    {
        free(ptr[i]);
    }
    return 0;
}

// write a program using array of pointers to a structure, to read and display data of a student