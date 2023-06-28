#include <bits/stdc++.h> 

pair<int,int> missingAndRepeating(vector<int> &arr, int n)
{
    // Write your code here 
    int missing_no=0, repeating_no=0;
    int xor1 = arr[0];
    for(int i=1; i<n; i++) {
        xor1 ^= arr[i];
    }
    for(int i=1; i<=n; i++) {
        xor1 ^= i;
    }
    
    int set_bit_no = xor1 & -xor1;
    for(int i=0; i<n; i++) {
        if(set_bit_no & arr[i])
            missing_no ^= arr[i];
        else
            repeating_no ^= arr[i];
    }
    for(int i=1; i<=n; i++) {
        if(set_bit_no & i)
            missing_no ^= i;
        else
            repeating_no ^= i;
    }
    
    for(int i=0; i<n; i++) {
        if(arr[i] == missing_no)
            return {repeating_no, missing_no};
        else if(arr[i] == repeating_no)
            return {missing_no, repeating_no};
    }
}
