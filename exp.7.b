#include <stdio.h>
void addmatrix(int ar1[2][2], int ar2[2][2],int add[2][2]){

   for(int i =0; i<2;i++){
       for(int j=0;j<2;j++){
           add[i][j]=ar1[i][j]+ar2[i][j];
       }
   }}
   int main() {
       int ar1[2][2],ar2[2][2],add[2][2];
       printf("enter array1: \n");
       for(int i=0;i<2;i++){
           for(int j=0;j<2;j++){
               scanf("%d",&ar1[i][j]);
           }
       }
       printf("enter array2: \n");
       for(int i=0;i<2;i++){
           for(int j=0;j<2;j++){
               scanf("%d",&ar2[i][j]);
           }}
               
                addmatrix(ar1,ar2,add);
    printf("sum of array 1 and 2: ");
       for(int i=0;i<2;i++){
           for(int j=0;j<2;j++){
               printf(" %d ",add[i][j]);
           }}
}
