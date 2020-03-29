import java.util.Scanner;
public class AppTest {
public static void main(String[] args){
  App Api = new App();
  Scanner k= new Scanner(System.in);
  System.out.println("Enter the name: ");
  String na = k.next();
  System.out.println("Enter the rate :");
  double ra = k.nextDouble();
  System.out.println("Enter the downloads numbers:");
  int down = k.nextInt();
  Api.setApp(na,ra,down);

if(Api.isTopApp()){
  System.out.println("The app is top app");

}else{
  System.out.println("It is not a top app");

}


}

}
