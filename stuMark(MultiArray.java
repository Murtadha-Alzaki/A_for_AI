import java.util.Scanner;
import javax.print.DocFlavor;
import javax.swing.*;
public class stuMark {
    public static final int ROWS= 5;
    public static final int COLUMN = 10 ;
    public static void main (String[] args){
        Scanner k =new Scanner(System.in);
        double[][] table = new double[ROWS][COLUMN];
        System.out.println("Enter the  5 student 10 assingment marks:");
        for(int row= 0 ; row< ROWS; row++ ){
            for (int column =0 ; column< COLUMN; column++){
                table[row][column]= k.nextDouble();
            }
        }
        int count ;

        for(int j =0 ; j < COLUMN ; j++){
            count = 0 ;
            for( int i =0 ; i<  ROWS ; i++){
                if(table[i][j]==10){
                    count++;

                }

            }
            System.out.println("#full mark in assignment(" + (j+1)+ ")="+ count);

        }

    }}
