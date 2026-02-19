class staticA
{
    int x=10;
    int y=20;
    static void show()
    {
       // System.out.println(this); error
       // System.out.println(super);  error
    }
   public static void main(String arg[])
   {
     A ob=new A();
      A.show();
   }
}
