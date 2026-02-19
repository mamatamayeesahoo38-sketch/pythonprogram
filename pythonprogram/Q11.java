import java.util.*;
class Q11
{
	public static void main(String []arg)
	{
		Scanner sc=new Scanner(System.in);
		System.out.println("enter principle");
		int p=sc.nextInt();
		System.out.println("enter time");
		int t=sc.nextInt();
		System.out.println("enter rate of interest");
		int r=sc.nextInt();
		int SI=p*t*r/100;
		System.out.println("principle="+p);
		System.out.println("time="+t);
		System.out.println("rate of interest="+r);
		System.out.println("simpole interest="+SI);
	}
}