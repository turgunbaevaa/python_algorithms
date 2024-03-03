#include <stdio.h>
#include <stdlib.h>

// Define a struct to store student information
typedef struct {
    int roll_number;
    char first_name[20];
    char surname[20];
    int age;
    int grade;
} Student;

int main() {
    Student students[20];

    // Ask the user to enter data for the first three students
    for (int i = 0; i < 3; i++) {
        printf("Enter data for student %d:\n", i+1);
        printf("Roll Number: ");
        scanf("%d", &students[i].roll_number);
        printf("First Name: ");
        scanf("%s", students[i].first_name);
        printf("Surname: ");
        scanf("%s", students[i].surname);
        printf("Age: ");
        scanf("%d", &students[i].age);
        printf("Grade: ");
        scanf("%d", &students[i].grade);
    }

    // Save first name, surname, and grade of the students in a text file
    FILE *file = fopen("students.txt", "w");
    if (file == NULL) {
        printf("Error opening file\n");
        return 1;
    }

    for (int i = 0; i < 3; i++) {
        fprintf(file, "%s %s %d\n", students[i].first_name, students[i].surname, students[i].grade);
    }

    fclose(file);

    return 0;
}
