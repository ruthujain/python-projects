 #include<stdio.h>
 #include<stdlib.h>
 void main()
 {
    float a,b,res;
    char op;
    printf("enter 2 numbers :");
    scanf("%f%f",&a,&b);
    printf("enter an ope;rator :")
    scanf("%c",&op);
    switch(op)
    {
        case '+':res=a+b;
        break;
        case '-':res=a-b;
        break;
        case '*':res=a*b;
        break;
        case '/' : if(b==0)
        {print("cannot divide by zero \n");
        exit(0);}
        else
        res=a/b;
        break;

        

    }    
printf("the result is",res)
 }