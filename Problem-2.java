import java.utill.Scanner;
class Odd
{
  public static void main(String args[])
  {
    int n;
    System.out.print("Enter No of Term ");
    Scanner r=new Scanner(System.in);
    n=r.nextInt();
    for(int i=1;i<=n; i=i+2)
    {
      System.out.print(i);
    }
  }
}
