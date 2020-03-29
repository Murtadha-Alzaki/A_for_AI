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


