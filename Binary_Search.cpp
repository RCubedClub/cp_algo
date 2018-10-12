#include <bits/stdc++.h> 
using namespace std; 
  
// Show function is used to print array  
void show(int a[], int arraysize) 
{ 
    for (int i = 0; i < arraysize; ++i) 
        cout << a[i] << " ";
    cout<<endl;
} 

int binarySearch(int arr[], int l, int r, int x) 
{ 
   if (r >= l) 
   { 
        int mid = l + (r - l)/2; //(l+r)/2 can be written but it may cause range problem
  
          if (arr[mid] == x)  // If the element is present at the middle  
            return mid; 
  
          if (arr[mid] > x)   // If element is smaller than mid, then
            return binarySearch(arr, l, mid-1, x); // it can only be present in left subarray 
  
        // Else the element can only be present in right subarray
        return binarySearch(arr, mid+1, r, x); 
   } 
   // We reach here when element is not present in array  
   return -1; 
}   
int main() 
{ 
    int a[] = { 1, 5, 8, 9, 6, 7, 3, 4, 2, 0 }; 
    int asize = sizeof(a) / sizeof(a[0]); 
    cout << "\n The array is : "; 
    show(a, asize); 
    
    sort(a, a + asize);//Binary sort is applied only on the sorted array
    int element = 6;//element we want to search
    if(binarySearch(a,0,10,element))
      cout<<"You search: "<<element<<", it is present";
    else 
      cout<<"You search: "<<element<<", it is not present";
    
    return 0; 
} 
