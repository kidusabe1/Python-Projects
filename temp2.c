#include <stdio.h>
#include <stdlib.h>
typedef struct students{
    char name[50];
    int rollno;
    char gender[6];
    float english;
}students;
int main()
{
    int n,i,j;
    printf("Provide the number of students\n");
    scanf("%d",&n);
    students* ptr= (students*) malloc(n*sizeof(students));
    
    for(i=0;i<n;i++)
    {
        printf("Give the name of student %d\n",i+1);
        scanf("%s",&(ptr+i)->name);
        printf("Give the roll number\n");
        scanf("%d",&(ptr+i)->rollno);
        printf("Give the gender\n");
        scanf("%s",&(ptr+i)->gender);
        printf("English marks\n");
        scanf("%f",&(ptr+i)->english);
    }

    for(i=0;i<n;i++)
    {
        printf("Student name= %s\n", (ptr+i)->name);
        printf("\n");
        printf("Student roll number= %d\n",(ptr+i)->rollno);
        printf("\n");
        printf("Student Gender= %s\n",(ptr+i)->gender);
        printf("\n");
        printf("English Result= %2.2f\n",(ptr+i)->english);
        printf("\n");
        printf("=======================================================================================================\n");
        printf("=======================================================================================================\n");
    }
    return 0;
}