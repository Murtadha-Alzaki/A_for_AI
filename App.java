/*
***************************************
I will make some changes.
See how it looks when someone else
contributes to your code.
The changes that I will make will be in c++ 
so it won't work in your code. It's just for 
learning purposes.
*/
public class App {
private String name ;
private double rate;
private int downloads ;
public App(){
    name = "NewApp";
    rate = 0.0;
    downloads  = 5;
}

        public void setApp(String na, double ra, int down){
name = na ;
            if (ra >= 0.0 && ra<= 5.0){
                rate = ra ;
            }else {
        System.out.println("Invaild values"); ;
            }
            if (down>0){
                downloads = down ;
            }else {
              System.out.println("Invaild values"); ;}
}
public String getName(){
   return  name;}
   public double getRate(){
    return rate;}
    public int getDownloads(){
    return downloads;}
    public boolean isTopApp(){
        if(rate==5.0 && downloads> 100){
            return  true;

        }else{
            return false;
        }
    }}

// This is a hello world program in c++

// First include this library which allows you
// to use input and output streams
#include<iostream>

// Then add the following to be able
// to use "methods" and other stuff 
// from the "iostream" library
using namespace std;

int main(){
    // cout is: console out, which outputs to the console.
    // endl is: the linebreak.Same as "br" in HTML.
 cout<<"Hello World!"<<endl;   
}
