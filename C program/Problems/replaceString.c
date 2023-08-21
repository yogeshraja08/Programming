#include<stdio.h>
#include<string.h>
void main(){
    char str[20], find, replace;
    // scanf("%s",str);
    // scanf("%c",&find);
    // scanf("%c",&replace);
    gets(str);
    find = getchar();
    replace = getchar();
    for (int i = 0; i < strlen(str); i++)
    {
        if (str[i]==find)
        {
            str[i]=replace;
        }
    }
    printf("%s",str);
}