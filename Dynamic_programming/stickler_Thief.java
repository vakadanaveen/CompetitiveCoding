//Gfg: Stickler Thief
//Narasimha karumanchi : DP problem-9

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
	public static void main (String[] args) {
		//code
		Scanner s= new Scanner(System.in);
		int t=s.nextInt();
	
		for(int i=0;i<t;i++){
		    int n=s.nextInt();
		    int[] a = new int[n];
		    	int ans=-999999;
		    for(int j=0;j<n;j++){
		        a[j]=s.nextInt();
		    }
		    int[] m =  new int[n];
		    for(int j=0;j<n;j++){
		        if(j==0) m[0]=a[0];
		        else if(j==1){
		            if(a[0]>a[1]) m[1]=a[0];
		            else m[1]=a[1];
		        }
		        else{
		            if(a[j]+m[j-2]>m[j-1]) m[j]=a[j]+m[j-2];
		            else m[j]=m[j-1];
		        }
		        
		        if(m[j]>ans) ans=m[j];
		    }
		    System.out.println(ans);
		}
	}
}