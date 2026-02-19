class privatestatic
{
   private static int data;
    static void show()
    {
        data=10;
        System.out.println(data); //10
    }
}
class Test
{
    public static void main(String arg[])
    {
         
           privatestatic.show();
         //System.out.println(A.data);//10 error

    }

}
