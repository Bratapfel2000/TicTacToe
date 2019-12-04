import java.util.Arrays;
import java.util.Scanner;

public class TicTacJoe_0012_beta {

  //creates fields from 0-x with numbers 1-x
     public static int [] createFields(int x) {
        int[] c = new int[x];
        for (int i = 0; i < x; i++) {
            c[i] = i+1;
        }
        return c;        
    }      

  //creates fields from 0-x with numbers 1-x
     public static String [] createStringFields(int x) {
        String[] d = new String[x];
        for (int i = 0; i < x; i++) {
            d[i] = Integer.toString(i+1);
        }
        return d;        
    }     
     
        //Int Scanner, for entering board numbers
        public static int scanInt() {
        Scanner in = new Scanner(System.in);
        while (true) {
            System.out.print("Enter a number: ");
            if (in.hasNextInt()) {
                break;
            }
            String word = in.next();
            System.err.println(word + " is not a number");
        }
        int x = in.nextInt();
        return x;
    }
        
        //Player X
        public static String [] makeStringMove_x(String [] j) {
          if (
              (
           (j[0] == "X" || j[0] == "O") &&
           (j[1] == "X" || j[1] == "O") &&
           (j[2] == "X" || j[2] == "O") &&
           (j[3] == "X" || j[3] == "O") &&
           (j[4] == "X" || j[4] == "O") &&
           (j[5] == "X" || j[5] == "O") &&
           (j[6] == "X" || j[6] == "O") &&  
           (j[7] == "X" || j[7] == "O") &&  
           (j[8] == "X" || j[8] == "O")   
           ) 
          )
      {
        printStringFields(j);
        System.out.println("Board Full. Game Over!");
        return new String[] { "hello", "world" };
      }
          else{printStringFields(j);
            System.out.println("Player X");
            int x = scanInt();
            String[] stringField = j; 
            if (j[x-1] == "X" || j[x-1] == "O"){
              System.out.println("Already occupied. Try another field");
              return  makeStringMove_x(j);
            } 
            stringField[x-1] =  "X";
            if ((j[0] == "X" && j[1] == "X" && j[2] == "X") ||
                (j[3] == "X" && j[4] == "X" && j[5] == "X") ||
                (j[6] == "X" && j[7] == "X" && j[8] == "X") ||
                (j[0] == "X" && j[4] == "X" && j[8] == "X") ||
                (j[2] == "X" && j[4] == "X" && j[6] == "X")
                  )
              {printStringFields(j);
              System.out.println("Player X Wins!");
              return new String[] { "hello", "world" };
            } 
               else{
                  return makeStringMove_o(j);}
      }     
    }     
       
        //Player O
        public static String [] makeStringMove_o(String [] j) {
      if (
          (
          (j[0] == "X" || j[0] == "O") &&
           (j[1] == "X" || j[1] == "O") &&
           (j[2] == "X" || j[2] == "O") &&
           (j[3] == "X" || j[3] == "O") &&
           (j[4] == "X" || j[4] == "O") &&
           (j[5] == "X" || j[5] == "O") &&
           (j[6] == "X" || j[6] == "O") &&  
           (j[7] == "X" || j[7] == "O") &&  
           (j[8] == "X" || j[8] == "O")   
          )  )
      {
        printStringFields(j);
        System.out.println("Board Full. Game Over!");
        return new String[] { "hello", "world" };
      }
      else{
          printStringFields(j);
          System.out.println("Player O");
          int x = scanInt();
          String[] stringField = j; 
          
          if (j[x-1] == "X" || j[x-1] == "O"){
          System.out.println("Already occupied. Try another field");
          return  makeStringMove_o(j);
          } 
          stringField[x-1] =  "O";
          if ((j[0] == "O" && j[1] == "O" && j[2] == "O") ||
              (j[3] == "O" && j[4] == "O" && j[5] == "O") ||
              (j[6] == "O" && j[7] == "O" && j[8] == "O") ||
              (j[0] == "O" && j[4] == "O" && j[8] == "O") ||
              (j[2] == "O" && j[4] == "O" && j[6] == "O")
                 ){printStringFields(j);
            System.out.println("Player O Wins!");
            return new String[] { "hello", "world" };
          } 
               else{
                  return makeStringMove_x(j);}
      }     
    }     
               
  // creates  board
     public static void printFields() {
       int[] field = createFields(9);
       System.out.printf("%d  %d  %d \n",
                          field[0], field[1], field[2]);
      System.out.printf("%d  %d  %d \n",
                          field[3], field[4], field[5]);      
      System.out.printf("%d  %d  %d \n",
                          field[6], field[7], field[8]);
      }         
         
    //print fields 
     public static void printStringFields(String [] j) {
       String[] stringField = j;
       System.out.println(stringField[0] +" "+ stringField[1] +" "+ stringField[2]);
      System.out.println(stringField[3] +" "+  stringField[4] +" "+  stringField[5]);      
      System.out.println(stringField[6] +" "+  stringField[7] +" "+  stringField[8]);
      }           
             
    public static void main(String[] args) {      
      String [] startFields = createStringFields(9);
      makeStringMove_x(startFields);
    }
}
